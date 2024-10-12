import json
import os

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse


router = APIRouter()

view_sort=10
view_desc="demo2页面"
amis_json = {
    "type": "page",
    "title": "demo",
    "body": {
        "type": "form",
        "api": "/demo",
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
__all__=["amis_json","view_desc"]



