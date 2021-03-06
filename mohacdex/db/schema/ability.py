from sqlalchemy import Column, Integer, Unicode
from ..base import Base 

class Ability(Base):
    __tablename__ = "abilities"
     
    identifier = Column(Unicode, primary_key=True)
    name = Column(Unicode, nullable=False)
    flavor_text = Column(Unicode, nullable=False)
