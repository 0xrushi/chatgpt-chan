FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get install -y chromium xvfb chromium-driver  git curl wget libportaudio2 libasound-dev libdbus-glib-1-2 gcc libstdc++6

COPY . /app
WORKDIR /app

RUN pip install -U rich playwright python-dotenv PyVirtualDisplay SpeechRecognition pyttsx3 azure-cognitiveservices-speech sounddevice soundfile
# RUN pip install -e pyChatGPT
RUN pip install --force-reinstall 'cffi>=1.15.1' 
RUN pip install git+https://github.com/mmabrouk/chatgpt-wrapper
RUN playwright install firefox

ENV SPEECH_KEY=<aws_speech_key>
ENV SPEECH_REGION=<azure_region>

# CMD ["python", "main.py"]
CMD ["bash"]
