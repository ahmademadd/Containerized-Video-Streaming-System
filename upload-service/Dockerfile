FROM python:3

WORKDIR /app

COPY requirements.txt /app

RUN mkdir videos

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
