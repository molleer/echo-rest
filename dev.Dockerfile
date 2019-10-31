FROM python:3.7

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED 0

COPY . .

EXPOSE 5000

CMD ["python","-u","app/main.py"]
