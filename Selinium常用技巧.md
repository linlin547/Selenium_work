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
