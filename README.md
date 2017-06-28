# 搜集selenium的一些常用知识
  * 使用Grid
    * 必须先启动hub：Java -jar selenium-server-standalone-3.3.0.jar -role hub
    * 启动节点，改变端口即可：Java -jar selenium-server-standalone-3.3.0.jar -role node -port 5555 -hub http://27.0.0.1:4444/grid/register 
      * -hub url 为节点指定hub地址，这个地址启动hub时，会显示
    * 剩下就是在脚本中指定节点地址即可
    <pre><code>
      driver = webdriver.Remote(
            command_executor=节点地址,
            desired_capabilities={
                'platform': 'ANY',
                'browserName': 指定浏览器,
                'version': '',
                'javascriptEnabled': True
            }
        )
    </pre></code>
