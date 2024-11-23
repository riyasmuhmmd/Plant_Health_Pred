FROM python:3.9-slim-buster
WORKDIR /service
COPY reqirement.txt
COPY . ./
RUN pip install -r reqirement.txt
ENTRYPOINT ["python3", "app.py"]