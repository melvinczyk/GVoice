FROM python:3.13-alpine
LABEL authors="nicholasburczyk"

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

ENTRYPOINT ["python", "-main.py", "--port", "8000"]