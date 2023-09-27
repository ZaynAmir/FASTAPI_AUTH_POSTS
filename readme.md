# FastAPI App with MySQL Database

This is a FastAPI application with a MySQL database. Follow the instructions below to set up and run the application.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.10.12
- pip (Python package manager)

## Installation

1. Clone this repository to your local machine:

```bash
git clone <repository_url>
cd FastApi_MVC_Assignment
```

## Start Server 

2. create virtualenv and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

pip install -r requirements.txt


```

3. Database should be created before running the project in MySQL server locally
Open the database.py file and update the DATABASE_URL with your MySQL database connection details. For example:
```bash
DATABASE_URL=mysql://username:password@localhost/database_name
```


4. Run the server using this command:
```bash
uvicorn main:app --reload

```


5. to view swagger docs go to this url:
```bash
localhost:8000/docs

```