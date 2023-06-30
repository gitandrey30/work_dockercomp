FROM python:3.10-alpine

WORKDIR ./

COPY reqirements.txt .

RUN pip install -r reqirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]