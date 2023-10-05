# Use an official Python runtime as the parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy only the necessary files from the frontend directory
COPY frontend/app.py .
COPY frontend/requirements.txt .

# Install required packages
RUN pip install -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py"]
