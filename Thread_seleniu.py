#-*- coding:utf-8 -*-

from selenium import webdriver
from time,sys
from threading import Thread

reload(sys)
sys.setdefaultencoding("utf-8")

def test_baidu_search(browser, url):
    driver = None
    if browser == "firefox":
        driver = webdriver.Firefox() 
    elif browser == "chrome":
        driver = webdriver.Chrome() 
    
    if driver == None:
        exit()    
        
    driver.get(url)    
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys("测试")    
    driver.find_element_by_id("su").click()
    time.sleep(3)    
    driver.quit()    
    
if __name__ == "__main__":    
    data = {        
        "firefox":"http://www.baidu.com", 
        "chrome":"http://www.baidu.com"
        }   
    threads = []  
    
    for bro, url in data.items():  
       t = Thread(target=test_baidu_search,args=(bro,url))
       threads.append(t)  
    
    for thr in threads:
        thr.start()
