#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
created on 2017年5月29日

@author: xuye
'''
import requests
import re
import random
import time

class download:
    
    def __init__(self):
        
        self.iplist = ['94.177.236.12','183.88.66.72','198.50.219.230','119.57.105.209','222.94.150.180']
#         html = requests.get("http://haoip.cc/tiqu.htm")
#         iplistn = re.findall(r'r/>(.*?)<b', html.text, re.S)# re.S的意思是包括匹配换行符
#         for ip in iplistn:
#             i = re.sub('\n', '', ip) 
#             self.iplist.append(i.strip())
        
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        
    def get(self,url,timeout,proxy=None,num_retries=6):
        UA = random.choice(self.user_agent_list)
        headers = {'User-Agent':UA}
        if proxy == None:
            try:
                return requests.get(url,headers=headers,timeout=timeout)
            except:
                if num_retries > 0:
                    time.sleep(10)
                    return self.get(url,timeout,num_retries-1)
                else:
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)).strip()) ##下面有解释哦
                    proxy = {'http': IP}
                    return self.get(url, timeout, proxy,)
            response = requests.get(url,headers=headers)
            return response
        else:
            try:
                
                IP = ''.join(str(random.choice(self.iplist)).strip())
                proxy = {'http':IP}
    #             print proxy
                response = requests.get(url,headers=headers,proxies=proxy,timeout=timeout)
                return response
            except:
                if num_retries>0:
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http': IP}
                    print(u'正在更换代理，10S后将重新获取倒数第', num_retries, u'次')
                    print(u'当前代理是：', proxy)
                    return self.get(url, timeout, proxy, num_retries - 1)
                else:
                    print(u'代理也不好使了！取消代理')
                    return self.get(url, 3)
#         response = requests.get(url,headers=headers)
#         return response
Xz = download() ##实例化
print(Xz.get("http://www.mzitu.com/all/").headers) ##打印headers

        
    
    