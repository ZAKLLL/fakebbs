import shutil
import doubaoAi.genMdWord as genMdWord
import doubaoAi.genWordMd as genWordMd
import os
from datetime import datetime  # 直接导入datetime类
base_path='./workspace'

def initWorkSpace(source_file_path):
    # 使用时间戳创建唯一的任务文件夹
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    task_folder = f"{os.path.basename(source_file_path).split('.')[0]}_{timestamp}"
    task_path = os.path.join(base_path, task_folder)
    # 创建主文件夹
    os.makedirs(task_path, exist_ok=True)
    # 创建子文件夹
    os.makedirs(os.path.join(task_path, "images"), exist_ok=True)
    # 将source_file 放入task_path

    shutil.copy(source_file_path, task_path)  # 直接复制到task_path
    return task_path
def md2Word(source_file_path):
    task_path=initWorkSpace(source_file_path)
    
    # 替换source_file_path为task_path下的文件路径
    source_file_path = os.path.join(task_path, os.path.basename(source_file_path))
    targetPath=genWordMd.doConvert(source_file_path,task_path)
    finalPath=genMdWord.convert_md_to_word(targetPath,task_path)
    return finalPath
# if __name__ == '__main__':
#     md2Word('2024063桥梁健康监测系统项目-概要设计.md')
    
