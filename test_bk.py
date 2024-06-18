from typing import List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # 实际项目中应配置允许的域名，例如 ["http://localhost", "https://example.com"]
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # 允许的 HTTP 方法
    allow_headers=["*"],  # 允许的请求头，* 表示允许所有请求头
)


users = []


# 模拟数据库存储用户信息
class User(BaseModel):
    id: int = len(users)
    name: str


# 获取用户列表
@app.get("/users/", response_model=List[User])
async def get_users():
    return users


# 添加新用户
@app.post("/users/", response_model=User)
async def create_user(user: User):
    user.id = len(users) + 1
    users.append(user)
    return user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
