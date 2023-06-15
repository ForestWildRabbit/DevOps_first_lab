FROM python

ENV LINK="${LINK}"

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py main.py

CMD ["python", "./main.py", "$LINK"]

