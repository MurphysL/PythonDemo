'''
Created on 2016年10月18日

@author: lenovo
'''
from baidu_spider import url_manager , html_parser, html_output , html_download

class SpiderMain(object):
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.OutPut()
        self.downloader = html_download.DownLoad()
    
    def crew(self, root_url):
        print(root_url)
        self.urls.add_new_url(root_url)
        i = 1
        
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d , %s" %(i , new_url))
                html_cont = self.downloader.download(new_url)
                new_urls , new_data = self.parser.parse(new_url , html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                i += 1
                if i>500:
                    break
            except Exception as e:
                print("craw failed%s"%e)
    
        self.outputer.output_html()
    



if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.crew(root_url)
    print("finish")
    
    
    
    
    
    
    
    
    