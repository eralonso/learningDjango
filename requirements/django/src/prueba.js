const WebSocket = require('ws')

const ws = new WebSocket('wss://localhost:443/ws', {
	rejectUnauthorized: false
});

ws.onmessage = (event) => {
	let data = JSON.parse(event.data)
	console.log("online users: ", data.online);
	console.log("state: ", data.msg);
	console.log("users: ");
	data.users.forEach(user => {
		console.log(user, ", ");
	})
};

ws.on('error', (err) => {
	console.log(err.message)
});
