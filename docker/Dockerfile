FROM python:3.8.8

RUN mkdir /app
WORKDIR /app

COPY ./* /app/

RUN pip install -r requirements.txt

CMD /bin/sh