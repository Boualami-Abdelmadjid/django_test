FROM python:3.10-alpine

# unbUffering output
ENV PYTHONUNBUFFERED 1

# creating workdir
RUN mkdir /code
WORKDIR /code

# dependencies and requirements
ADD requirements.txt /code/
RUN  pip install --no-cache-dir -r requirements.txt

ADD . /code/

RUN python manage.py collectstatic