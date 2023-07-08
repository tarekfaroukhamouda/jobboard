from fastapi import FastAPI
from core.config import settings
from db.session import  engine
from db.base import Base


def create_tables():
    Base.metadata.create_all(bind=engine)

def startapplication():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    return app

app=startapplication()
@app.get("/")
def hello_api():
    return {"details":settings.PROJECT_NAME}


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
