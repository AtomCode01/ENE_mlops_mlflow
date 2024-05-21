FROM python:3.8-slim-buster

# Update package lists and install awscli
RUN apt-get update -y && apt-get install -y awscli

# Set the working directory
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install the required Python packages
RUN pip install -r requirements.txt

# Define the command to run the application
CMD ["python3", "app.py"]


# FROM python:3.8-slim-buster

# RUN apt update -y && apt install awscli -y
# WORKDIR /app

# COPY ./app
# RUN pip install -r requirements.txt

# CMD ["python3", "app.py"]