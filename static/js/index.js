//https://www.eclipse.org/paho/clients/js/

function Alimentar() {
	console.log("Se enviara alimento");
	message = new Paho.MQTT.Message("Alimentar perro")
	message.destinationName="jeffersson.pino@gmail.com/Alimentador";
    client.send(message);
}
function LED1_On() {
	alert("led on");
	console.log("led on");
	message = new Paho.MQTT.Message("LED1_ON")
	message.destinationName="jeffersson.pino@gmail.com/test";
    client.send(message);
}
function LED1_Off(){	
	console.log("led off");
	message = new Paho.MQTT.Message("LED1_OFF")
	message.destinationName="jeffersson.pino@gmail.com/test";
    client.send(message);
}






// Create a client instance
  //client = new Paho.MQTT.Client("postman.cloudmqtt.com", 14970);
  
  client = new Paho.MQTT.Client("maqiatto.com", 3883, "web_" + parseInt(Math.random() * 100, 10));

  // set callback handlers
  client.onConnectionLost = onConnectionLost;
  client.onMessageArrived = onMessageArrived;
  var options = {
   useSSL: false,
    userName: "jeffersson.pino@gmail.com",
    password: "Pepino123",
    onSuccess:onConnect,
    onFailure:doFail
  }

  // connect the client
  client.connect(options);
   
  // called when the client connects
  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("Conectado...");
	
    client.subscribe("jeffersson.pino@gmail.com/test");
    message = new Paho.MQTT.Message("hola desde la web");
    message.destinationName = "jeffersson.pino@gmail.com/test";
    client.send(message);
	
  }

  function doFail(e){
    console.log(e);
	
  }

  // called when the client loses its connection
  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:"+responseObject.errorMessage);
    }
  }

  // called when a message arrives
  function onMessageArrived(message) {
    console.log("onMessageArrived:"+message.payloadString);
  }
  
