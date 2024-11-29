# 将markdown文件转换为word文件
import pypandoc
import os
from pathlib import Path
import shutil  # 新增导入
import fileinput

from docx import Document
from docxcompose.composer import Composer

def split_markdown_file(input_file, chunk_size, task_path):
    """Split markdown file into smaller chunks and copy images"""
    temp_dir = os.path.join(task_path, "temp_md")
    os.makedirs(temp_dir, exist_ok=True)
    
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
        
    chunks = []
    current_chunk = []
    current_size = 0
    
    for line in lines:
        current_chunk.append(line)
        current_size += len(line.encode('utf-8'))
        
        if current_size >= chunk_size:
            chunks.append('\n'.join(current_chunk))
            current_chunk = []
            current_size = 0
    
    if current_chunk:
        chunks.append('\n'.join(current_chunk))
    
    chunk_files = []
    for i, chunk in enumerate(chunks):
        chunk_file = os.path.join(temp_dir, f"chunk_{i:03d}.md")
        with open(chunk_file, 'w', encoding='utf-8') as f:
            f.write(chunk)
        chunk_files.append(chunk_file)
    
    return chunk_files 

def process_chunk_file(chunk_file, task_path):
    """Process a single chunk file to replace image paths and convert to HTML"""
    with fileinput.FileInput(chunk_file, inplace=True, backup='.bak', mode='r', encoding='utf-8') as file:
        for line in file:
            if '![' in line and ']' in line and '(' in line and ')' in line:  # 检查是否有图片
                img_path = task_path.replace('\\','/')+"/"+(line.split('(')[1].split(')')[0])[2:]
                line = line.replace(line.split('(')[1].split(')')[0], img_path)  # 替换图片路径
            print(line, end='')

    import markdown
    with open(chunk_file, "r", encoding="utf-8") as md_file:
        md_content = md_file.read()
    return markdown.markdown(md_content)


def merge_word_documents(word_files, final_path):
    """Merge multiple Word documents into a single document"""
    final_doc = Document(word_files[0])
    composer = Composer(final_doc)
    for doc_path in word_files[1:]:
        doc = Document(doc_path)
        composer.append(doc)

    # Save final combined document
    composer.save(final_path)
    print(f"Successfully combined all chunks into {final_path}")

def convert_md_to_word(input_file, task_path, chunk_size=5000):
    try:
        # Create output directories
        os.makedirs(os.path.join(task_path, "documents"), exist_ok=True)
        
        # # Split the markdown file and get images directory
        # chunk_files = split_markdown_file(input_file, chunk_size, task_path)
        
        # # Convert each chunk to Word
        # word_files = []
        # for chunk_file in chunk_files:
        #     html_content = process_chunk_file(chunk_file, task_path)
        #     file_name = os.path.basename(chunk_file).split('.')[0]
        #     target_file = os.path.join(task_path, "documents", f"{file_name}.docx")
        #     create_word_document(chunk_file, target_file)
        #     word_files.append(target_file)
        #     print(f"Successfully converted chunk {chunk_file} to {target_file}")

        with fileinput.FileInput(input_file, inplace=True, backup='.bak', mode='r', encoding='utf-8') as file:
            for line in file:
                if '![' in line and ']' in line and '(' in line and ')' in line:  # 检查是否有图片
                    img_path = task_path.replace('\\','/')+"/"+(line.split('(')[1].split(')')[0])[2:]
                    line = line.replace(line.split('(')[1].split(')')[0], img_path)  # 替换图片路径
                print(line, end='')

        # # Merge all Word documents
        input_name = os.path.basename(input_file).split('.')[0]
        final_path = os.path.join(task_path, "documents", f"{input_name}.docx")
        # merge_word_documents(word_files, final_path)
        output = pypandoc.convert_file(input_file, 'docx', outputfile=final_path)
        print(f'生成文件成功：{final_path}')

        return final_path
    except Exception as e:
        print(f"Error converting file: {str(e)}")

# def main():
#     # 创建参数解析器
#     parser = argparse.ArgumentParser(description='Convert Markdown to Word document')
#     parser.add_argument('-i', '--input', required=True, help='Input markdown file path')
#     parser.add_argument('-o', '--output', required=True, help='Output Word file path')
    
#     args = parser.parse_args()
#     convert_md_to_word(args.input, args.output)

# if __name__ == '__main__':
#     main()