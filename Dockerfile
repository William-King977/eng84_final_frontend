# Using Python official image
FROM python:3.7-slim

# Optional, but a good practice
# LABEL MAINTAINER = kingbigw

# Copying the project from our OS to the specified location (in container) 
COPY . /usr/src/app

# Run the requirements
WORKDIR /usr/src/app
RUN python -m pip install -r requirements.txt

# Make migrations, then run the application
CMD ["python", "app.py"]
