FROM python:3

EXPOSE 8000

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

CMD [ "python", "./project_quorum/manage.py", "runserver", "0.0.0.0:8000" ]
