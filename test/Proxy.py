import requests

proxy = {'http':'118.122.92.252:37901'}
header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

url = 'http://www.whatismyip.com'
response = requests.get(url, proxies=proxy, headers=header)
response.encoding = 'utf-8'
print(response.text)