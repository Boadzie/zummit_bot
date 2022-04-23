FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /app

EXPOSE 8000:8000


# command to run on container start 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]