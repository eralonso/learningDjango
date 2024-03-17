# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    routing.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: eralonso <eralonso@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/14 18:02:54 by eralonso          #+#    #+#              #
#    Updated: 2024/03/17 17:37:26 by eralonso         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.urls import path
from web_sockets.consumers import ExampleConsumer

urlpatterns = [
    path("ws/exampleWS", ExampleConsumer.as_asgi()),
]
