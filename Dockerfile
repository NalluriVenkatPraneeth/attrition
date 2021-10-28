FROM python:3.8.12-alpine
WORKDIR /project
ADD . /project
WORKDIR /project
RUN pip install -r requirements.txt
CMD ["python","main.py"]