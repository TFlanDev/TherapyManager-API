
# Therapy Manager API

A RESTful API for managing therapists and patients, built with FastAPI and containerized with Docker.

## Technology Stack

* **Backend**: FastAPI
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **Containerization**: Docker & Docker Compose

***

## Project Structure
```
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app object and endpoints
│   ├── crud.py          # Database logic and operations
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic data validation schemas
│   └── database.py      # DB connection and session management
├── .env                 # Environment variables
├── Dockerfile           # Instructions to build the API image
└── docker-compose.yml   # Service orchestration for the API & DB
```

## Getting Started


### Prerequisites

* Docker & Docker Compose
* Python 3.12+ (for local development)

### Running with Docker 


1.  **Clone the repository:**
    ```bash
    git clone https://github.com/TFlanDev/TherapyManager-API
    cd TherapyMgr
    ```

2.  **Create Environment File:**
    Create a file named `.env` in the project root and add the following, replacing the values as needed.
    ```env
    POSTGRES_USER=myuser
    POSTGRES_PASSWORD=mypassword
    POSTGRES_DB=mydatabase
    ```

3.  **Build and Run:**
    ```bash
    docker-compose up --build
    ```

Once the application is running, you can access the API documentation (Swagger UI) to test all the endpoints: `http://localhost:8000/docs`

## API Endpoints

* **Therapists**: `POST /therapist/`, `GET /therapists/`, `GET /therapist/{id}/`
* **Patients**: `POST /patient/`, `GET /patients/`, `GET /patient/{id}/`, `PUT /patient/{id}/`

***