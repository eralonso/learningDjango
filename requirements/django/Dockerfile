FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update -y \
		&& apt-get upgrade -y \
		&& apt-get install -y \
			vim \
			bash

WORKDIR /srv/ft_transcendence_backend/www

COPY requirements.txt /srv/ft_transcendence_backend/www/

RUN pip install -r requirements.txt

COPY .vimrc /root/.vimrc

COPY srcs/ /srv/ft_transcendence_backend/www/

ENTRYPOINT [ "/bin/tail", "-f" ]
