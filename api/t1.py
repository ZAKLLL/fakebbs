import json
import os

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from webUI import templateCfg
router = APIRouter()


amis_json = {
    "type": "page",
    "title": "fuckTest",
    "body": {
        "type": "form",
        "api": "/fuckF",
        "body": [
            {
                "type": "textarea",
                "label": "输入文本",
                "name": "input_text",
                "placeholder": "请输入要转换的文本"
            },
            {
                "type": "button",
                "label": "转换",
                "actionType": "submit",
                "level": "primary"
            },
            {
                "type": "textarea",
                "label": "输出文本",
                "name": "output_text",
                "readOnly": True
            }
            ]
        }
    }

    
    

@router.get("/f", response_class=HTMLResponse,description="f1页面")
async def read_index():
    return templateCfg.render(amis_json)
    


@router.post("/fuckF")
async def convert_text(request:Request):
    # 这里实现你的转换逻辑
    data = await request.json()
    output_text = data['input_text'].upper()  # 示例：将输入文本转换为大写
    return JSONResponse(content={"output_text": output_text+"fuck"})

