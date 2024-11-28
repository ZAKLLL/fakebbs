import os
import urllib.parse
import time
from selenium import webdriver

from selenium.webdriver.edge.options import Options



def render_mermaid(mermaid_code,task_path):

    
    ops=Options()
    ops.add_argument('--headless')  # 确保无头模式生效
    ops.add_argument('--disable-gpu')  # 禁用GPU加速
    ops.add_argument('--no-sandbox')  # 禁用沙盒模式
    ops.add_argument('--window-size=1920x1080')  # 设置窗口大小 
    driver = webdriver.Edge(options=ops)

    # 加载index.html并且替换{{mermain_code}}为参数内容
    with open('doubaoAi/index.html', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('{{mermaid_code}}', mermaid_code)
    
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
    
    driver.quit()

# render_mermaid(mermaid_code=mermaid_code)

