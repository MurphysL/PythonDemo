'''
Created on 2016年10月18日

@author: MurphySL
'''
import urllib.request


class DownLoad(object):
    
    
    def download(self , url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
          
        if response.getcode() != 200:
            return None
       
        return response.read()  
        
        
    
    



