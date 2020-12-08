FROM python:3.7-alpine

ARG AWS_ACCESS_KEY
ARG AWS_SECRET_KEY
ARG AWS_REGION

COPY . /app

WORKDIR /app

RUN chmod +x /app/build.sh && \
     sh /app/build.sh

RUN  pip install -r /app/requirements.txt

CMD [ "python", "handler.py" ]