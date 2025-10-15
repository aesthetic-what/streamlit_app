from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router
from db import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("db start")
    await init_db()
    yield
    print("db close")


app = FastAPI(lifespan=lifespan)
app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],  # URL Streamlit
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def start():
    return {"status": "ok"}