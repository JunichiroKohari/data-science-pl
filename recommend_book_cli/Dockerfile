FROM --platform=linux/amd64 library/python:3.11
COPY requirements.txt requirements.lock requirements-dev.txt ./
RUN pip install -r requirements.txt -c requirements.lock