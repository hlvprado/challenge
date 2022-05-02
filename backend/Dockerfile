FROM python

WORKDIR /

COPY requirements.txt ./

COPY . .

EXPOSE 5000

RUN apt-get update && \
    pip install -r requirements.txt

RUN export FLASK_APP=helder_backend && export FLASK_ENV=development

CMD python wsgi.py runserver 0.0.0.0:5000