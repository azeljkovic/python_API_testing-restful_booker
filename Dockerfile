FROM python:latest

RUN mkdir /home/python_API_testing
WORKDIR /home/python_API_testing
COPY . .

RUN pip install -r requirements.txt
