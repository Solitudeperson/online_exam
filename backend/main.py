from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 解决跨域（前后端分离必备）

app = FastAPI(title="Online Exam API", version="1.0")

# 配置跨域（允许前端Vue访问）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Vue默认运行端口
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 测试接口
@app.get("/test")
async def hello():
    return {"message": "FastAPI 后端启动成功！"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)  # 热重载模式