import base, mod, rout

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


mod.Base.metadata.create_all(bind=base.engine)

app = FastAPI()

origins = [
    "localhost",
    "http://0.0.0.0",
    "datatrap.sysbiomed.ru",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rout.router)
app.mount("/", StaticFiles(directory="./", html = True), name="./")

