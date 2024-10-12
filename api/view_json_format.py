import json
import os

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse


router = APIRouter()

view_sort=3
view_desc="JSON格式化"
amis_json = {
    "type": "page",
    "asideResizor": 'true',
    # "asideMinWidth": 150,
    # "asideMaxWidth": 400,
    "aside": [
        {
         "type": "textarea",
         "label": "输入文本",
         "name": "json",
         "placeholder": "请输入要格式化的文本",
         "value":{"a":123}
        }
    ],
    "body":[       
        {
            "type": "json",
            "source":"${json}"
        }
    ]
}
__all__=["amis_json","view_desc"]



