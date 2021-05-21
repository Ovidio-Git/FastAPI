#st
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip

EXPOSE 3000

COPY ./app /app