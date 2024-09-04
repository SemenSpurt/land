from base import Base

from sqlalchemy import Column, Integer, String


class Docs(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    mail = Column(String)
    phon = Column(String)
    work = Column(String) 
    nite = Column(String)