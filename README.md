# Cosmocloud Backend Assignment 
## Library Management System

### Tech Stack
- Language: Python
- Framework: FastAPI
- Database: MongoDB (M0 Free Cluster of MongoDB Atlas)
- Deploy: Render

### API Endpoints 
Deployed URL: [https://cosmocloud-backend-assesment.onrender.com/](https://cosmocloud-backend-assesment.onrender.com/)

#### Create a Student
- **Method**: POST
- **Endpoint**: `/students`
- **Request Body**:
  ```json
  {
    "name": "string",
    "age": 0,
    "address": {
      "city": "string",
      "country": "string"
    }
  }
  ```
- **Response Status Code**: 201
- **Response Body**:
  ```json
  {
    "id": "string"
  }
  ```

#### Get Students
- **Method**: GET
- **Endpoint**: `/students`
- **Parameters**:
  - `country`: To apply a filter by country. Optional.
  - `age`: Filters records with an age greater than or equal to the provided age. Optional.
- **Response Status Code**: 200
- **Response Body**:
  ```json
  {
    "data": [
      {
        "name": "string",
        "age": 0
      }
    ]
  }
  ```

#### Get Specific Student
- **Method**: GET
- **Endpoint**: `/students/{id}`
- **Parameters**:
  - `id`: ID of the student (required)
- **Response Status Code**: 200
- **Response Body**:
  ```json
  {
    "name": "string",
    "age": 0,
    "address": {
      "city": "string",
      "country": "string"
    }
  }
  ```

#### Update Specific Student
- **Method**: PATCH
- **Endpoint**: `/students/{id}`
- **Parameters**:
  - `id`: ID of the student (required)
- **Request Body**:
  ```json
  {
    "name": "string",
    "age": 0,
    "address": {
      "city": "string",
      "country": "string"
    }
  }
  ```
- **Response Status Code**: 204 (No Content)

#### Delete Specific Student
- **Method**: DELETE
- **Endpoint**: `/students/{id}`
- **Parameters**:
  - `id`: ID of the student (required)
- **Response Status Code**: 200
- **Response Body**:
  ```json
  {
    "data deleted"
  }
  ```
