from typing import Any
from fastapi.responses import JSONResponse
from openai import BaseModel

class AmisRet(BaseModel):
    status: int
    msg: str
    data: Any



    @staticmethod
    def ok(data):
        return AmisRet(status=0, msg="", data=data)

    @staticmethod
    def error(msg):
        return AmisRet(status=1, msg=msg, data="")