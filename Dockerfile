# Using Python official image
FROM python:3.7-slim

# Optional, but a good practice
# LABEL MAINTAINER = kingbigw

# Copying the project from our OS to the specified location (in container) 
WORKDIR /
COPY ./app/requirements.txt .
RUN python -m pip install -r requirements.txt

COPY ./app /usr/src/app

# Run the requirements
WORKDIR /usr/src/app
#RUN python -m pip install -r requirements.txt

EXPOSE 8000

# Run the application
#CMD ["python", "app.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]

