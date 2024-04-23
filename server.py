from fastapi import FastAPI
from routes.students_route import student
# from middleware.ratelimiter import rate_limit_middleware

# import aioredis
app = FastAPI()

app.include_router(student)


@app.get("/")
async def root():
    return {"message": "/docs for more"}
