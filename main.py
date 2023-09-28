from fastapi import FastAPI
from routers import filter_router

app = FastAPI()

app.include_router(filter_router.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

