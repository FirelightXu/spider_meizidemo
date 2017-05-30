#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
created on 2017年5月29日

@author: xuye
'''
'''
import requests
from Download import request
from bs4 import BeautifulSoup
import os
from pymongo import MongoClient
import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''

'''
headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
all_url = 'http://www.mzitu.com/all'
start_html = requests.get(all_url,headers=headers)

Soup = BeautifulSoup(start_html.text,'lxml')

all_a = Soup.find('div',class_='all').find_all('a')
for a in all_a:
    title = a.get_text()
#     print type(title)
    path = str(title).strip()
#     print path
    # print path
    os.makedirs(os.path.join("/Users/xuye/Documents/spider_meizidemo",path))
    os.chdir("/Users/xuye/Documents/spider_meizidemo/"+path)
    href = a['href']
    html = requests.get(href,headers=headers)
    html_Soup = BeautifulSoup(html.text,'lxml')
#     print href
#     print html_Soup.find('div',class_='pagenavi').find_all('span')
    max_span = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1,int(max_span)+1):
        page_url = href + '/' + str(page)
        img_html = requests.get(page_url,headers=headers)
        img_Soup = BeautifulSoup(img_html.text,'lxml')
        img_url = img_Soup.find('div',class_='main-image').find('img')['src']
        
        name = img_url[-9:-4]
        img = requests.get(img_url,headers=headers)
        f = open(name+'.jpg','ab')
        f.write(img.content)
        f.close()

class mzitu():
    def all_url(self,url):
        html = self.request(url)
        all_a = 


def request(url):
    headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    content = requests.get(url,headers=headers)   
    return content 

def mkdir(self,path):
    path = path.strip()
    isExists = os.path.exists(os.path.join("/Users/xuye/Documents/spider_meizidemo",path))
    if not isExists:
        print(u'建了一个名字叫做',path,u'的文件夹')
        os.makedirs(os.path.join("/Users/xuye/Documents/spider_meizidemo",path))
        return True
    else:
        print "已经存在了"
        return False
#         print img_url

#     print max_span
#     print title,href
    
#     print a

# li_list = Soup.find_all('li')
# for li in li_list:
#     print li

# print start_html.text
'''
from bs4 import BeautifulSoup
import os
from Download import down ##导入模块变了一下
from pymongo import MongoClient
import datetime

import sys
from email.header import _max_append
reload(sys)
sys.setdefaultencoding('utf-8')

class mzitu():

    def __init__(self):
        client = MongoClient() ##与MongDB建立连接（这是默认连接本地MongDB数据库）
        db = client['meinvxiezhenji'] ## 选择一个数据库
        self.meizitu_collection = db['meizitu'] ##在meizixiezhenji这个数据库中，选择一个集合
        self.title = '' ##用来保存页面主题
        self.url = '' ##用来保存页面地址
        self.img_urls = [] ##初始化一个 列表  用来保存图片地址

    def all_url(self, url):
        html = down.get(url, 3)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            self.title = title ##将主题保存到self.title中
            print(u'开始保存：', title)
            path = str(title).replace("?", '_')
            self.mkdir(path)
            os.chdir("/Users/xuye/Documents/spider_meizidemo/"+path)
            href = a['href']
            self.url = href ##将页面地址保存到self.url中
            if self.meizitu_collection.find_one({'主题页面': href}):  ##判断这个主题是否已经在数据库中、不在就运行else下的内容，在则忽略。
                print(u'这个页面已经爬取过了')
            else:
                self.html(href)

    def html(self, href):
        html = down.get(href, 3)
        max_span = BeautifulSoup(html.text, 'lxml').find_all('span')[10].get_text()
        page_num = 0  ##这个当作计数器用 （用来判断图片是否下载完毕）
        for page in range(1, int(max_span) + 1):
            page_num = page_num + 1 ##每for循环一次就+1  （当page_num等于max_span的时候，就证明我们的在下载最后一张图片了）
            page_url = href + '/' + str(page)
            self.img(page_url, max_span, page_num)  ##把上面我们我们需要的两个变量，传递给下一个函数。

    def img(self, page_url, max_span, page_num): ##添加上面传递的参数
        img_html = down.get(page_url, 3)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.img_urls.append(img_url) ##每一次 for page in range(1, int(max_span) + 1)获取到的图片地址都会添加到 img_urls这个初始化的列表
        if int(max_span) == page_num: ##我们传递下来的两个参数用上了 当max_span和Page_num相等时，就是最后一张图片了，最后一次下载图片并保存到数据库中。
            self.save(img_url)
            post = {  ##这是构造一个字典，里面有啥都是中文，很好理解吧！
                '标题': self.title,
                '主题页面': self.url,
                '图片地址': self.img_urls,
                '获取时间': datetime.datetime.now()
            }
            self.meizitu_collection.save(post) ##将post中的内容写入数据库。
            print(u'插入数据库成功')
        else:  ##max_span 不等于 page_num执行这下面
            self.save(img_url)


    def save(self, img_url):
        name = img_url[-9:-4]
        print(u'开始保存：', img_url)
        img = down.get(img_url, 3)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("/Users/xuye/Documents/spider_meizidemo", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("/Users/xuye/Documents/spider_meizidemo", path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False




Mzitu = mzitu() ##实例化
Mzitu.all_url('http://www.mzitu.com/all') ##给函数all_url传入参数  你可以当作启动爬虫（就是入口）