import importlib
import json
import os

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse

from api import tools_methods
from base.amisRet import AmisRet
from webUI import templateCfg

router = APIRouter()


base_index_amis_json = {
  "type": "page",
  "aside": [
    {
      "type": "page",
      "data": {
        "nav": [
          {
            "label": "Nav 1",
            "to": "/docs/index",
            "icon": "fa fa-user"
          },
        ],
      },
      "body": {
        "type": "nav",
        "stacked": "true",
        "source": "/index/views",
        "searchable": 'true',
        "searchConfig": {
          "matchFunc": "return link.label.indexOf(keyword)!=-1;"
        },
        "onEvent": {
          "click": {
            "actions": [
              {
                "actionType": "toast",
                "args": {
                  "msg": "${event.data.item.label}"
                }
              }
              
            ]
          }
       } 
      },
      
    }
  ],
  "body": '{}'
}

# # 动态导入所有API路由
api_dir = "api"
apiList=[]
for filename in os.listdir(api_dir):
    if filename.endswith(".py") and filename.startswith("view_") and not filename.startswith("__"):
        module_name = f"{api_dir}.{filename[:-3]}"
        module = importlib.import_module(module_name)
        if filename=='index.py':
            continue
        
        if hasattr(module, "router"):
            apiList.append({"value":filename,"label":module.view_desc,"to":"/index/"+filename,"view_sort":module.view_sort})
apiList.sort(key=lambda x:x["view_sort"])

@router.get("/", response_class=HTMLResponse,description="")
async def read_index():
    viewJson=dict(base_index_amis_json)
    viewJson['body']="Hello Bitch!"
    return templateCfg.render(viewJson)




@router.get("/index/views")
async def listToolMethods():
    # 列出所有的api 下的router 
    return AmisRet.ok(apiList)
    


@router.get("/index/{filename}", response_class=HTMLResponse,description="")
async def read_index(filename):
    print(filename)
    module_name = f"{api_dir}.{filename[:-3]}"
    module = importlib.import_module(module_name)
    viewJson=dict(base_index_amis_json)
    viewJson['body']=module.amis_json
    return templateCfg.render(viewJson)
    

