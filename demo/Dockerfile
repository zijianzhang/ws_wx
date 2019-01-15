FROM python:3.6.5

MAINTAINER Zhangzi Zijian <342088102@qq.com>


WORKDIR /app/
COPY r.txt /app/
RUN pip install -r r.txt
COPY . /app/


ENV FLASK_APP=demo.py 
EXPOSE 5000
CMD ["uwsgi","--ini","uwsgi.ini"]
