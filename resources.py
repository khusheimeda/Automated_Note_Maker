from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests

f = open('resources1.txt','w')
resp = requests.get("https://www.bestcollegereviews.org/50-top-online-learning-sites/")
http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
encoding = html_encoding or http_encoding
soup = BeautifulSoup(resp.content, from_encoding=encoding)
l = []
j1 = []
for link in soup.find_all("div",attrs={'class':'entry-content'}):
    j = link.find_all('p')
    k = link.find_all('ul')
    for i in j:
        if i.find('strong'):
            j1.append(i)
    print(j1)
    print(k)
    #f.write(str(i) + '.' + link['href'] + '\n')
f.close()

