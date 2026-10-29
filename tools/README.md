# Zuga Fitness Operational Tools

This directory contains operational scripts that support the build pipeline and maintenance tasks. **These scripts are never user-facing code.**

## Existing Tools

### `validate_schema.py`
- **Purpose**: Validates all JSON-LD schemas in the repository to ensure they are byte-valid.
- **CLI Usage**: `python3 tools/validate_schema.py`
- **Dependencies**: `bs4`, `json`, `glob`

### `build_desk_workers_post.py`
- **Purpose**: Generates the Desk Workers blog post using BeautifulSoup from the Back Pain template.
- **CLI Usage**: `python3 tools/build_desk_workers_post.py`
- **Dependencies**: `bs4`

[... other existing tools documentation continues below ...]

### `validate_schema.py`
- **Purpose**: Validates all JSON-LD schemas in the repository to ensure they are byte-valid.
- **CLI Usage**: `python3 tools/validate_schema.py`
- **Dependencies**: `bs4`, `json`, `glob`

### `build_desk_workers_post.py`
- **Purpose**: Generates the Desk Workers blog post using BeautifulSoup from the Back Pain template.
- **CLI Usage**: `python3 tools/build_desk_workers_post.py`
- **Dependencies**: `bs4`

## `inject_gtm.py`
**Purpose:** Programmatically injects the Google Tag Manager (GTM) script immediately after `<head>` and the `<noscript>` iframe immediately after `<body>` across all `.html` files in the repository. Ensures idempotency to avoid duplicate injection.
**Usage:** `python tools/inject_gtm.py`
**Example Invocation:**
```bash
$ python tools/inject_gtm.py
Processed 174 HTML files.
Injected GTM into 174 files.
```
**Dependencies:** None (uses built-in `os` and `re` modules).
