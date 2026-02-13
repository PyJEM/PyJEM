Usage
-----

Run this from the repository root to regenerate `index.html` listing available documentation versions:

```bash
python scripts/generate_index.py
```

The script looks for subdirectories that contain `index.html` and treats them as versioned docs. It will pick the highest numeric version (when parseable) as the redirect target.
