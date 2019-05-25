import requests
EVENTS_LINK = 'https://www.facebook.com/pg/{}/events/'

class FacebookParser:
    def __init__(self):
        pass

    def get_html(self, company_link_name):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
        r = requests.get(EVENTS_LINK.format(company_link_name, headers=headers))
        print(r.content)

if __name__ == '__main__':
    FacebookParser().get_html('interlinkua')