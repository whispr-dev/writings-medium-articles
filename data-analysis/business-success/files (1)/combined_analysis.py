"""Cross-dataset startup-myths analysis. Six datasets, same questions.
Layout expected (paths relative to this script):
  data/full_data.csv  data/phbench_public_train.csv  data/producthunt_products.csv
  data/2020.csv data/2021.csv data/2022.csv  data/producthunt_12k_2022.csv  data/gumroad-sales.csv
Run:  python combined_analysis.py [data_dir]
Deps: pandas numpy scipy statsmodels matplotlib
"""
import ast, sys, os
import numpy as np, pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = sys.argv[1] if len(sys.argv) > 1 else "data"
P = lambda f: os.path.join(D, f)

def gini(x):
    x = np.sort(np.asarray(x, float)); x = x[~np.isnan(x)]; n = len(x)
    return (2*np.sum(np.arange(1, n+1)*x)/(n*x.sum())) - (n+1)/n
def top_share(x, p):
    x = np.sort(np.asarray(x, float))[::-1]; return 100*x[:max(1, int(len(x)*p))].sum()/x.sum()

# ---------- load ----------
ih = pd.read_csv(P("full_data.csv")); ih = ih[ih.revenue.astype(str).str.startswith("$")].copy()
ih["rev"] = ih.revenue.str.replace(r"[$,]", "", regex=True).astype(float).clip(lower=0)
def tl(s):
    try: return ast.literal_eval(s)
    except Exception: return None
ih["tagl"] = ih.tags.map(tl); ih = ih[ih.tagl.notna()]
ih["multi"] = ih.tagl.map(lambda L: "Multiple Founders" in L); ih["AI"] = ih.tagl.map(lambda L: "AI" in L)
ih["B2B"] = ih.tagl.map(lambda L: "B2B" in L); ih["B2C"] = ih.tagl.map(lambda L: "B2C" in L)

pb = pd.read_csv(P("phbench_public_train.csv"), low_memory=False); pb["y"] = pb.label_series_a_within_18m.astype(int)
pp = pd.read_csv(P("producthunt_products.csv"))
ph3 = pd.concat([pd.read_csv(P(f"{y}.csv")).assign(year=y) for y in (2020, 2021, 2022)], ignore_index=True)
num = lambda c: pd.to_numeric(c.astype(str).str.replace(",", "", regex=False), errors="coerce")
ph3["Upvotes"] = num(ph3.Upvotes); ph3 = ph3[ph3.Upvotes.notna()]
pp["votes_count"] = num(pp.votes_count).fillna(0)
ph12 = pd.read_csv(P("producthunt_12k_2022.csv")); ph12["upvotes"] = pd.to_numeric(ph12.upvotes, errors="coerce")
gs = pd.read_csv(P("gumroad-sales.csv")); gs = gs[pd.to_numeric(gs.sales_count, errors="coerce").notna()].copy()
gs["gross"] = pd.to_numeric(gs.sales_count)*pd.to_numeric(gs.price_usd, errors="coerce").fillna(0)

# ---------- 1. the lottery shape, everywhere ----------
print("=== 1. IS IT A LOTTERY? (Gini: 0 = everyone equal, 1 = one winner takes all) ===")
series = {
  "Indie Hackers: monthly revenue":            ih.rev,
  "Gumroad: units sold x price (disclosers)":  gs.gross,
  "PHBench featured launches: votes":          pb.votesCount,
  "Product Hunt 2020-22: upvotes":             ph3.Upvotes,
  "Product Hunt 12k (2022 scrape): upvotes":   ph12.upvotes.dropna(),
  "PH raw launches (incl. unfeatured): votes": pp.votes_count,
}
series = {k: pd.to_numeric(v, errors="coerce").dropna().clip(lower=0) for k, v in series.items()}
rows = [dict(dataset=k, n=len(v), median=np.median(v), mean=round(np.mean(v), 1), gini=round(gini(v), 3),
             top1pct_share=round(top_share(v, .01), 1), top10pct_share=round(top_share(v, .10), 1)) for k, v in series.items()]
lot = pd.DataFrame(rows); print(lot.to_string(index=False))

