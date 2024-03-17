# **************************************************************************** #
#																			   #
#														  :::	   ::::::::    #
#	 consumers.py										:+:		 :+:	:+:    #
#													  +:+ +:+		  +:+	   #
#	 By: eralonso <eralonso@student.42barcel>		+#+  +:+	   +#+		   #
#												  +#+#+#+#+#+	+#+			   #
#	 Created: 2024/03/15 11:36:56 by eralonso		   #+#	  #+#			   #
#	 Updated: 2024/03/17 17:43:53 by eralonso		  ###	########.fr		   #
#																			   #
# **************************************************************************** #

import json
from channels.generic.websocket import WebsocketConsumer

class ExampleConsumer(WebsocketConsumer):

	connections = []

	def connect(self):
		self.accept()
		self.user = self.scope["user"]
		self.connections.append(self)
		self.update_indicator(msg="Connected")

	def disconnect(self, code):
		self.update_indicator(msg="Disconnected")
		self.connections.remove(self)
		return super().disconnect(code)

	def update_indicator(self, msg):
		for connection in self.connections:
			connection.send(
				text_data=json.dumps(
					{
						"msg": f"{self.user} {msg}",
						"online": f"{len(self.connections)}",
						"users": [f"{user.scope['user']}" for user in self.connections],
					}
				)
			)


