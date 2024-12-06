import json
import os
from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from doubaoAi import main  # 导入 doubaoAi 包中的 main 函数
from base.amisRet  import AmisRet
from fastapi import FastAPI, BackgroundTasks

router = APIRouter()

view_sort=1
view_desc="markdown2Word"
amis_json = {
    "type": "page",
    "title": "demo",
    "body": {
        "type": "form",
        "api": "/md2word",
        "body": [
            {
                "type": "input-file",
                "name": "file",
                "label": "File(单选)",
                "mode": "horizontal",
                "labelAlign": "left",
                "accept": ".md",
                "receiver": "/md2word",
                "multiple": "false",
                "autoUpload": "false",
                "joinValues": "false",
                "onEvent": {
                "success": {
                    "actions": [
                    {
                        "actionType": "toast",
                        "args": {
                        "msgType": "info",
                        "msg": "「${event.data.path}」上传成功"
                        }
                    }
                    ]
                }
                }
            },
            {
                "type": "button",
                "label": "转换",
                "actionType": "submit",
                "level": "primary"
            },
            {
                "type": "textarea",
                "label": "下载地址",
                "name": "output_text",
                "readOnly": True
            }
        ]
    }
}
__all__=["amis_json","view_desc"]



@router.post("/md2word")
async def demo(request: Request, file: UploadFile = File(...)):

    import doubaoAi.main
    
    temp_file_path = os.path.join("./temp", file.filename)
    
    # 确保临时目录存在
    os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
    
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(file.file.read())

    # 获取绝对路径
    absolute_temp_file_path = os.path.abspath(temp_file_path)

    task_path= main.initWorkSpace(absolute_temp_file_path)
    retFile = doubaoAi.main.md2Word(absolute_temp_file_path,task_path)  # 使用绝对路径
    print("fffffffffffffffff",retFile)
    relative_retFile = os.path.relpath(retFile) 
    print(relative_retFile)
    # workspace\2024063桥梁健康监测系统项目-概要设计_20241128_145338\documents\2024063桥梁健康监测系统项目-概要设计-word_combined.docx
    ret="/md2word/download?filePath=" + relative_retFile.split("workspace")[1].replace("\\", "/")
    #运行完毕之后清除 temp 中的临时文件
    os.remove(temp_file_path)
    return AmisRet.ok({"output_text":ret})

def write_markdown_file(temp_file_path, markdown_content):
    with open(temp_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

@router.post("/md2word/string")
async def demo_string(request: Request, background_tasks: BackgroundTasks):
    body = await request.json()
    markdown_content = body["mdData"]
    fileName = body["fileName"]
    print("---------->",body)
    temp_file_path = os.path.join("./temp", fileName + ".md")
    os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
    write_markdown_file(temp_file_path, markdown_content)

    
    absolute_temp_file_path = os.path.abspath(temp_file_path)
    task_path= main.initWorkSpace(absolute_temp_file_path)
    background_tasks.add_task(main.md2Word, absolute_temp_file_path,task_path)

    ret = "http://139.9.223.239/md2word/download?filePath="+task_path.split("workspace")[1].replace("\\", "/")+"/documents/"+fileName+"-word.docx"
    return AmisRet.ok({"downloadLink": ret})

@router.get("/md2word/download")
async def download_file(filePath: str):
    filePath="./workspace"+filePath
    # 检查文件是否存在
    if not os.path.exists(filePath):
        return JSONResponse(status_code=201, content={"message": "文件正在生成中，请稍后再试!"})

    # 下载的文件名试用文件全名
    fileName=os.path.basename(filePath)
    return FileResponse(filePath,filename=fileName)  # 返回文件以供下载


