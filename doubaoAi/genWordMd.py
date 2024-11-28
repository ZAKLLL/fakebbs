import shutil
import re
from typing import List, Optional
from pathlib import Path
import doubaoAi.genMermaidPic as genMermaidPic

import os
from datetime import datetime
class MermaidConverter:
    """处理Markdown文件中的Mermaid图表转换为图片的类"""
    
    def __init__(self, source_file_path: str,task_path:Optional[str]=None):
        """
        初始化转换器
        
        Args:
            source_file: 源Markdown文件路径
            target_file: 目标Markdown文件路径，如果为None则自动生成
        """
        self.source_file_path = Path(source_file_path)
        self.task_path=task_path
        self.target_file= self._get_default_target_file()
        self.mermaid_pattern = r"```mermaid\n(.*?)```"

    def _get_default_target_file(self) -> Path:
        """生成默认的目标文件路径"""
        return self.source_file_path.with_name(f"{self.source_file_path.stem}-word{self.source_file_path.suffix}")

    def extract_mermaid_diagrams(self, content: str) -> List[str]:
        """提取所有Mermaid图表代码"""
        return re.findall(self.mermaid_pattern, content, re.DOTALL)

    def generate_mermaid_html(self, mermaid_codes: List[str]) -> str:
        """生成Mermaid HTML代码"""
        return '\n'.join(
            f'<div class="mermaid">\n{code}\n</div>'
            for code in mermaid_codes
        )

    def replace_mermaid_with_images(self, content: str, mermaid_matches: List[str]) -> str:
        """将Mermaid代码替换为图片引用"""
        for index, mermaid_code in enumerate(mermaid_matches):
            content = content.replace(
                f'```mermaid\n{mermaid_code}```',
                f'![{index}](./images/{index}.png)'
            )
        return content

    def convert(self) -> None:
        """执行转换流程"""
        try:
            # 读取源文件
            with open(self.source_file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 提取Mermaid图表
            mermaid_matches = self.extract_mermaid_diagrams(content)
            
            # 复制源文件到目标文件
            shutil.copy(self.source_file_path, self.target_file)

            mmcodes=self.generate_mermaid_html(mermaid_matches)    

            # 生成图片
            genMermaidPic.render_mermaid(mmcodes,self.task_path)

            # 替换Mermaid代码为图片引用
            with open(self.target_file, 'r', encoding='utf-8') as file:
                content = file.read()
            
            content = self.replace_mermaid_with_images(content, mermaid_matches)

            # 写入修改后的内容
            with open(self.target_file, 'w', encoding='utf-8') as file:
                file.write(content)

            print(f'生成文件成功：{self.target_file}')

        except Exception as e:
            # 打印错误堆栈
            import traceback
            traceback.print_exc()
            # print(f'转换过程中出现错误：{str(e)}')
        return self.target_file

def doConvert(source_file_path:str,task_path:str):
    converter = MermaidConverter(source_file_path,task_path)
    return converter.convert()

# def main():
#     """主函数"""
#     source_file = '2024063桥梁健康监测系统项目-概要设计.md'
#     converter = MermaidConverter(source_file)
#     converter.convert()