# ---------- 2. team size ----------
print("\n=== 2. TEAM SIZE vs OUTCOME ===")
print("-- Indie Hackers: % reaching $1k/mo --")
print(ih.groupby("multi").rev.agg(n="size", median="median", ge1k=lambda s: round(100*(s >= 1000).mean(), 1)).rename(index={False: "solo", True: "team"}).to_string())
pb["mk"] = pd.cut(pb.maker_count, [-1, 0, 1, 2, 3, 5, 99], labels=["0 listed", "1", "2", "3", "4-5", "6+"])
base = pb.y.mean()
t = pb.groupby("mk", observed=True).agg(n=("y", "size"), series_a=("y", "sum"), rate_pct=("y", lambda s: round(100*s.mean(), 2)), median_votes=("votesCount", "median"))
t["x_baseline"] = (t.rate_pct/(100*base)).round(2)
print(f"-- PHBench: Series A within 18 months, by maker count (baseline {100*base:.2f}%) --"); print(t.to_string())
pp["mk"] = pd.cut(pp.maker_count, [-1, 0, 1, 2, 99], labels=["0 listed", "1", "2", "3+"])
print("-- PH raw launches: votes by maker count --")
print(pp.groupby("mk", observed=True).agg(n=("votes_count", "size"), median_votes=("votes_count", "median"), mean_votes=("votes_count", "mean"), viral_pct=("is_viral", lambda s: round(100*s.mean(), 1))).round(1).to_string())

# ---------- 3. does team survive controls? ----------
print("\n=== 3. PHBench LOGIT: Series A ~ team + traction + segment + year (odds ratios) ===")
X = pd.DataFrame({"log_votes": np.log1p(pb.votesCount), "makers_2": (pb.maker_count == 2).astype(float),
                  "makers_3plus": (pb.maker_count >= 3).astype(float), "no_makers_listed": (pb.maker_count == 0).astype(float),
                  "ai_topic": pb.is_ai_topic.astype(float), "b2b_topic": pb.is_b2b_topic.astype(float),
                  "consumer_topic": pb.is_consumer_topic.astype(float), "prime_window": pb.is_prime_window.astype(float)})
X = pd.concat([X, pd.get_dummies(pb.launch_year, prefix="yr", drop_first=True).astype(float)], axis=1)
fit = sm.Logit(pb.y, sm.add_constant(X)).fit(disp=0, maxiter=200)
ci = np.exp(fit.conf_int()); lg = pd.DataFrame({"odds_ratio": np.exp(fit.params), "ci_lo": ci[0], "ci_hi": ci[1], "p": fit.pvalues}).round(4)
print(lg.drop(index=[i for i in lg.index if i.startswith("yr_") or i == "const"]).to_string())
print("(baseline = exactly 1 maker, non-AI, non-B2B, non-consumer, 2019. log_votes OR is per ~2.7x more votes.)")

# ---------- 4. segment + AI ----------
print("\n=== 4. SEGMENTS ===")
for lab, m in (("B2B topic", pb.is_b2b_topic == 1), ("consumer topic", pb.is_consumer_topic == 1), ("AI topic", pb.is_ai_topic == 1), ("not AI", pb.is_ai_topic == 0)):
    print(f"  PHBench {lab:15s} n={m.sum():6d}  Series A rate={100*pb.y[m].mean():.2f}%  ({pb.y[m].mean()/base:.2f}x)  median votes={pb.votesCount[m].median():.0f}")
tc = [c for c in pb.columns if c.startswith("topic_") and c != "topic_count"]
tr = pd.DataFrame([dict(topic=c[6:], n=int(pb[c].sum()), series_a=int(pb.y[pb[c] == 1].sum()), rate_pct=round(100*pb.y[pb[c] == 1].mean(), 2)) for c in tc]).sort_values("rate_pct", ascending=False)
print("-- PHBench topic flags, Series A rate --"); print(tr.to_string(index=False))
print("-- AI over time (PHBench): share of launches tagged AI, and Series A rate AI vs not --")
ay = pb.groupby("launch_year").apply(lambda g: pd.Series(dict(ai_share_pct=round(100*g.is_ai_topic.mean(), 1), ai_rate=round(100*g.y[g.is_ai_topic == 1].mean(), 2), nonai_rate=round(100*g.y[g.is_ai_topic == 0].mean(), 2), ai_series_a=int(g.y[g.is_ai_topic == 1].sum()))), include_groups=False)
print(ay.to_string())
print(f"-- Indie Hackers: AI reach $1k = {100*(ih.rev[ih.AI]>=1000).mean():.1f}% vs non-AI {100*(ih.rev[~ih.AI]>=1000).mean():.1f}%;  B2B-only {100*(ih.rev[ih.B2B&~ih.B2C]>=1000).mean():.1f}% vs B2C-only {100*(ih.rev[ih.B2C&~ih.B2B]>=1000).mean():.1f}%")
print(f"-- PH raw launches: AI median votes {pp.votes_count[pp.is_ai_product==1].median():.0f} (n={(pp.is_ai_product==1).sum()}) vs non-AI {pp.votes_count[pp.is_ai_product==0].median():.0f};  viral: AI {100*pp.is_viral[pp.is_ai_product==1].mean():.1f}% vs {100*pp.is_viral[pp.is_ai_product==0].mean():.1f}%")

