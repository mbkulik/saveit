import sys
import requests
from bs4 import BeautifulSoup


if len(sys.argv) < 2:
    print('Enter a url to save for later')
    sys.exit(1)

for url in sys.argv[1:]:

    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        print('1. [{0}]({1})'.format(soup.title.string, r.url))
    except requests.exceptions.ConnectionError as e:
        print('ERROR: skipping {0}'.format(url), file=sys.stderr)
