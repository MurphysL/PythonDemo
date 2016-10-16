import re
import urllib.request 

def getHtml(url):
    html = urllib.request.urlopen(url).read()
    html = html.decode('utf-8')
    return html

def getImg(html):
    reg = r' src="(.*?\.jpg)" pic_ext="jpeg"'
    img = re.compile(reg)
    imagelist = img.findall(html)
    
    x=0
    print("start")
    for imgurl in imagelist:
        print(imgurl)
        urllib.request.urlretrieve(imgurl, "%s.jpg" % x)
        x += 1
    print("finish")

print(getHtml("http://tieba.baidu.com/p/3885457501"))
getImg(getHtml("http://tieba.baidu.com/p/3885457501"))














