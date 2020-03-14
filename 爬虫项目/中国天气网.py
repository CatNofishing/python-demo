import requests
from bs4 import BeautifulSoup
import pymysql
from datetime import date

def parse_page(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
               }
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf8')
    soup = BeautifulSoup(text, 'lxml')
    conMidtab = soup.find('div', class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')
        tr = list(trs)[2]
        tds = list(tr.find_all('td'))
        td = list(tds[0].stripped_strings)[0]
        print('*'*20, td, '*'*20)
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            print({'city': city, 'min_temp': min_temp})
            all_data.append({'city': city, 'min_temp': min_temp})


def main(urllist):

    for url in urllist:
        parse_page(url)



if __name__ == '__main__':
    all_data = []
    urllist = ['http://www.weather.com.cn/textFC/hb.shtml', 'http://www.weather.com.cn/textFC/db.shtml', 'http://www.weather.com.cn/textFC/hd.shtml',
               'http://www.weather.com.cn/textFC/hz.shtml', 'http://www.weather.com.cn/textFC/hn.shtml', 'http://www.weather.com.cn/textFC/xb.shtml', 'http://www.weather.com.cn/textFC/xn.shtml']

    main(urllist)
