"""Rebuild es/index.html from index.html.

Every element with a data-es attribute gets its Spanish text baked in,
and the English text is kept in data-en so the EN/ES toggle still works.
Run from the site folder:  python3 tools/build_es.py   (needs beautifulsoup4)
"""
import json, os
from bs4 import BeautifulSoup

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(here, 'index.html'), encoding='utf-8').read()
soup = BeautifulSoup(src, 'html.parser')
soup.html['lang'] = 'es'

for el in soup.select('[data-es]'):
    el['data-en'] = el.decode_contents()
    es = el['data-es']
    el.clear()
    for node in list(BeautifulSoup(es, 'html.parser').contents):
        el.append(node)

soup.title.string = 'Nateblendz | Barbero en Tustin, CA: fades, tapers y barba'
soup.find('meta', attrs={'name': 'description'})['content'] = (
    'Nateblendz es un barbero en Tustin, CA, en Newport Ave. Fades bajos, medios y altos, '
    'tapers, diseños y perfilado de barba a navaja. Reserva en línea en Booksy.')
soup.find('meta', property='og:title')['content'] = 'Nateblendz | Barbero en Tustin, CA'
soup.find('meta', property='og:description')['content'] = 'Fades, tapers, diseños y barba en Tustin, California. Reserva en Booksy.'
soup.find('meta', property='og:locale')['content'] = 'es_US'
soup.find('meta', property='og:locale:alternate')['content'] = 'en_US'
soup.find(id='lang-en')['aria-pressed'] = 'false'
soup.find(id='lang-es')['aria-pressed'] = 'true'

links = soup.select_one('.langlinks')
links.find('a', hreflang='en')['href'] = '../index.html'
links.find('a', hreflang='es')['href'] = 'index.html'
for tag in soup.select('link[rel="icon"]'):
    tag['href'] = '../' + tag['href']
for img in soup.select('img[src^="photos/"]'):
    img['src'] = '../' + img['src']
for el in soup.select('[data-photo]'):
    el['data-photo'] = '../' + el['data-photo']

for script in soup.find_all('script', type='application/ld+json'):
    data = json.loads(script.string)
    if data.get('@type') == 'FAQPage':
        count = len(data['mainEntity'])
        data['inLanguage'] = 'es'
        data['mainEntity'] = [
            {'@type': 'Question', 'name': d.summary.get_text(),
             'acceptedAnswer': {'@type': 'Answer', 'text': d.select_one('.answer').get_text(' ', strip=True)}}
            for d in soup.select('.faq details')[:count]]
    else:
        data['description'] = 'Barbero en Tustin, California: fades, tapers, diseños y barba.'
    script.string = '\n' + json.dumps(data, indent=1, ensure_ascii=False) + '\n'

out = str(soup).replace('<link rel="canonical" href="https://YOUR-DOMAIN/">',
                        '<link rel="canonical" href="https://YOUR-DOMAIN/es/">', 1)
out = out.replace('<meta property="og:url" content="https://YOUR-DOMAIN/">',
                  '<meta property="og:url" content="https://YOUR-DOMAIN/es/">', 1)
os.makedirs(os.path.join(here, 'es'), exist_ok=True)
open(os.path.join(here, 'es', 'index.html'), 'w', encoding='utf-8').write(out)
print('Wrote es/index.html')
