FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD sh -c "python manage.py parsing -o data/data.json -n data/new.json && \
           python manage.py loaddata data/new.json && \
           python manage.py runserver 0.0.0.0:8000"