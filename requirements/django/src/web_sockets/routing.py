# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    routing.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: eralonso <eralonso@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/14 18:02:54 by eralonso          #+#    #+#              #
#    Updated: 2024/03/18 12:22:07 by eralonso         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.urls import path
from web_sockets.consumers import ExampleConsumer

urlpatterns = [
    path("ws", ExampleConsumer.as_asgi()),
]
