import socket
from fastapi import FastAPI
from nacos import NacosClient
# from dotenv import load_dotenv
import os

app = FastAPI()


nacos_ip:str = os.getenv("SERVER-ADDR","10.91.121.21")
nacos_group:str = os.getenv("GROUP","dev")
nacos_namespace:str = os.getenv("NAMESPACE","84a19263-d7f5-40e5-b5cc-7e83264237ec")

# 连接到 Nacos 服务器
client = NacosClient(server_addresses=nacos_ip, namespace= nacos_namespace)

def get_container_ip():
    return socket.gethostbyname(socket.gethostname())

# 注册 FastAPI 服务到 Nacos
@app.on_event("startup")
async def register_service():

    service_name = "fastapi-service"
    ip = get_container_ip()
    port = 8000  # FastAPI 服务端口
    group= nacos_group
    client.add_naming_instance(service_name=service_name,ip= ip,port=port, group_name=group)

# 注销 FastAPI 服务
@app.on_event("shutdown")
async def unregister_service():
    service_name = "fastapi-service"
    ip = "fastapi_host"
    port = 8000  # FastAPI 服务端口
    client.remove_naming_instance(service_name, ip, port)
