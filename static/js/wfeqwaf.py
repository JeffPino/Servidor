import  RPi.GPIO as GPIO
import paho.mqtt.client as mqtt 
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

def alimentarp():
	for i in range(0,1):
		GPIO.output(7, True)
		time.sleep(2)
		GPIO.output(7, False)
		print("Se alimentara al perro")
	GPIO.cleanup()

def on_message(client, obj, msg): 
	#GPIO.output(11, False)
	mensaje=(msg.payload.decode("utf-8"))
	print(mensaje)
	if mensaje=="Alimentar":
		alimentarp()


mqttc = mqtt.Client() 
mqttc.on_message = on_message
mqttc.username_pw_set("jeffersson.pino@gmail.com","Pepino123") 
mqttc.connect("maqiatto.com", 1883) 
mqttc.subscribe("jeffersson.pino@gmail.com/Alimentador", 0)
rc=0
print("Inicio...")
i=0
while rc == 0:
	time.sleep(2)
	rc = mqttc.loop()
	i=i+1