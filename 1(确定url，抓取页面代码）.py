#coding:utf8
#!/usr/bin/env python
__author__ = 'greatbuger'

import urllib,urllib2,re

class Spider:
    def __init__(self,url):
        self.url = url

    def getPageCode(self):
        url = self.url
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
        headers = { 'User-Agent' : user_agent }
        #print url
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
        #print  response.read().decode('gbk')
        return response.read().decode('gbk')


    def getContents(self):
        page = self.getPageCode()
        print 2

        pattern = re.compile('<div class="tb-mm-main".*?<dd class="mm-info">(.*?)</dd>',re.S)
        items = re.findall(pattern,page)
        print 1
        for item in items:
            print item[0]





url = 'http://mm.taobao.com/search_tstar_model.htm?spm=719.1001036.1998089564.7.smT1DD'
MM  = Spider(url)
