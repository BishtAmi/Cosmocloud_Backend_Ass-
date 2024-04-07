from fastapi import APIRouter
from models.student_model import Student
from schemas.student_schema import  students_serializer
from bson import ObjectId
from config.db import collection
from typing import Optional
from fastapi import Query
from fastapi import HTTPException

student = APIRouter()


# post request  /student -> create students

@student.post("/students", status_code=201)
async def create_student(student: Student):
    student_dict = student.dict()
    student_dict["address"] = student.address.dict()
    res = collection.insert_one(student_dict)
    inserted_id = str(res.inserted_id)
    return { "id": inserted_id }



# get request /students -> get list of all students

@student.get("/students",status_code=200)
async def get_all_students(country: Optional[str] = Query(None, description="To apply filter of country."),
                           min_age: Optional[int] = Query(None, description="Only records which have age greater than or equal to the provided age should be present in the result.")):
    query = {}
    if country:
        query["address.country"] = country
    if min_age is not None:
        query["age"] = {"$gte": min_age}
    # print("country",query.get("address.country", "None"))
    # print("age",query.get("age", "None"))
    students = students_serializer(collection.find(query))
    data = [{"name": student["name"], "age": student["age"]} for student in students]
    return {"data": data }


# get request /student/{id} get student by there id

@student.get("/students/{id}",status_code=200)
async def get_student_by_id(id: str):
    existing_student = collection.find_one({"_id": ObjectId(id)})
    if existing_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    student = students_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "Ok", "data": student}
    

# patch request /student/{id} update student by there id

@student.patch("/students/{id}",status_code=204)
async def update_student_by_id(id: str, student_data: dict):
    # Fetch the existing student from the database
    existing_student = collection.find_one({"_id": ObjectId(id)})
    if existing_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Update the student data with the provided fields
    for key, value in student_data.items():
        if key in existing_student:
            existing_student[key] = value

    # Update the student in the database
    collection.update_one({"_id": ObjectId(id)}, {"$set": existing_student})
    

# delete request /student/{id} delete student with given id

@student.delete("/students/{id}",status_code=200)
async def delete_student_by_id(id: str):
    existing_student = collection.find_one({"_id": ObjectId(id)})
    if existing_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    collection.delete_one({"_id": ObjectId(id)})
    return { "data": "record delete"}