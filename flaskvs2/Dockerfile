FROM tiangolo/uwsgi-nginx-flask:python3.9
RUN apt-get update && apt-get install -y gcc unixodbc-dev
#RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY . /app
COPY ./requirements.txt /var/www/requirements.txt
#RUN pip install pyodbc
RUN pip install -r /var/www/requirements.txt