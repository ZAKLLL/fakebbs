from fastapi import APIRouter, Request
import importlib
import inspect

from base.amisRet import AmisRet

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


base_amis_json = {
    "type": "page",
    "title": "demo",
    "body": {
        "type": "form",
        "api": {
            "method": "post",
            "url": "/methodExec",
            "data": {}
        },
        "body":{} 
        }
    }
__all__=["base_amis_json"]


def generate_amis_json(module):

 # 获取该module 下的所有非__函数
    targetFuncName = [func for func in dir(module) if callable(getattr(module, func)) and not func.startswith("__")][0]
    
    # 获取函数签名
    methodSign = inspect.signature(getattr(module, targetFuncName))
    model_name = module.__name__
    api_body = {"moduleName": model_name ,"targetFuncName":targetFuncName}
    tmp_view_body = []
    for name, param in methodSign.parameters.items():
        tmp_view_body.append({
            "type": "input-text",
            "label": f"{name}",
            "placeholder": f"请输入参数: {name}",
            "name": name
        })
        api_body[name]=f"${{{name}}}"
    tmp_view_body.extend(view_body)
    base_amis_json["body"]["body"]=tmp_view_body
    base_amis_json["body"]["api"]["data"]=api_body
    base_amis_json["title"]=module.view_desc
    
    return base_amis_json
    


router = APIRouter()

@router.post("/methodExec")
async def methodExec(request:Request):
    # 这里实现你的转换逻辑
    body = await request.json()
    moduleName=body["moduleName"]
    methodName=body["targetFuncName"]
    module=importlib.import_module(moduleName)

    targetFunc=getattr(module, methodName)
    methodSign = inspect.signature(getattr(module, methodName))
    reqParams=[body[paramName] for paramName, _ in methodSign.parameters.items()]
    ret=targetFunc(*reqParams)
    return AmisRet.ok({"output_text":ret})