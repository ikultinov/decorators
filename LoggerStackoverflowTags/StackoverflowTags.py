import requests

from Decorator.Decorators import outer


@outer
def getting_questions_on_tag(tag):
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': '1654905600', 'todate': '1655164800',
              'tagged': tag, 'site': 'stackoverflow'}
    response = requests.get(url, params=params)
    for i in response.json()['items']:
        print(i.get('title'))


if __name__ == '__main__':
    getting_questions_on_tag("Python")
