# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: eralonso <eralonso@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/16 17:14:04 by eralonso          #+#    #+#              #
#    Updated: 2024/03/10 12:33:12 by eralonso         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#VARS
COMPOSE_YML := docker-compose.yml

#SHELL
SHELL := /bin/bash

#RULES
all:
	while : ; do \
		sleep 0.5; \
		docker compose -f $(COMPOSE_YML) up -d --build; \
		if [ "$$?" -eq 0 ]; then \
			break; \
		fi; \
	done

start:
	docker compose -f $(COMPOSE_YML) start

stop:
	docker compose -f $(COMPOSE_YML) stop

down:
	docker compose -f $(COMPOSE_YML) down

connect-%:
	docker exec -it $$(docker ps -q -f name=$*) /bin/bash

logs-%:
	docker logs $$(docker ps -q -f name=$*)

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
