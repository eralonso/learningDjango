const ws = new WebSocket('ws://localhost:8000/ws/exampleWS/');
    ws.onmessage = (event) => {
      let data = JSON.parse(event.data)
      console.log("online users: ", data.online);
      console.log("state: ", data.msg);
      console.log("users: ");
      data.users.forEach(user => {
        console.log(user, ", ");
      });

