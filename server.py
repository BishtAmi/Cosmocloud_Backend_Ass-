from fastapi import FastAPI
from routes.students_route import student
app = FastAPI()

app.include_router(student)

@app.get("/")
async def root():
    return {"message": "/docs for more"}


    