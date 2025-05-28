# Django DRF Project with Celery and Docker

## Description
This project is built with Django using Django REST Framework (DRF), Celery, and Redis for asynchronous task processing and periodic tasks (via celery-beat). PostgreSQL is used as the database. The project runs inside Docker containers orchestrated by Docker Compose.

---

## Technologies
- Django
- Django REST Framework (DRF)
- Redis
- Celery
- Celery-beat
- PostgreSQL
- Docker & Docker Compose
- unittest (Django)
- isort, pylint (for formatting and linting)

---

## How to run

1. Clone the repository and navigate to the project root.

2. Create a `.env` file with the following environment variables:


**SECRET\_KEY**=your\_secret\_key
**POSTGRES\_DB**=your\_db\_name
**POSTGRES\_USER**=your\_db\_user
**POSTGRES\_PASSWORD**=your\_db\_password

````

3. Start the Docker containers:
```bash
docker-compose up --build
````

4. Migrations, static files collection, and server startup are run automatically.

---

## Usage

* The server is available at `http://localhost:8000/`

* Periodic tasks (celery-beat) can be managed via the Django Admin interface.

---

## REST API Endpoints

Available GET endpoints:

* `/get_users/` — retrieve user information
* `/get_addresses/` — retrieve addresses information
* `/get_credit_cards/` — retrieve credit card information

---

## Testing

Run Django unit tests inside the container:

```bash
docker-compose exec api python tech_task/manage.py test tests.test_tasks
```

---

## Linting and Formatting

* `isort` — for import sorting
* `pylint` — for code style and error checking

---

## Notes

* Celery and celery-beat require environment variables to connect properly to the database and Redis, which are set in docker-compose.
* Redis is used as the message broker for Celery.

---

