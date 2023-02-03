# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# save token in /root/.cache/huggingface/token
COPY token  /root/.cache/huggingface/

# Copy the requirements.txt file to the container
COPY requirements.txt ./

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the flask server code to the container
COPY app.py ./

# Specify the command to run the Flask server
CMD ["python", "app.py"]

# Expose port 5000 to allow external access to the Flask server
EXPOSE 8088

