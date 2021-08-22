FROM python:3.8
  
RUN mkdir /django
WORKDIR /django

COPY requirements.txt /django/

RUN pip install --no-compile --no-cache-dir --upgrade pip && \
    pip install --no-compile --no-cache-dir -r requirements.txt
