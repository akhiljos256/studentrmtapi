# Student API Service

This is a simple RESTful API built with Flask, providing basic CRUD operations for managing a Student entity with attributes such as ID, Name, Grade, and Email.

## Features

- **GET /students**: Retrieve a list of all students.
- **GET /students/{id}**: Retrieve details of a student by ID.
- **POST /students**: Add a new student.
- **PUT /students/{id}**: Update an existing student by ID.
- **DELETE /students/{id}**: Delete a student by ID.

## Prerequisites

- Python 3.8+
- pip


## Project Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/ramymohamed10/rest-api-demo <---sample repository--->
    ```
2. Create another folder for our project.
 
3. Create app.py file, requirements.txt file, .gitignore file, test-api.http corresponding to our project refering the sample repository which was cloned.

4. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```


## Running the Service Locally

1. **Start the Flask server**:

    ```bash
    python app.py
    ```

2. **Access the API**:

    By default, the API will run on `http://localhost:8000`.
## API Endpoints

- **GET /students** - Retrieve all students
- **GET /students/{id}** - Retrieve a specific student by ID
- **POST /students** - Add a new student (requires JSON body with `name`, `grade`, and `email`)
- **PUT /students/{id}** - Update an existing student by ID (accepts JSON body to update fields)
- **DELETE /students/{id}** - Delete a student by ID

## Sample `test-api.http` File

Use test-api.http to test the REST API using the REST Client extension in Visual Studio Code.

## Create a repository in GitHub and clone the folder to the repository

## Deploy the API to Azure Web App Service.





