from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import  MongoClient
app = FastAPI()
conn = MongoClient("mongodb+srv://tomararman4:ram123@cluster0.u3uzo.mongodb.net/") # type: ignore
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # docs = conn.pynotes.note.find_one({})
    # print(docs)
    return templates.TemplateResponse(
        request=request, name="item.html"
    )