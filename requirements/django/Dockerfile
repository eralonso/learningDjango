FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update \
		&& apk add --no-cache \
			gcc \
			musl-dev \
			postgresql-dev \
			vim \
			bash \
			npm

WORKDIR /srv/ft_transcendence_backend/www

COPY requirements.txt /srv/ft_transcendence_backend/www/

RUN pip install -r requirements.txt

#COPY src /srv/ft_transcendence_backend/www/src
COPY src/server.sh /srv/ft_transcendence_backend/www/server.sh

RUN chmod +x /srv/ft_transcendence_backend/www/server.sh

#RUN npm i ws

#ENTRYPOINT [ "/bin/tail", "-f" ]
ENTRYPOINT [ "/srv/ft_transcendence_backend/www/server.sh" ]
