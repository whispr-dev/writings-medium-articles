# Startup myths vs six datasets — findings sheet

**What this is:** one script (`combined_analysis.py`) asking the same questions of six datasets.
**Where we are:** analysis done, numbers below are real and reproducible. **Next move:** pick a headline, write the article.

Run: `pip install pandas numpy scipy statsmodels matplotlib` then `python combined_analysis.py data`

## The datasets

| Dataset | Rows | Measures | Trust |
|---|---|---|---|
| Indie Hackers (`full_data.csv`) | 2,827 | monthly revenue | medium — 90% self-reported, lopsided sample |
| PHBench train (`phbench_public_train.csv`) | 47,071 | Series A within 18 months (372 yes) | high — the anchor dataset |
| Product Hunt 2020–22 (Kaggle, 3 files) | 32,572 | upvotes, pricing type | medium — popularity only |
| PH raw launches (`producthunt_products.csv`) | 5,624 | votes incl. unfeatured launches | medium — recent, median launch gets 2 votes |
| PH 12k (2022 scrape) | 10,467 | upvotes by category | low — thin |
| Gumroad sales | 316 | units x price | low — only sellers who disclose |

Not used: `collections.csv` (375 curated Product Hunt collections — lists of products, no outcomes to test).

## Finding 1 — Money is a lottery. Attention is much less of one.

| | Gini | Top 1% hold | Top 10% hold |
|---|---|---|---|
| Indie Hackers revenue | 0.92 | 52% | 87% |
| Gumroad gross sales | 0.91 | 48% | 86% |
| PH raw launches, votes | 0.83 | 39% | 82% |
| PH 2020–22, upvotes | 0.60 | 11% | 45% |
| PHBench featured, votes | 0.37 | 6% | 32% |

Two separate platforms, two near-identical revenue curves (0.92 and 0.91). Upvotes among *featured* launches are
far more evenly spread (0.37) — once you're on the front page, everyone gets a decent crowd. The inequality is in
the money, not the applause.

## Finding 2 — Team size is the strongest signal in every dataset that has it.

- **Indie Hackers:** teams reach $1k/mo 56% of the time, solos 29%. Holds on Stripe-verified rows.
- **PHBench:** Series A rate climbs step by step — 1 maker 0.25%, 2 makers 1.02%, 3 makers 1.36%, 4–5 makers 1.83%, 6+ makers 2.88%. That's an **11x gap** between solo and 6+.
- **Survives controls:** holding votes, topic and year fixed, 2 makers = 3.1x the odds of a solo launch, 3+ makers = 4.7x (95% CI 3.5–6.3).
- **PH raw launches:** median votes 2 (solo) vs 15 (3+ makers); "viral" 15% vs 76%.

**The caveat you must print:** 88% of PHBench's Series A companies already had seed money at launch. A launch with six
makers is often an already-funded company with staff, not six mates in a garage. Maker count partly *measures* "already
a real company" rather than *causing* success. Honest wording: "solo launches almost never turn into venture-backed
companies", not "add a co-founder and 4x your odds".

## Finding 3 — AI gets you funded. It doesn't get you paid.

- **PHBench (funding):** AI-tagged launches raise Series A at 1.05% vs 0.72%; 1.6x odds with controls. The edge *grew*: in 2025 AI 1.05% vs non-AI 0.29%, even though AI went from 6% of launches (2019) to 51% (2025).
- **Indie Hackers (revenue):** AI products reach $1k/mo 31% of the time vs 40% for everything else; 0.62x odds.

Investors are paying for AI; customers, on this evidence, less so. Caveat: different populations and the revenue data is
self-reported, so treat it as a strong hint, not proof.

## Finding 4 — Boring B2B wins on both scoreboards.

- PHBench top topics by Series A rate: API 2.5%, Payments 2.5%, Fintech 2.3%, Sales 2.3%. Bottom: Education 0.3%, Marketing 0.5%, Android/iOS/Web App 0.6%.
- B2B topics 1.31% vs consumer 0.50%.
- Indie Hackers: B2B-only reach $1k/mo 55% vs B2C-only 38%. Payments and Sales sit in the top four on *both* platforms.

## Finding 5 — Winning Product Hunt mostly doesn't matter.

- 97.8% of "#1 Product of the Day" winners did **not** raise a Series A within 18 months.
- Votes help (top vote decile 2.22% vs bottom 0.33%), but pick one funded and one unfunded launch at random and the funded one had more votes only 68% of the time.
- Tue–Thu launches: same median votes (100 vs 100), but more than double the Series A rate (1.05% vs 0.47%). That's not timing magic — serious companies pick serious days.

## Finding 6 — Free doesn't buy applause.

PH 2020–22 median upvotes: Free 59, Free Options 76, Payment Required 51. Charging costs you almost nothing in attention.

## Finding 7 — Portfolios are one hit plus satellites. (Indie Hackers only)

8% of founders have 2+ products; their single best product supplies a median 92% of their revenue.

## Headline candidates, ranked by how well the data backs them

1. **"AI Gets You Funded. It Doesn't Get You Paid."** — novel, two datasets pointing opposite ways.
2. **"Solo Launches Raise a Series A 1 Time in 400. Six-Person Teams: 1 in 35."** — biggest, cleanest effect; carry the seed-funding caveat.
3. **"98% of Product Hunt Winners Never Raise a Series A."** — punchy, bulletproof arithmetic.
4. **"Two Platforms, Same Curve: 1% of Indie Products Take Half the Money."**

## What would sink this if ignored

Every dataset is a volunteer sample: people who list on Indie Hackers, launch on Product Hunt, or disclose Gumroad sales.
None is a census of startups. Say "among products on X", never "startups in general".
PHBench data is CC BY 4.0 — credit Ihlamur, Griffin & Chen (arXiv:2605.02974), and its licence bars using it to target specific companies.
