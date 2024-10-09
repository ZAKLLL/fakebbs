from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from webUI import templateCfg
router = APIRouter()


amisJson = {
    "type": "page",
    "title": "fuckTest",
    "body": {
        "type": "form",
        "api": "/fuckF2",
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

@router.get("/f2", response_class=HTMLResponse,description="f2页面")
async def read_index():
    return templateCfg.render(amisJson)
    


@router.post("/fuckF2")
async def convert_text():
    return await templateCfg.postLogic(
        func= lambda data: {"output_text": data['input_text'].upper()+"ffffffffffffffffffffffffffffu"}
    )
    

