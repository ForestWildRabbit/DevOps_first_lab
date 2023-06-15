FROM python:3.10

COPY . .

ENV LINK="${LINK}"

RUN pip install -r requirements.txt

CMD ["python", "./main.py", "$LINK"]

