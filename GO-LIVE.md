# Go-live checklist

Do these only after Nathan approves the site and a domain is bought.

0. Flip noindex back and confirm photo permission:
   - Get Nathan's written OK to use the Booksy photos in `photos/`.
   - In `index.html`, change `<meta name="robots" content="noindex, nofollow">` to `index, follow`, then rebuild the Spanish page.
   - In `robots.txt`, change `Disallow: /` to `Allow: /`.
1. Replace `YOUR-DOMAIN` with the real domain in:
   - `index.html` and `es/index.html` (the commented "Go-live" block in the head; remove the `<!--` and `-->` around it)
   - `sitemap.xml`
   - `robots.txt` (uncomment the Sitemap line)
2. Add the website link to the JSON-LD business data (`"url": "https://YOUR-DOMAIN/"`) in both pages.
3. Remove the "Sample concept" banner and footer note once Nathan approves.
4. Publish, then submit `sitemap.xml` in Google Search Console.
5. Add the website link to the Google Business Profile, Booksy, and Instagram bio.
6. Add approved photos to `photos/` using the names in README.md, and remove any placeholder you don't fill.
7. After any change to `index.html`, run `python3 tools/build_es.py` to update the Spanish page.
8. Swap the two Google Maps links in the "Find us on Google" section for Nathan's real Google Business Profile link (search the code for PLACEHOLDER), and replace the three review slots with reviews Nathan approves (they're hidden for now: remove `hidden` from each `review-slot` you fill).
