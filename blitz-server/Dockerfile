FROM python:3.10.1
RUN apt-get update -qq && \
apt-get install -y --no-install-recommends \
libmpc-dev \
libgmp3-dev \
libmpfr-dev
WORKDIR /api
COPY requirements.txt /api/
RUN pip install -r requirements.txt
RUN pip install channels-redis
RUN pip install psycopg2-binary
COPY . /api/
CMD [ "python", "blitz/manage.py", "runserver",  "0.0.0.0:8000" ]