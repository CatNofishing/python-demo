from lxml import etree
import requests
import re
base_domain = 'https://www.dy2018.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}


def getdetail_urils(url):
    try:
        response = requests.get(url, headers=headers, timeout=5)
    except Exception:
        print('主域名连接超时！')
        return
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url: base_domain+url, detail_urls)
    return detail_urls


def parse_detail_page(url):
    try:
        response = requests.get(url, headers=headers, timeout=5)
    except Exception:
        print('网页连接超时!')
        return
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    movie = {}
    try:
        release_datetime = html.xpath(
            "//div[@class='position']/span[3]/text()")[0]
        release_datetime = re.search(
            r'\d{4}-\d{2}-\d{2}', release_datetime).group()
        img_url = html.xpath("//img/@src")[0]
        img_screenshots = html.xpath('//img/@src')[1]
        message = html.xpath("//div[@id='Zoom']/text()")
        movie['img_url'] = img_url
        movie['img_screenshots'] = img_screenshots
        movie['relase_datetime'] = release_datetime
        movie['img_url'] = img_url
        index = 0
        for info in message:
            if info.startswith('◎译　　名'):
                movie['ch_title'] = info.replace('◎译　　名', '').strip()
            elif info.startswith('◎片　　名'):
                movie['eg_title'] = info.replace('◎片　　名', '').strip()
            elif info.startswith('◎年　　代'):
                movie['year'] = info.replace('◎年　　代', '').strip()
            elif info.startswith('◎产　　地'):
                movie['country'] = info.replace('◎产　　地', '').strip()
            elif info.startswith('◎类　　别'):
                movie['type'] = info.replace('◎类　　别', '').strip()
            elif info.startswith('◎语　　言'):
                movie['language'] = info.replace('◎语　　言', '').strip()
            elif info.startswith('◎字　　幕'):
                movie['subtitle'] = info.replace('◎字　　幕', '').strip()
            elif info.startswith('◎豆瓣评分'):
                movie['score'] = info.replace('◎豆瓣评分', '').strip()
            elif info.startswith('◎导　　演'):
                movie['director'] = info.replace('◎导　　演', '').strip()
            elif info.startswith('◎主　　演'):
                actors = [info.replace('◎主　　演', '').strip()]
                for i in message[index+1:]:
                    if (not i.startswith('◎简　　介')) and (not i.startswith('◎标　　签')):
                        actors.append(i.strip())
                    else:
                        break
                movie['actors'] = actors
            else:
                pass
            index += 1
    except Exception:
        print('这部电影出错!')
    else:
        print(movie)


def spider(page_start, page_end=310):
    base_url = "https://www.dy2018.com/html/gndy/dyzz/index{}.html"
    for i in range(page_start, page_end):
        if i == 1:
            url = base_url.format('')
        else:
            url = base_url.format('_'+str(i+1))
        detail_urls = getdetail_urils(url)
        print('*'*10+f'第{i}页'+'*'*10)
        num = 0
        for detail_url in detail_urls:
            num += 1
            print()
            print(f'第{num}部电影')
            parse_detail_page(detail_url)


if __name__ == '__main__':
    spider(1)
