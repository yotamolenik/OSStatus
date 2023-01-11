import pickle

import click
import requests
from bs4 import BeautifulSoup

from osstatus.cache import CACHE_FILE, ErrorCode, Platform


@click.command()
def cli():
    """ get error code information from the OSStatus website """
    result = {}

    response = requests.get('https://www.osstatus.com/search/results?platform=all&framework=all&search=')
    soup = BeautifulSoup(response.text, 'html.parser')
    for tr in soup.find('tbody').find_all('tr'):
        platforms = []

        if tr.find('span', {'class': 'platform-mac'}):
            platforms.append(Platform.macOS)

        if tr.find('span', {'class': 'platform-ios'}):
            platforms.append(Platform.iOS)

        framework = tr.find('span', {'class': 'ec-framework'}).text
        header_file = tr.find('span', {'class': 'ec-header_file'}).text
        name = tr.find('span', {'class': 'value-symbol'}).text
        description = tr.find('span', {'class': 'ec-description'}).text
        value = int(tr.find('span', {'class': 'value-number'}).text)

        if value not in result:
            result[value] = []

        result[value].append(
            ErrorCode(platforms=platforms, framework=framework, header_file=header_file, name=name, value=value,
                      description=description))

    CACHE_FILE.write_bytes(pickle.dumps(result))


if __name__ == '__main__':
    cli()
