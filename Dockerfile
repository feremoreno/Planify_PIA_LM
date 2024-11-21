FROM python:3.12-slim

WORKDIR /app

COPY . /app/

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && apt-get clean

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -v -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
