---
license: cc-by-4.0
pretty_name: AI Training Pay Index
language:
  - en
tags:
  - ai-training
  - data-annotation
  - rlhf
  - pay
  - labor-market
size_categories:
  - n<1K
configs:
  - config_name: pay_index
    data_files: pay-index.csv
  - config_name: transparency
    data_files: pay-index-transparency.csv
---

# AI Training Pay Index

What AI training platforms list as hourly pay for their open roles (rating model answers, writing expert examples,
checking code, medical and legal review), by platform and by field. Monthly editions, measured from public job posts.

Published by [AI Work Central](https://aiworkcentral.com), which reads the public job lists of 22 AI training platforms
once a day. The page with charts, the method and the full notes: **https://aiworkcentral.com/pay-index**

The median listed hourly rate of each edition, with the number of rates behind it, is the `all` line of `pay-index.csv`; the page shows the same figures.

## Files

| File | What it holds |
|---|---|
| `pay-index.csv` | The current edition: all platforms, by platform, by field, open to the EU or not, and platform by field |
| `pay-index-transparency.csv` | For each platform: open roles, how many list any pay, how many list an hourly USD rate |
| `editions/YYYY-MM.csv` | One file per monthly edition |

Columns of `pay-index.csv`: `edition, as_of, section, name, field, open_roles, hourly_usd_rates, p25_usd, median_usd, p75_usd`.
`hourly_usd_rates` is the number of listed hourly rates behind the figures. A platform line with fewer than 5 rates keeps
its counts and leaves the quartiles empty.

## How the numbers are made

- Listed pay, not earnings: each posting counts at the midpoint of the hourly range it lists, or its single figure; a
  posting that says "up to $X" counts at X.
- A role a platform posts once per country counts once.
- A range a platform puts on almost all of its roles (not the pay of any one role) is left out of the medians.
- Hourly rates in USD only; per-task, yearly and other currencies are counted separately on the page.
- Two platforms (Mercor and Terac) are left out of every figure, totals included, because their terms of use name
  benchmarking or aggregation.

## Licence and how to cite

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Reuse, chart or republish freely with credit:

> AI Work Central, AI Training Pay Index, <edition>, https://aiworkcentral.com/pay-index

The licence covers these figures. Platform names belong to their owners and are not licensed.

## Updates

A GitHub Action copies the files from aiworkcentral.com every Monday and keeps each monthly edition. Questions or
corrections: hello@aiworkcentral.com

Mirror of https://github.com/MarcoCotas/ai-training-pay-index, which updates every Monday from aiworkcentral.com.
