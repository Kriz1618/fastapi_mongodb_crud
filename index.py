#  start with uvicorn index:app --reload
from fastapi import FastAPI
from routes.student import student_router
from fastapi.middleware.cors  import CORSMiddleware

client_apps = ['http://localhost:3000'] #The react server

#create app
app = FastAPI()
#Register apps wth CORS  middleware to allow resources sharing between different domains/origins
app.add_middleware(
  CORSMiddleware,
  allow_origins = client_apps,
  allow_credentials = True,
  allow_methods = ['*'],
  allow_headers = ['*']
)
#register routes
app.include_router(student_router)