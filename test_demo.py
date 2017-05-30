#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
created on 2017年5月29日

@author: xuye
'''

import requests
import re
import random
from bs4 import BeautifulSoup

iplist = []
html = requests.get("http://www.ip181.com/")
ip_ = BeautifulSoup(html.text,'lxml').find('div', class_='col-md-12')#.find_all('td')
print ip_

# iplistn = re.findall(r'r/>(.*?)<b', html.text, re.S)# re.S的意思是包括匹配换行符
# for ip in iplistn:
#     i = re.sub('\n', '', ip) 
#     iplist.append(i.strip())