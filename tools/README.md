# Zuga Fitness Operational Tools

This directory contains operational scripts that support the build pipeline and maintenance tasks. **These scripts are never user-facing code.**

## Existing Tools

### `indexnow_ping.py`
- **Purpose**: Batch-POSTs recently updated URLs to the IndexNow API (`api.indexnow.org`) to accelerate search engine discovery (Bing, Yandex, etc.).
- **Requirement**: Before running, ensure the valid 32-hex IndexNow API key is committed at the repository root as `<key>.txt` (e.g. `7f8e9d2c1b4a5...txt`). The file must contain only the key string on a single line with no trailing newline.
- **CLI Usage**: Run after every merge containing URL changes, passing the full absolute URLs of the changed files.
- **Example Invocation**:
  ```bash
  python tools/indexnow_ping.py https://zugafitness.in/free-trial.html https://zugafitness.in/Blog/yoga-for-desk-workers.html
  ```
- **Dependencies**: Uses Python standard library only (`sys`, `glob`, `json`, `urllib`).

### Other scripts
There are various other Python scripts in this directory (e.g., `fix_yoga_page.py`, `add_pricing_form.py`, `update_schema.py`) utilized for batch updates, DOM manipulation, and repository formatting checks.
