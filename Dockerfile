FROM python:3.11

WORKDIR /autowillow

COPY . /autowillow 

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]

