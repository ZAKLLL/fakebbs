import config.swagger as swagger
from webUI import templateCfg

# 创建 FastAPI 实例
app=templateCfg.app
app.include_router(swagger.router)
# 自动注册路由
import importlib
import os
import base.methodView
# 动态导入所有API路由
api_dir = "api"
for filename in os.listdir(api_dir):
    if filename.endswith(".py") and not filename.startswith("__"):
        module_name = f"{api_dir}.{filename[:-3]}"
        module = importlib.import_module(module_name)
        if hasattr(module, "router"):
            app.include_router(getattr(module, "router"))

app.include_router(base.methodView.router)

@app.get("/hello")
async def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    # 启动FastAPI服务
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



# uvicorn main:app --host 0.0.0.0 --port 8000 --reload 