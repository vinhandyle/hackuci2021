
import json
import urllib.error
import urllib.request


def failure_report(code: int) -> None:
    '''
    Displays a message describing the error that occurred when accessing the API
    '''
    print(code, end = ' ')
    if code == 400:
        print('Bad Request: API could not process action.')
    elif code == 403:
        print('Forbidden: API rate limit exceeded.')
    elif code == 404:
        print('Not Found: Requested resource could not be found.')
    elif code == 500:
        print('Internal Server Error: API encountered a server problem.')
    elif code == 503:
        print('Service Unavailable: API is offline for maintenance.')

def download_page(url: str) -> dict:
    '''
    Given a url, opens and downloads the content from the corresponding webpage.
    The content stored and returned as a dict.
    '''
    response = None

    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        data = response.read().decode(encoding = 'utf-8')
        return json.loads(data)

    except urllib.error.HTTPError as e:
        failure_report(e.code)

    finally:
        if response != None:
            response.close()
