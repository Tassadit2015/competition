import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy.orm import relationship


from sqlalchemy import create_engine

Base = declarative_base()



class Category(Base):

    __tablename__ = 'category'

    name = Column(String(8), nullable = False)
    id = Column (Integer, primary_key = True)


class Participant(Base):
    __tablename__ = 'participant'

    name = Column(String(8), nullable = False)
    id = Column(Integer, primary_key = True)
    age = Column(Integer, nullable = False)
    category_id = Column(ForeignKey('category.id'))
    category = relationship(Category)




engine = create_engine('sqlite:///competitionround2.db')
Base.metadata.create_all(engine)
