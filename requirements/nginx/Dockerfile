FROM nginx:1.25-alpine

RUN apk update \
		&& apk add \
			openssl \
			bash \
			npm

RUN  openssl req -x509 -nodes -newkey rsa:4096 -days 365 \
		-keyout /etc/ssl/private/nginx.key \
		-out /etc/ssl/certs/nginx.cert \
		-subj "/C=ES/ST=Barcelona/L=Barcelona/O=42/OU=Education/CN=eralonso.42.fr"

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/default.html

#COPY html /var/www/html

ENTRYPOINT [ "nginx", "-g", "daemon off;" ]
