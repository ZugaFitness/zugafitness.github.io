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

## Anusha Portfolio Updates
The following scripts were used to modify the `Anusha-Portfolio.html` file by manipulating the DOM directly using regular expressions:
- `add_animations.py`: Add intersection observer for fade in animations.
- `clean_old_cta.py`: Cleans up the old CTA section.
- `fix_missing_specialties.py`: Restores the specialties section structure.
- `fix_reels.py`: Fixes closing div issues in the reels marquee.
- `fix_syntax.py`: Fixes general HTML syntax issues.
- `replace_bio.py`: Replaces the biography content.
- `replace_cta.py`: Replaces the call-to-action content.
- `replace_gallery.py`: Overhauls the gallery layout.
- `replace_hero.py`: Redesigns the hero section with a video background.
- `replace_reels.py`: Replaces static reels with auto-sliding ones.
- `replace_reels3.py`: Refines the marquee animation and dimensions.
- `replace_specialties.py`: Replaces specialties content.
- `replace_specialties2.py`: Finishes specialties replacements.

Usage: Run these via `python <script_name>.py` to regenerate the DOM state if testing.

- `generate_wlc_sales_page.py`: Generates the 90-Day Weight Loss Challenge sales page HTML content.
- `add_promo_bar.py`: Injects the WLC promo bar into `index.html` and `Online-Dance-Fitness-Classes.html`.
- `update_whatsapp_concierge.py`: Adds exclusions to the WhatsApp concierge script.
- `update_sitemap.py`: Updates the sitemap with priority 0.8 and today's lastmod for the WLC page.
