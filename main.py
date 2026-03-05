from fastapi import FastAPI, Form, Request
from src.routes.tasks import router as tasks_router
from src.routes.auth import router as auth_router
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(title="Todo APP")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.post("/login")
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/task/new", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse("new_task.html", {"request": request})

app.include_router(tasks_router)
app.include_router(auth_router)
