FROM python:3.10.12-alpine3.18

WORKDIR /usr/src/app

ENV VAR=$LINK

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py main.py

CMD ["python3", "./main.py", "$VAR"]

