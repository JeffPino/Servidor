//https://www.eclipse.org/paho/clients/js/

function nivel(){
	document.getElementById("tanto").innerHTML=mentrada+"%";
}
function App() {
	console.log("Se Alimentara un perro pequeño");
	message = new Paho.MQTT.Message("APP")
	message.destinationName="jeffersson.pino@gmail.com/Alimentador";
    client.send(message);
}
function Apm() {
	console.log("Se Alimentara un perro mediano");
	message = new Paho.MQTT.Message("APM")
	message.destinationName="jeffersson.pino@gmail.com/Alimentador";
    client.send(message);
}
function Apg() {
	console.log("Se Alimentara un perro grande");
	message = new Paho.MQTT.Message("APG")
	message.destinationName="jeffersson.pino@gmail.com/Alimentador";
    client.send(message);
}
function Apx() {
	console.log("Se Alimentara un perro gigante");
	message = new Paho.MQTT.Message("APX")
	message.destinationName="jeffersson.pino@gmail.com/Alimentador";
    client.send(message);
}




// Create a client instance
  //client = new Paho.MQTT.Client("postman.cloudmqtt.com", 14970);
  
  client = new Paho.MQTT.Client("maqiatto.com", 8883, "web_" + parseInt(Math.random() * 100, 10));

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
	
    client.subscribe("jeffersson.pino@gmail.com/WEB");
    message = new Paho.MQTT.Message("Enlace... OK!");
    message.destinationName = "jeffersson.pino@gmail.com/Alimentador";
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
    console.log(message.payloadString);
    mentrada=message.payloadString;
    document.getElementById("tanto").innerHTML=mentrada;
    if (mentrada == "0"){
		alert("No hay alimento en el dispensador");

  }
  
