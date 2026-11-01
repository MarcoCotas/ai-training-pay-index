"""Check the two downloaded files and copy them into data/. Fails (and nothing is committed) when a file is not what
this repository promises: the expected header, at least one platform line, and no line for a platform whose terms name
benchmarking or aggregation (left out by the publisher too). Each monthly edition is also kept as data/editions/<edition>.csv."""
import csv, os, shutil, sys

MAIN_HEAD = ['edition', 'as_of', 'section', 'name', 'field', 'open_roles', 'hourly_usd_rates', 'p25_usd', 'median_usd', 'p75_usd']
TRANS_HEAD = ['edition', 'as_of', 'platform', 'open_roles', 'roles_with_pay_figure', 'pct_with_pay_figure',
              'hourly_usd_rates', 'pct_hourly_usd', 'referral_link_on_site']
LEFT_OUT = ('mercor', 'terac')


def rows(path, head):
    with open(path, encoding='utf-8', newline='') as f:
        r = list(csv.reader(f))
    if not r or r[0] != head:
        sys.exit(f'{path}: unexpected header {r[0] if r else None}')
    return r[1:]


main, trans = sys.argv[1], sys.argv[2]
m = rows(main, MAIN_HEAD)
t = rows(trans, TRANS_HEAD)
if not any(x[2] == 'platform' for x in m):
    sys.exit('pay-index.csv: no platform line')
for path, data, col in ((main, m, 3), (trans, t, 2)):
    bad = [x[col] for x in data if x[col].strip().lower() in LEFT_OUT]
    if bad:
        sys.exit(f'{path}: lines for {sorted(set(bad))}, which this repository leaves out')
os.makedirs('data/editions', exist_ok=True)
shutil.copy(main, 'data/pay-index.csv')
shutil.copy(trans, 'data/pay-index-transparency.csv')
for ed in sorted({x[0] for x in m}):
    shutil.copy(main, f'data/editions/{ed}.csv')
print(f'ok: {len(m)} lines, editions {sorted({x[0] for x in m})}')
