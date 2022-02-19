FROM python:3.10

RUN apt update && apt install pip -y

ADD requirements.txt /

RUN pip install -r /requirements.txt

WORKDIR /anime_site_2

ADD anime_site_2 /anime_site_2/
