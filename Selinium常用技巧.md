# Selenium 一些常用技巧：
  * Frame定位：
  <pre>
    driver.switch_to.frame(0)  # 1.用frame的index来定位，第一个是0
    driver.switch_to.frame("frame1")  # 2.用id来定位
    driver.switch_to.frame("myframe")  # 3.用name来定位
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  # 4.用WebElement对象来定位
  </pre>
  * Frame切换：
  <pre>
    driver.switch_to.parent_frame() # 切换到父frame
    driver.switch_to.default_content() # 由frame切换回默认文档
  </pre>
* 页面滑动区域：
  <pre>
    # 列表区域，里面包含展示列表，滑动会加载新的数据
    sp_scop_ele = (By.CSS_SELECTOR, 'div.flow-table > div.list')
    scop_ele_obj = wait_ele(driver, sp_scop_ele)
    # 滑动 1000像素 
    # arguments[0]:获取传递参数对象，在这个对象基础上进行滑动
    driver.execute_script('arguments[0].scrollTop += 1000', scop_ele_obj)
    time.sleep(1)
  </pre>
