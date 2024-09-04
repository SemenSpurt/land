import base, mod

from typing import Annotated

from fastapi import APIRouter, Depends, Request, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from pydantic import BaseModel

from sqlalchemy.orm import Session


class DocBase(BaseModel):

    name: str
    mail: str
    phon: str
    work: str
    nite: str


router = APIRouter()
db_dep = Annotated[Session, Depends(base.get_db)]
templs = Jinja2Templates(directory="./")


@router.get("/")
async def index(request: Request):
    return templs.TemplateResponse("index.html", {"request": request})


@router.post("/new")
async def new(
    request: Request,
    # doc: DocBase,
    db: db_dep,
    name: str = Form(...),
    mail: str = Form(...),
    phon: str = Form(...),
    work: str = Form(...),
    nite: str = Form(...),
):
        
    db_doc = mod.Docs(
        name=name,
        mail=mail,
        phon=phon,
        work=work,
        nite=nite,
    )

    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)

    redirect_url = request.url_for('index')    
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)

# @router.post("/new")
# async def new(
#     doc: DocBase,
#     db: db_dep,
# ):
#     db_doc = mod.Docs(
#         name=doc.name,
#         mail=doc.mail,
#         phon=doc.phon,
#         work=doc.work,
#         nite=doc.nite,
#     )
#     db.add(db_doc)
#     db.commit()
#     db.refresh(db_doc)