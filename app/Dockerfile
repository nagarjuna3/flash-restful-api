FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
COPY . /app

RUN pip install -r requirements.txt
# RUN apt update -y ; apt install vim -y 

COPY app.py /app
CMD python app.py