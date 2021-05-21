FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Copy requirements to docker container
COPY requirements.txt .

# Install requirements on docker container
RUN pip3 install -r requirements.txt

# Expose port 3000 of container
EXPOSE 3000

COPY ./app /app