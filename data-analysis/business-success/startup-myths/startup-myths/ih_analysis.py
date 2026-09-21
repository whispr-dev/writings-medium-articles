"""Indie Hackers dataset analysis (full_data.csv, 2,868 products).
Run:  python ih_analysis.py full_data.csv
Deps: pandas numpy scipy statsmodels matplotlib
"""
import ast, sys, collections
import numpy as np, pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

path = sys.argv[1] if len(sys.argv) > 1 else "full_data.csv"
raw = pd.read_csv(path)
print(f"rows={len(raw)} unique products={raw.link.nunique()}")

def parse(s, default):
    try: return ast.literal_eval(s)
    except Exception: return default

df = raw[raw.revenue.astype(str).str.startswith("$")].copy()       # drop 'does not exist'
df["rev"] = df.revenue.str.replace(r"[$,]", "", regex=True).astype(float)
df["tagl"] = df.tags.map(lambda s: parse(s, None))
print(f"with revenue field={len(df)}  unparseable tags={df.tagl.isna().sum()}  negative rev={(df.rev<0).sum()}")
df = df[df.tagl.notna()].copy()
df["rev0"] = df.rev.clip(lower=0)                                   # negatives = losing money -> 0 revenue
has = lambda t: df.tagl.map(lambda L: t in L)
df["multi"] = has("Multiple Founders"); df["solo"] = has("Solo Founder")
df["code"] = has("Founders Code");      df["nocode"] = has("Founders Don't Code")
df["stripe"] = df.revenue_explanation.eq("stripe-verified revenue")
for t in ["B2B", "B2C", "AI", "SaaS"]: df[t] = has(t)

def gini(x):
    x = np.sort(np.asarray(x, float)); n = len(x)
    return (2*np.sum(np.arange(1, n+1)*x)/(n*x.sum())) - (n+1)/n

def summ(s):
    return dict(n=len(s), zero_pct=round(100*(s<=0).mean(),1), median=s.median(), mean=round(s.mean()),
                p75=s.quantile(.75), p90=s.quantile(.9), p99=s.quantile(.99),
                ge1k_pct=round(100*(s>=1000).mean(),1), ge10k_pct=round(100*(s>=10000).mean(),1))

print("\n=== 1. DISTRIBUTION (monthly revenue, USD) ===")
print(pd.DataFrame({"all": summ(df.rev0), "stripe-verified": summ(df.rev0[df.stripe]),
                    "self-reported": summ(df.rev0[~df.stripe])}).T.to_string())
r = df.rev0.sort_values(ascending=False); tot = r.sum()
print(f"Gini all={gini(df.rev0):.3f}  Gini stripe-only={gini(df.rev0[df.stripe]):.3f}")
for p in (.01, .05, .10, .20):
    k = max(1, int(len(r)*p)); print(f"  top {int(p*100):>2}% ({k} products) hold {100*r.iloc[:k].sum()/tot:.1f}% of revenue")
# power-law tail (Hill estimator on top 10%)
tail = r.iloc[:int(len(r)*.10)].values; xmin = tail[-1]
print(f"  Hill tail exponent alpha (top 10%, xmin=${xmin:,.0f}) = {1/np.mean(np.log(tail/xmin)):.2f}  (<2 => infinite-variance territory)")

def compare(a, b, la, lb, title):
    print(f"\n=== {title} ===")
    print(pd.DataFrame({la: summ(a), lb: summ(b)}).T.to_string())
    u = stats.mannwhitneyu(a, b, alternative="two-sided")
    print(f"Mann-Whitney p={u.pvalue:.2e}   P({la} > {lb}) = {u.statistic/(len(a)*len(b)):.3f}  (0.5 = coin flip)")

compare(df.rev0[df.multi], df.rev0[df.solo], "team", "solo", "2. TEAM vs SOLO")
s = df[df.stripe]; compare(s.rev0[s.multi], s.rev0[s.solo], "team", "solo", "2b. TEAM vs SOLO — stripe-verified only")
compare(df.rev0[df.code], df.rev0[df.nocode], "code", "nocode", "3. FOUNDERS CODE vs DON'T")
compare(df.rev0[df.B2B & ~df.B2C], df.rev0[df.B2C & ~df.B2B], "B2B", "B2C", "4. B2B vs B2C")
compare(df.rev0[df.AI], df.rev0[~df.AI], "AI", "non-AI", "5. AI vs everything else")

