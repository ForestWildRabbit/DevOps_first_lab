FROM python:3.10

ENV LINK="${LINK}"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["python", "./main.py", "$LINK"]

