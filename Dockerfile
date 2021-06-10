# Pull base image
FROM python:3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /code/

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /code/
RUN pip install -r /code/requirements.txt

COPY . /code/

EXPOSE 8000