import requests

def pretty_print_request(req):
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))
    
req = requests.Request('GET','http://httpbin.org/cookies/set/MySecretSessionID/1234'),headers={'X-Custom':'Test'})
prepared = req.prepare()
pretty_print_request(prepared)

req = requests.Request('POST','http://httpbin.org',headers={'X-Custom':'Test'},data='a=1&b=2')
prepared = req.prepare()
pretty_print_request(prepared)

deckID = "5afe9579-53e7-4ef2-9a14-d4312d73bc56"

print(requests.get('https://www.keyforgegame.com/api/decks/?page=1&page_size=10&search=r.%20petrov%2C%20the%20minefield%20ranger').content)