# Nateblendz sample site

A one-page sample website for Nateblendz, a barber in Tustin, CA. Booking happens on Booksy; this site helps visitors choose a service and sends them there. It is a private sample until Nathan approves it.

While it's a sample, search engines are blocked (`noindex, nofollow` in the page, `Disallow: /` in `robots.txt`). Before go-live: flip noindex back and confirm photo permission with Nathan (GO-LIVE.md step 0).

## Files

| File | What it is |
| --- | --- |
| `index.html` | The English page. All styles and scripts are inside it. |
| `es/index.html` | The Spanish page. Generated from `index.html`, so don't edit it by hand. |
| `tools/build_es.py` | Rebuilds the Spanish page. Run `python3 tools/build_es.py` after any change to `index.html`. |
| `favicon.svg` | The "NB" browser-tab icon. |
| `og-image.png` | The 1200x630 picture shown when the link is shared in texts or social posts. |
| `robots.txt`, `sitemap.xml`, `llms.txt` | Files for search engines and AI tools. |
| `GO-LIVE.md` | Launch-day checklist. |

## Adding photos

Make a `photos` folder next to `index.html` and save photos with these exact names. Each photo replaces its placeholder automatically; any missing photo keeps the placeholder.

| File name | Where it shows |
| --- | --- |
| `low-fade.jpg`, `mid-fade.jpg`, `high-fade.jpg`, `taper.jpg`, `line-up.jpg` | Cut gallery (the fade guide uses drawings) |
| `gallery-taper.jpg`, `gallery-fade.jpg`, `gallery-design.jpg`, `gallery-beard.jpg` | Cut gallery (portrait, 4:5 crop works best) |
| `before-1.jpg` + `after-1.jpg`, `before-2.jpg` + `after-2.jpg` | Before-and-after slots in the cut gallery (both files of a pair are needed; the card and its filter stay hidden until then) |

Only use photos Nathan has approved for the site.

The photos in `photos/` now come from Nathan's Tustin Booksy portfolio (downloaded 2026-10-16). Booksy only labels them "Haircut" or "Haircut & Beard", so the cut-type matches were judged by eye. They are for the private preview; get Nathan's permission before launch.

## Changing text

Most text has an English version between the tags and a Spanish version in its `data-es` attribute. Change both, then rebuild the Spanish page.
