//import WebSocket from 'ws';

function	createWebSocket() {
	//const WebSocket = require('ws');
	//process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";
	
	const ws = new WebSocket('wss://localhost:443/api/ws');
	//const ws = new WebSocket('wss://localhost:443/api/ws', { rejectUnauthorized: false });
	//const ws = new WebSocket('wss://localhost:443/api/ws', {
	//	rejectUnauthorized: false
	//});
	
	//ws.onmessage = (event) => {
	//	let data = JSON.parse(event.data)
	//	console.log("online users: ", data.online);
	//	console.log("state: ", data.msg);
	//	console.log("users: ");
	//	data.users.forEach(user => {
	//		console.log(user, ", ");
	//	})
	//};
	
	//ws.on('error', (err) => {
	//	console.log(err.message)
	//});
	
	const presenceEl = document.getElementById('pre_cnt');
	const messagesEl = document.getElementById('messages');
	const onlineUsers = document.querySelector("#online-users");
	
	ws.onmessage = (event) => {
		onlineUsers.innerHTML = "";
	
		let data = JSON.parse(event.data)
		presenceEl.innerHTML = data.online;
	
		const li1 = document.createElement('li');
		li1.innerHTML = data.msg;
		messagesEl.appendChild(li1);
	
		data.users.forEach(user => {
			const li2 = document.createElement("li");
			li2.classList.add("on-us")
			li2.innerHTML = user;
			onlineUsers.appendChild(li2);
		});
	};
}

const	btn_web = document.getElementById('ws-button');

btn_web.addEventListener("click", createWebSocket);
