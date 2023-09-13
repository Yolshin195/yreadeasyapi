from fastapi import Depends
from sqlalchemy.orm import Session
import db


class BaseService:
    def __init__(self,
                 session: Session = Depends(db.get_db)):
        self.session: Session = session

        self.__init__post__()

    def __init__post__(self):
        pass
