from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from src.config.db import db

templates = Jinja2Templates(directory='templates')

router = APIRouter()


def get_loggedin_user(request: Request):
  token = request.cookies.get('user_session')
  if token:
     result = db.auth.get_user(token)
     if result:
       return result.user
     

@router.get('/dashboard')
def show_dashboard(request: Request):
    if get_loggedin_user(request):
       return templates.TemplateResponse("dashboard.html", {"request": request})
    

@router.get("/task/new")
def new_task(request: Request):
   if get_loggedin_user(request):
      return templates.TemplateResponse("new_task.html", {"request": request})
   
@router.post("/task/new")
def new_task(request: Request, taskTitle = Form(...), description = Form(...), status = Form(...)):
   user = get_loggedin_user(request)
   if user:
      user_id = user.id
      result = db.table('tasks').insert({
         'title': taskTitle,
         'description': description,
         'status': status,
         'user_id': user_id
      }).execute()

      return templates.TemplateResponse('task_success.html', {"request": request})
   
   
