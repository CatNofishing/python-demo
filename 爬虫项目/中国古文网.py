import requests
import re
import time
start=time.perf_counter()
response=requests.get('https://www.gushiwen.org/')
text=response.content.decode('utf8')
title=re.findall(r'<div class="cont">.*?<b>(.*?)</b>',text,re.S)
dynasty=re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text,re.S)
author=re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.S)
content=re.findall(r'<div class="contson" .*?>(.*?)</div>',text,re.S)
contents=[]
for i in content:
    i=re.sub(r'<.*?>','',i).strip()
    contents.append(i)
poems=[]
for  value in zip(title,dynasty,author,contents):
    poem={}
    title,dynasty,author,contents=value
    poem['title']=title
    poem['author']=author
    poem['dynasty']=dynasty
    poem['content']=contents
    poems.append(poem)
end=time.perf_counter()
print(end-start)
print(poems)
