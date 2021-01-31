
import data
import urllib.parse


class PokeData:
    base_url = 'https://api.pokemontcg.io/v1/cards?'
    
    def __init__(self, query: {str: [str]}) -> None:
        self._query = query
        self._url = self._construct_url(query)

    def __repr__(self):
        return f'PokeData({self._query})'

    def __str__(self):
        return self._url

    def query(self) -> {str: [str]}:
        return self._query

    def result(self) -> dict:
        return data.download_page(self._url)

    def _construct_url(self, query: {str: [str]}) -> str:
        '''
        Given a dict of query items, returns a URL that can be processed by the
        Pokemon TCG API.
        '''
        params = urllib.parse.urlencode([
            (name, ('|'.join(item for item in items)))
            for name, items in query.items()])
        return PokeData.base_url + params.replace('%7C', '|')
