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
