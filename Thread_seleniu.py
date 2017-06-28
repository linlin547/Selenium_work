#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import threading
class Web_info:
    def grid(self):
        d = {'http://127.0.0.1:5559/wd/hub': 'firefox',
             'http://127.0.0.1:5555/wd/hub': 'chrome',
             }
        return d
    def ge(self,dr):
        dr.get("http://www.baidu.com")
        time.sleep(10)
        dr.quit()
if __name__ == '__main__':
    wi = Web_info()
    lis_driver = []
    lis_thread = []
    for host, browser in wi.grid().items():
        driver = webdriver.Remote(
            command_executor=host,
            desired_capabilities={
                'platform': 'ANY',
                'browserName': browser,
                'version': '',
                'javascriptEnabled': True
            }
        )
        lis_driver.append(driver)
    for o in lis_driver:
        th = threading.Thread(target=wi.ge,args=(driver,))
        th.start()
        lis_thread.append(th)
    for n in lis_thread:
        n.join()