print("\n=== 6. CATEGORIES (n>=40), sorted by % reaching $1k/mo ===")
skip = {"Founders Code","Founders Don't Code","Solo Founder","Multiple Founders"} | {t for L in df.tagl for t in L if "Employees" in t}
cnt = collections.Counter(t for L in df.tagl for t in L if t not in skip)
rows = []
for t, n in cnt.items():
    if n >= 40:
        m = has(t); x = df.rev0[m]
        rows.append(dict(tag=t, n=n, median=x.median(), ge1k_pct=round(100*(x>=1000).mean(),1),
                         ge10k_pct=round(100*(x>=10000).mean(),1), zero_pct=round(100*(x<=0).mean(),1)))
cat = pd.DataFrame(rows).sort_values("ge1k_pct", ascending=False)
print(cat.head(12).to_string(index=False)); print("  ..."); print(cat.tail(8).to_string(index=False))

print("\n=== 7. REGRESSION: what predicts reaching $1k/mo? (logit, odds ratios) ===")
X = sm.add_constant(df[["multi","nocode","B2B","B2C","AI","SaaS","stripe"]].astype(float))
fit = sm.Logit((df.rev0>=1000).astype(float), X).fit(disp=0)
print(pd.DataFrame({"odds_ratio": np.exp(fit.params), "p": fit.pvalues}).round(4).to_string())
print("NOTE: employee count deliberately excluded — it's a CONSEQUENCE of revenue, not a cause.")

print("\n=== 8. REPEAT FOUNDERS / PORTFOLIOS ===")
df["fl"] = df.founder_links.map(lambda s: list(parse(s, {})) if isinstance(s, str) else [])
ex = df[["title","rev0","fl"]].explode("fl").dropna(subset=["fl"])
g = ex.groupby("fl").rev0.agg(n="size", total="sum", best="max")
print(f"distinct founder profiles={len(g)}   with 2+ products={(g.n>=2).sum()} ({100*(g.n>=2).mean():.1f}%)   3+={(g.n>=3).sum()}")
m = g[(g.n>=2) & (g.total>0)]
print(f"among multi-product founders with any revenue (n={len(m)}): median share of their revenue from their SINGLE best product = {100*(m.best/m.total).median():.0f}%")
print(f"  ...founders where best product is >=90% of portfolio revenue: {100*((m.best/m.total)>=.9).mean():.0f}%")
one = ex[ex.fl.isin(g.index[g.n==1])].rev0; many = ex[ex.fl.isin(g.index[g.n>=2])].rev0
print(f"per-PRODUCT median: single-product founders ${one.median():,.0f} vs portfolio founders ${many.median():,.0f};  "
      f"% >= $1k: {100*(one>=1000).mean():.1f}% vs {100*(many>=1000).mean():.1f}%")
print(f"per-FOUNDER best product >= $1k: single {100*(g.best[g.n==1]>=1000).mean():.1f}% vs portfolio {100*(g.best[g.n>=2]>=1000).mean():.1f}%")

print("\n=== 9. SANITY: how 'round' are the numbers? (round = exact multiple of $1,000) ===")
for lab, m in (("stripe-verified", df.stripe), ("self-reported", ~df.stripe)):
    x = df.rev0[m & (df.rev0 >= 1000)]
    print(f"  {lab:16s} n={len(x):4d}  round-number share = {100*(x % 1000 == 0).mean():.0f}%")

# ---- charts ----
fig, ax = plt.subplots(1, 3, figsize=(17, 5))
pos = df.rev0[df.rev0>0]
ax[0].hist(np.log10(pos), bins=40, color="#2a6f97"); ax[0].set_title(f"Monthly revenue, log10 USD (n={len(pos)} with rev>0; {100*(df.rev0<=0).mean():.0f}% at $0 not shown)"); ax[0].set_xlabel("log10(USD/mo)")
xs = np.sort(df.rev0.values); L = np.cumsum(xs)/xs.sum()
ax[1].plot(np.linspace(0,1,len(L)), L, color="#c1121f"); ax[1].plot([0,1],[0,1],"k--",lw=.7)
ax[1].set_title(f"Lorenz curve — Gini {gini(df.rev0):.2f}"); ax[1].set_xlabel("share of products"); ax[1].set_ylabel("share of revenue")
rk = np.arange(1, len(pos)+1); ax[2].loglog(rk, np.sort(pos.values)[::-1], ".", ms=3, color="#386641")
ax[2].set_title("Rank vs revenue (log-log): straight line = power law"); ax[2].set_xlabel("rank"); ax[2].set_ylabel("USD/mo")
plt.tight_layout(); plt.savefig("ih_revenue_charts.png", dpi=130)
cat.to_csv("ih_category_table.csv", index=False)
print("\nwrote ih_revenue_charts.png, ih_category_table.csv")
