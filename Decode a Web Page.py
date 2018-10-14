import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')
title1 = soup.find_all('h2')
title2 = soup.find_all('span')
all_title = title1 + title2
articles = []
for item in all_title:
    if 'New York Times' in item.get_text():
        pass
    elif 'Music' in item.get_text():
        pass
    elif 'Books' in item.get_text():
        pass
    elif 'SEARCH' in item.get_text():
        pass
    elif 'Site' in item.get_text():
        pass
    elif 'via' in item.get_text():
        pass
    elif '2018' in item.get_text():
        pass
    elif 'Sections' in item.get_text():
        pass
    elif 'Politics' in item.get_text():
        pass
    elif 'Magazine' in item.get_text():
        pass
    elif 'New York' in item.get_text():
        pass
    elif 'Getty Images' in item.get_text():
        pass
    elif 'AP' in item.get_text():
        pass
    elif 'Associated Press' in item.get_text():
        pass
    elif 'Newsletter' in item.get_text():
        pass
    else:
        articles.append(item.get_text())

articles = list(filter(None, articles))
for item in articles:
    print(item)

#{"class": "balancedHeadline"}
#{"class":"css-1y86ca1 es182me2"}