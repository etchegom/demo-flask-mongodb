FROM python:3.7-alpine

RUN apk add --no-cache --update git bash

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.5.0/wait /wait
RUN chmod +x /wait

ADD ./requirements.txt /tmp/
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt

WORKDIR /code
ADD ./entrypoint.sh /code/
ADD ./src/ /code/

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]
CMD ["server"]
