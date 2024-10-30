from fastapi import APIRouter, Request


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

api_data = {
    "input_text":"",
    "output_text":""
}
base_amis_json = {
    "type": "page",
    "title": "demo",
    "body": {
        "type": "form",
        "api": {
            "method": "post",
            "url": "/tools/doProcess",
            "data": {}
        },
        "body":{} 
        }
    }
__all__=["base_amis_json"]


def generate_amis_json(module):
    import inspect
    # module.
    # 获取函数签名
    mehthodSign=inspect.signature(module.p_f)
    for name,param in mehthodSign.parameters.items():
        print(name,param)
        view_body.append({
            "type": "input-text",
            "label": f"情输入{name}",
            "name": name
        })
    base_amis_json["body"]=view_body
    return base_amis_json
    


router = APIRouter()

@router.post("/c/doProcess")
async def doProcess(request:Request):
    # 这里实现你的转换逻辑
    data = await request.json()
    