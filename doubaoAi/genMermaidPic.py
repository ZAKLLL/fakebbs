import os
import urllib.parse
import time
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


   # return True
    # return
# print("-------------------"+"开始渲染图片")    
# ops=Options()
# ops.add_argument('--headless=new')  # 新版Chrome的无头模式写法
# ops.add_argument('--disable-gpu')  # 禁用GPU加速
# ops.add_argument('--no-sandbox')  # 禁用沙盒模式
# ops.add_argument('--window-size=1920x1080')  # 设置窗口大小 
# ops.add_argument('--disable-dev-shm-usage')  # fix:DevToolsActivePort file doesn't exist

# # 设置页面语言和字符编码
# ops.add_argument('--lang=zh-CN')  # 设置页面语言为简体中文
# ops.add_argument('--charset=utf-8')  # 设置字符编码为UTF-8
# # 设置字体渲染
# ops.add_argument('--font-render-hinting=none')  # 禁用字体渲染提示，可能有助于解决字体显示问题

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=ops)

def render_mermaid(mermaid_code,task_path):
    
    # return True
    # return
    print("-------------------"+"开始加载无头浏览器")    
    ops=Options()
    ops.add_argument('--headless=new')  # 新版Chrome的无头模式写法
    ops.add_argument('--disable-gpu')  # 禁用GPU加速
    ops.add_argument('--no-sandbox')  # 禁用沙盒模式
    ops.add_argument('--window-size=1920x1080')  # 设置窗口大小 
    ops.add_argument('--disable-dev-shm-usage')  # fix:DevToolsActivePort file doesn't exist
    # 设置页面语言和字符编码
    ops.add_argument('--lang=zh-CN')  # 设置页面语言为简体中文
    ops.add_argument('--charset=utf-8')  # 设置字符编码为UTF-8
    # 设置字体渲染
    ops.add_argument('--font-render-hinting=none')  # 禁用字体渲染提示，可能有助于解决字体显示问题
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=ops)
    try:
        print("-------------------"+"加载无头浏览器完毕")    
        # 加载index.html并且替换{{mermain_code}}为参数内容
        with open('doubaoAi/index.html', 'r') as file:
            filedata = file.read()
        filedata = filedata.replace('{{mermaid_code}}', mermaid_code)
        
        print("-------------------"+"开始渲染图片")
        driver.get("data:text/html;charset=utf-8," + urllib.parse.quote(filedata))
        
        # 等待Mermaid图渲染完成
        # 你可能需要调整等待时间，或者使用更可靠的等待机制
        time.sleep(5)
        # 获取Mermaid图的元素
        mermaid_graphs = driver.find_elements("class name", 'mermaid')
        index=0
        for mermaid_graph in mermaid_graphs:
            # 保存Mermaid图为png
            screenshot = mermaid_graph.screenshot_as_png
            with open(os.path.join(task_path, "images", f"{index}.png"), 'wb') as file:
                file.write(screenshot)
            index+=1
        print("-------------------"+"渲染图片结束")    
    except Exception as e:
        print(f"------------------渲染图片异常 An error occurred: {e}")
    finally:
        driver.quit()
        print("-------------------"+"退出无头浏览器")    
        
# render_mermaid(mermaid_code=mermaid_code)

