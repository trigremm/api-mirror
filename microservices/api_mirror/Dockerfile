FROM python:3.9-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add python3-dev 

COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 80
CMD python api_mirror/manage.py migrate && python api_mirror/manage.py runserver 0.0.0.0:80 
