import json
import os

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse


router = APIRouter()

view_sort=10
view_desc="demo2页面"
view_body=[
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

amis_json = {
    "type": "page",
    "title": "demo",
    "body": {
        "type": "form",
        "api": "/c/doProcess",
        "body":view_body 
        }
    }
__all__=["amis_json","view_desc"]


inputJson=  {
                "type": "textarea",
                "name": "input_text",
                "label": "输入文本",
                "placeholder": "请输入要转换的文本"
            }





@router.post("/c/doProcess")
async def doProcess(request:Request):
    # 这里实现你的转换逻辑
    data = await request.json()





