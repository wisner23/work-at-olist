FROM python:3

COPY . /work-at-olist
WORKDIR /work-at-olist

RUN pip install -r requirements.txt
RUN pip install gunicorn==18.0.0
RUN chmod a+x /work-at-olist/start.sh

ENTRYPOINT ["/work-at-olist/start.sh"]