# ---------- 5. does launch hype buy funding? ----------
print("\n=== 5. DO VOTES PREDICT FUNDING? (PHBench) ===")
pb["vq"] = pd.qcut(pb.votesCount, 10, labels=False, duplicates="drop")
vd = pb.groupby("vq").agg(min_votes=("votesCount", "min"), max_votes=("votesCount", "max"), n=("y", "size"), series_a=("y", "sum"), rate_pct=("y", lambda s: round(100*s.mean(), 2)))
print(vd.to_string())
rk = pb[pb.daily_rank.notna() & (pb.has_daily_rank == 1)]
print(f"  #1 of the day: n={(rk.daily_rank==1).sum()}, Series A rate {100*rk.y[rk.daily_rank==1].mean():.2f}%  => {100*(1-rk.y[rk.daily_rank==1].mean()):.1f}% of daily winners did NOT raise a Series A in 18 months")
auc = stats.mannwhitneyu(pb.votesCount[pb.y == 1], pb.votesCount[pb.y == 0]).statistic/((pb.y == 1).sum()*(pb.y == 0).sum())
print(f"  P(a funded launch had more votes than an unfunded one) = {auc:.3f}")

# ---------- 6. pricing + timing ----------
print("\n=== 6. SIDE DISHES ===")
print("-- PH 2020-22: upvotes by pricing type --")
print(ph3.groupby(ph3.PricingType.fillna("(not stated)")).Upvotes.agg(n="size", median="median", mean="mean").round(1).to_string())
print("-- PHBench: Tue-Thu 'prime window' vs rest --")
print(pb.groupby("is_prime_window").agg(n=("y", "size"), median_votes=("votesCount", "median"), series_a_pct=("y", lambda s: round(100*s.mean(), 2))).to_string())

# ---------- charts ----------
fig, ax = plt.subplots(2, 2, figsize=(15, 10))
for k, v in series.items():
    xs = np.sort(np.asarray(v, float)); ax[0, 0].plot(np.linspace(0, 1, len(xs)), np.cumsum(xs)/xs.sum(), label=f"{k.split(':')[0]} (G={gini(v):.2f})")
ax[0, 0].plot([0, 1], [0, 1], "k--", lw=.7); ax[0, 0].legend(fontsize=7); ax[0, 0].set_title("Lorenz curves: every platform is a lottery"); ax[0, 0].set_xlabel("share of products"); ax[0, 0].set_ylabel("share of revenue / votes")
ax[0, 1].bar(t.index.astype(str), t.rate_pct, color="#2a6f97"); ax[0, 1].axhline(100*base, color="r", ls="--", label=f"baseline {100*base:.2f}%"); ax[0, 1].legend()
ax[0, 1].set_title("PHBench: Series A rate by number of makers"); ax[0, 1].set_xlabel("makers on the launch"); ax[0, 1].set_ylabel("% raising Series A in 18 mo")
ax[1, 0].bar([f"{a}-{b}" for a, b in zip(vd.min_votes, vd.max_votes)], vd.rate_pct, color="#386641"); ax[1, 0].tick_params(axis="x", rotation=45, labelsize=7)
ax[1, 0].set_title("PHBench: Series A rate by vote decile"); ax[1, 0].set_ylabel("%")
ax[1, 1].plot(ay.index, ay.ai_rate, "o-", label="AI-tagged"); ax[1, 1].plot(ay.index, ay.nonai_rate, "s-", label="not AI"); ax[1, 1].legend()
ax2 = ax[1, 1].twinx(); ax2.bar(ay.index, ay.ai_share_pct, alpha=.15, color="gray"); ax2.set_ylabel("% of launches tagged AI (grey bars)")
ax[1, 1].set_title("AI: more launches every year, funding edge?"); ax[1, 1].set_ylabel("Series A rate %")
plt.tight_layout(); plt.savefig("combined_charts.png", dpi=125)
lot.to_csv("lottery_table.csv", index=False); tr.to_csv("phbench_topic_rates.csv", index=False)
print("\nwrote combined_charts.png, lottery_table.csv, phbench_topic_rates.csv")
