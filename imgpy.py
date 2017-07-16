# -*- coding:utf-8 -*-
import urllib
import urllib2     # 导入urllib2模块
import os
import re         # 导入re模块
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Cookie': 'passwordMember=; JSESSIONID=543C29CA2DC35E930EB3E51AEACCE933'
}
imgurl = 'https://www.ituba.cc/fengjingtupian/'
request = urllib2.Request(imgurl, None, header)
req = urllib2.urlopen(request)
# req = urllib2.urlopen('http://www.didavc.com/')
buf = req.read()

listurl = re.findall(r'src="([^>]+\.jpg)"', buf)  # 正则表达式，匹配图片格式
# print '222222222', listurl   # 将图片的格式放入list中


if not listurl:
    print 'not found....'
else:
    filepath = os.getcwd() + '\pythonimg'                     # 将下载到的图片存在当前目录的pythonimg文件夹下
    if os.path.exists(filepath) is False:
        os.mkdir(filepath)
    x = 0
    print u'爬虫准备就绪...'
    for imgurl in listurl:
        temp = filepath + '\%s.jpg' % x
        print u'正在下载第%s张图片' % x
        print imgurl
        reg = '../'
        imgurl = imgurl.replace(reg, '')
        # newUrl = 'http://www.didavc.com/' + imgurl
        newUrl = imgurl
        print newUrl, temp
        urllib.urlretrieve(newUrl, temp)
        x += 1
        print u'图片下载完毕，保存路径为' + filepath
