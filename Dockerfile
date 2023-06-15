FROM python:3.10

ENV LINK="${LINK}"

COPY requirements.txt .
COPY main.py .

RUN pip install -r requirements.txt

CMD ["python", "./main.py", "$LINK"]

