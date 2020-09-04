import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup (7, GPIO.IN)
GPIO.setup (11, GPIO.OUT)
f=open("sensor.txt","w")
c=0
while(True):
	 if GPIO.input(7):
	     GPIO.output(11, False)
	     print("boton activado")
	     c=c++1;
	     f.write("29/07/2020:15:54     "+str(1) +"\n")
	     time.sleep(1)
	     
	 else:
	       GPIO.output(11, True)
	       print("boton desactivado")
	       time.sleep(1)
	      
 
def main ():
	print("fin")
	while(1):
	 f.close()
	 pass
#main()