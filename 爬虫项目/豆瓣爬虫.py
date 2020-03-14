import requests
from lxml import etree
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
           'Referer': 'https://movie.douban.com/cinema/nowplaying/qingdao/'}
url='https://movie.douban.com/cinema/nowplaying/beijing/'
response=requests.get(url,headers=headers)
text=response.text
html=etree.HTML(text)
ul=html.xpath("//div[@id='upcoming']//ul[@class='lists']")[0]
lists=ul.xpath('./li')
movies=[]
for li in lists:
    title=li.xpath('./@data-title')[0]
    duration=li.xpath('./@data-duration')[0]
    region=li.xpath('./@data-region')[0]
    duration=li.xpath('./@data-duration')[0]
    director=li.xpath('./@data-director')[0]
    actor=li.xpath('./@data-actors')[0]
    actor=re.split(r' / ',actor)
    release_date=li.xpath(".//li[@class='release-date']/text()")[0]
    release_date=re.search(r'[^\n ]+',release_date).group()
    image=li.xpath('.//img/@src')[0]
    movie={'title':title,'image':image}
    movies.append(movie)
for i in movies:
    print(i)