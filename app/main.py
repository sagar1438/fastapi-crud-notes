from fastapi import FastAPI
from app.api import root, notes
from app.db import metadata, engine, database

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(root.router,tags=["root"])
app.include_router(notes.router, prefix="/notes",tags=["Notes"])