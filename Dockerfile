FROM python:3.10-slim

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt

COPY . /app/
WORKDIR /app

RUN chown nobody:nogroup -R /app

EXPOSE 8000
USER nobody

CMD uvicorn --host 0.0.0.0 --port 8000 main:app
