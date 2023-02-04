FROM python:3.9-buster
RUN apt update && apt install -y build-essential 
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

EXPOSE 5004

CMD ["/usr/local/bin/flask", "run", "--host=0.0.0.0", "--port=5004"]