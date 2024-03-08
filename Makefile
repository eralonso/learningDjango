# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: eralonso <eralonso@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/16 17:14:04 by eralonso          #+#    #+#              #
#    Updated: 2024/03/08 11:27:22 by eralonso         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#VARS
COMPOSE_YML := docker-compose.yml

#SHELL
SHELL := /bin/bash

#RULES
all:
	docker compose -f $(COMPOSE_YML) up -d --build

start:
	docker compose -f $(COMPOSE_YML) start

stop:
	docker compose -f $(COMPOSE_YML) stop

down:
	docker compose -f $(COMPOSE_YML) down

connect:
	docker exec -it $$(docker ps -q -f name=django_test) /bin/bash

clean:
	-docker system prune --all --force

fclean: down clean
	-docker volume prune --force
	VOLUMES_ID=$$(docker volume ls -q); \
	if [ ! -z $$VOLUMES_ID ]; then \
		docker volume rm $$VOLUMES_ID; \
	fi

re: clean all

.PHONY: all start stop down clean fclean re
.SILENT:
