FROM python:3.7.0-alpine
WORKDIR /project
ADD . /project
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python","main.py"]