

浏览器SSL处理：

IE的解决方案，对ie浏览器而言，需要添加Desired Capabilities的acceptSslCerts选项为True，代码如下：

#_*_ coding:utf-8 _*_

__author__ = '苦叶子'

from selenium import webdriver

if __name__ == '__main__':

    capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER

    capabilities['acceptSslCerts'] = True

    driver = webdriver.Ie(capabilities=capabilities)

    driver.get(u'https://cacert.org/')

    print driver.title

    driver.quit()

对于firefox浏览器则需要添加FirefoxProfile()的accept_untrusted_certs的选项为True，示例代码如下：
#_*_ coding:utf-8 _*_

__author__ = '苦叶子'

from selenium import webdriver

if __name__ == '__main__':   

    profile=webdriver.FirefoxProfile()

    profile.accept_untrusted_certs=True

    driver=webdriver.Firefox(firefox_profile=profile)

    driver.get(u'https://cacert.org/')

    driver.close()

对于chrome浏览器则需要添加ChromeOptions()的--ignore-certificate-errors选项为True，示例代码如下：
#_*_ coding:utf-8 _*_

__author__ = '苦叶子'

from selenium import webdriver

if __name__ == '__main__':
    options=webdriver.ChromeOptions()

    options.add_argument('--ignore-certificate-errors')

    driver=webdriver.Chrome(chrome_options=options)

    driver.get(u'https://cacert.org/')

    driver.close()

对于在利用上述方式针对不同浏览器处理SSL时，可能还会碰到还是处理不了的情况，比如提示证书损坏、无效等等；如果出现这类情况，请联系网站管理员更新SSL证书。转自苦叶子
