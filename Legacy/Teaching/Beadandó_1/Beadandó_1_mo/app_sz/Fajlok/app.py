from fastapi import FastAPI
from .utvonalak import utvonal

app = FastAPI()

app.include_router(utvonal, tags=["Kurzusok"])


@app.get("/", tags=["Root"])
async def read_root():
    return {"üzenet": "Üdvözöllek a Szakácsképző Intézmény FastAPI alkalmazásában!"}

