
FROM python:3.10
ENV PYTHONUNBUFFERED=1

# set work directory
WORKDIR /asianmusic

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

