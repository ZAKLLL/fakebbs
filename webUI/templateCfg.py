

import json
import os

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import contextvars

# 创建 FastAPI 实例
app=FastAPI()

# 设置静态文件服务
app.mount("/static", StaticFiles(directory="webUI"), name="static")

templates = Jinja2Templates(directory="webUI")

__all__ = ["templates","app"]

# 全局request
current_request = contextvars.ContextVar('current_request')

@app.middleware("http")
async def add_request_to_context(request: Request, call_next):
    # 在调用下一个中间件或路由处理函数之前，将请求对象设置到上下文中
    token = current_request.set(request)
    try:
        response = await call_next(request)
    finally:
        # 在请求处理完成后，从上下文中移除请求对象
        current_request.reset(token)
    return response

# webui 渲染
def render(amisJson:str):
    request=current_request.get()
    # 当前请求为http请求,从全局域中获取request
    return templates.TemplateResponse("index.html", {"request": request, "AMIS_JSON": json.dumps(amisJson)})

async def getLogic(func):
    request=current_request.get()

async def postLogic(func):
    request=current_request.get()
    data = await request.json()
    return JSONResponse(content=func(data))


