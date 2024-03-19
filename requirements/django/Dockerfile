FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update -y \
		&& apt-get upgrade -y \
		&& apt-get install -y \
			vim \
			bash \
			npm

WORKDIR /srv/ft_transcendence_backend/www

COPY requirements.txt /srv/ft_transcendence_backend/www/

RUN pip install -r requirements.txt

#COPY src /srv/ft_transcendence_backend/www/src
COPY src/server.sh /srv/ft_transcendence_backend/www/server.sh

RUN chmod +x /srv/ft_transcendence_backend/www/server.sh

RUN npm i ws

#ENTRYPOINT [ "/bin/tail", "-f" ]
ENTRYPOINT [ "/srv/ft_transcendence_backend/www/server.sh" ]
