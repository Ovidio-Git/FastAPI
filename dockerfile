FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
# directory for work
WORKDIR /app
# Copy requirements to docker container
COPY requirements.txt requirements.txt

# Install requirements on docker container
RUN pip3 install -r requirements.txt

# Expose port 3000 of container
EXPOSE 3000

COPY . .
CMD ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "3000"]