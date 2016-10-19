'''
Created on 2016年10月18日

@author: lenovo
'''


class UrlManager(object):
    
    def __init__(self):
        self.old_url_list = set()
        self.new_url_list = set()
    
    def get_new_url(self):
        new_url = self.new_url_list.pop()
        self.old_url_list.add(new_url)
        return new_url
  
    def add_new_urls(self , urls):
        if len(urls) == 0 or urls is None:
            return
        for url in urls:
            self.add_new_url(url)
    
    
    def add_new_url(self , url):
        if url is None:
            return
        if url not in self.old_url_list and url not in self.new_url_list:
            self.new_url_list.add(url)
        
    
    def has_new_url(self):
        return len(self.new_url_list) != 0
  
    
    



