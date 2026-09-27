# ASTRAL

Static multi-page website for the Astral Discord bot collection. BALAN is the first bot. Built with Python's standard library; the deployed files need no backend or build service.

## Generate the site

```bash
python3 site.py
```

Optional verified values:

```bash
BALAN_CLIENT_ID=YOUR_NUMERIC_DISCORD_APPLICATION_ID ASTRAL_SUPPORT_EMAIL=you@example.com python3 site.py
```

The invite link remains disabled until `BALAN_CLIENT_ID` is set. It requests the `bot` and `applications.commands` scopes without hard-coded permissions; configure actual permissions and installation settings in Discord Developer Portal. The Status page deliberately reports monitoring as unavailable until a trusted uptime source is integrated.

## Publish with GitHub Pages

1. Create a new repository in your GitHub account, for example `astral-site`.
2. Upload the **contents of `dist/`** to the repository root (including `.nojekyll`), or publish `dist/` with a GitHub Actions Pages deployment. The root `index.html` must be in the published directory.
3. In **Settings → Pages**, choose deployment from the repository's main branch and `/ (root)`; wait for the Pages URL to become available.
4. If you own `astral.ro`, add it under **Settings → Pages → Custom domain**, configure DNS as instructed by GitHub, then enable **Enforce HTTPS** when available. Add a `CNAME` file containing `astral.ro` to `dist/` before the next upload. Do not point DNS or add CNAME until the domain is under your control.
5. Once the site is live and policies accurately describe BALAN, put the actual public `/legal/privacy/balan/` and `/legal/terms/balan/` URLs into Discord Developer Portal.

For `username.github.io/astral-site/`, relative navigation and asset paths work from the project subpath. For a custom root domain, the same output works without changes.

## Before publishing BALAN policies

The legal pages are **drafts** with conspicuous placeholders. Check them against the running bot before submitting the URLs to Discord. Verify the operator identity, contact, actual data received and retained, legal basis, hosting and subprocessors, retention and deletion, transfers, bot permissions, and any paid features. Replace bracketed text and remove the draft banners once reviewed. Review whenever features change.

To add another bot, create its page and its own privacy and terms pages in `site.py`, then regenerate. The reusable `shell` handles navigation, metadata and shared layout.
