FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get install -y chromium xvfb chromium-driver 

COPY . /app
WORKDIR /app

RUN pip install -U python-dotenv PyVirtualDisplay SpeechRecognition pyttsx3
RUN pip install -e pyChatGPT

# CMD ["python", "main.py"]
CMD ["bash"]
