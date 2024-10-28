import json
import os

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from base.amisRet import AmisRet
from webUI import templateCfg
from api import  tools_methods
router = APIRouter()

view_sort=0
view_desc="工具集"
amis_json = {
  "type": "page",
  "body": {
    "type": "form",
    "title": "常用工具集",
    "api": {
      "method": "post",
      "url": "/tools/doProcess",
      "data": {
        "method": "${select_method}",
        "input_text": "${input_text}"
      }
    },
    "body": [
      {
        "label": "工具列表",
        "type": "select",
        "name": "select_method",            
        "source": "/tools/listToolMethods"
      },
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
          "type": "button",
          "label": "复制",
          "actionType": "copy",
          "content": "${output_text}",
          "level": "primary",
          "style": {
              "marginLeft": "10px"  # 设置左边距以增加间隔
          }
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
    
@router.get("/tools", response_class=HTMLResponse,description="工具集")
async def read_index():
    return templateCfg.render(amis_json)
    


@router.get("/tools/listToolMethods")
async def listToolMethods():
    return AmisRet.ok(list(map(lambda x: {"value":x.code,"label":x.name,} ,tools_methods.ToolMethods)))
    





@router.post("/tools/doProcess")
async def doProcess(request:Request):
    # 这里实现你的转换逻辑
    data = await request.json()
    method=data["method"]
    #获取方法
    ms=list(filter(lambda x:x.code==method,tools_methods.ToolMethods))
    
    if not ms:
        return AmisRet.error("方法不存在")
    print(ms[0].run(data["input_text"]))
    return AmisRet.ok({"output_text":ms[0].run(data["input_text"])})

