FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r reqirement.txt
