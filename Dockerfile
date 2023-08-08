FROM python:latest
WORKDIR /ddns-updater
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "updater.py"]
