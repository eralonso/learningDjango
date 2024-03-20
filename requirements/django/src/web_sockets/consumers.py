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
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class ExampleConsumer(AsyncJsonWebsocketConsumer):

	connections = []

	async def connect(self):
		await self.accept()
		print("accepted connection")
		self.user = self.scope["user"]
		self.connections.append(self)
		await self.update_indicator(msg="Connected")

	async def disconnect(self, code):
		self.update_indicator(msg="Disconnected")
		self.connections.remove(self)
		return await super().disconnect(code)

	async def update_indicator(self, msg):
		for connection in self.connections:
			await connection.send_json({
						"msg": f"{self.user} {msg}",
						"online": f"{len(self.connections)}",
						"users": [f"{user.scope['user']}" for user in self.connections],
			    })


