FROM python:3.10-alpine


ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /usr/src

RUN apk update && \
    apk add --no-cache gcc musl-dev postgresql-dev

COPY ./requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "sleep 5 && python tech_task/manage.py migrate && python tech_task/manage.py runserver 0.0.0.0:8000"]
