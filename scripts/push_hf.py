"""Copy the checked files to the Hugging Face mirror (AIWorkCentral/ai-training-pay-index). Runs only when the
repository secret HF_TOKEN exists (the workflow skips this step otherwise). The token is read from the environment and
never printed. Same files as the GitHub copy: hf/README.md (the dataset card), the two CSV of data/ and every frozen
edition of data/editions/ (CSV, and JSON when there is one) as editions/<file>, so a new month reaches the mirror on the
day it is frozen. python3 scripts/push_hf.py --dry-run lists the files without a token and pushes nothing."""
import glob
import os
import sys

from huggingface_hub import CommitOperationAdd, HfApi

REPO = 'AIWorkCentral/ai-training-pay-index'
FILES = (('hf/README.md', 'README.md'), ('data/pay-index.csv', 'pay-index.csv'),
         ('data/pay-index-transparency.csv', 'pay-index-transparency.csv'))

FILES += tuple((f, 'editions/' + os.path.basename(f)) for f in sorted(glob.glob('data/editions/*.csv') + glob.glob('data/editions/*.json')))

if '--dry-run' in sys.argv:
    for src, dst in FILES:
        print(f'{src} -> {dst}' + ('' if os.path.exists(src) else '  MISSING'))
    sys.exit(0)
token = os.environ.get('HF_TOKEN', '').strip()
if not token:
    print('HF_TOKEN not set: nothing pushed')
    sys.exit(0)
api = HfApi(token=token)
ops = [CommitOperationAdd(path_in_repo=dst, path_or_fileobj=src) for src, dst in FILES]
info = api.create_commit(repo_id=REPO, repo_type='dataset', operations=ops,
                         commit_message='Pay Index: weekly copy from aiworkcentral.com')
print('pushed to Hugging Face:', info.oid if info else 'no change')
