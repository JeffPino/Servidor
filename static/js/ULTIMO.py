import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt 
import datetime

LCD_RS = 6
LCD_E  = 7
LCD_D4 = 8
LCD_D5 = 9
LCD_D6 = 10
LCD_D7 = 11

LCD_WIDTH = 20    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line
POR = 0xA4 # LCD RAM address for the 4th line

 
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005


# Main program block
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) # DB7
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
f=open("horario.txt","w")

def buscando():
	hora=datetime.datetime.now().strftime('%H:%M')
	f=open("horario.txt","r")
	horario = f.read() 
	if horario==hora:
		programada(horario)
	f.close()
	
def programada(horario):
	lcd_string("Horario:     "+ horario,LCD_LINE_3)
	GPIO.output(17, True)
	time.sleep(10)
	GPIO.output(17, False)
	print("Se alimentara al perro")
	lcd_string("                    ",LCD_LINE_3)
	time.sleep(50)
		
def alimentarp():
		lcd_string("PERRO PEQUENO",LCD_LINE_3)
		GPIO.output(17, True)
		time.sleep(2)
		GPIO.output(17, False)
		print("Se alimentara al perro")
		lcd_string("                    ",LCD_LINE_3)

def alimentarm():
		lcd_string("PERRO MEDIANO",LCD_LINE_3)
		GPIO.output(17, True)
		time.sleep(4)
		GPIO.output(17, False)
		print("Se alimentara al perro")
		lcd_string("                    ",LCD_LINE_3)

def alimentarg():
		lcd_string("PERRO GRANDE",LCD_LINE_3)
		GPIO.output(17, True)
		time.sleep(6)
		GPIO.output(17, False)
		print("Se alimentara al perro")
		lcd_string("                    ",LCD_LINE_3)

def alimentarx():
		lcd_string("PERRO GIGANTE",LCD_LINE_3)
		GPIO.output(17, True)
		time.sleep(8)
		GPIO.output(17, False)
		print("Se alimentara al perro")	
		lcd_string("                    ",LCD_LINE_3)
		
def ocantidad(a):
		lcd_string("Cant definida:",LCD_LINE_3)
		lcd_string(str(a)+" g",POR)
		b=((a*1)/10)
		print(b)
		GPIO.output(17, True)
		time.sleep(b)
		GPIO.output(17, False)

		print("Se alimentara al perro")	
		lcd_string("                    ",LCD_LINE_3)
		
def on_message(client, obj, msg): 
	mensaje=(msg.payload.decode("utf-8")).split(" ")[0]
	dato=(msg.payload.decode("utf-8")).split(" ")[1]
	print(mensaje + dato)
	if mensaje=="APP":
		alimentarp()
	elif mensaje=="APM":
		alimentarm()
	elif mensaje=="APG":
		alimentarg()
	elif mensaje=="APX":
		alimentarx()
	elif mensaje =="H":
		f=open("horario.txt","w")
		f.write(dato)
		f.close()
	elif mensaje=="C":
		men=int(dato)
		print("H")
		ocantidad(men)
		
def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)
 
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
 
def lcd_string(message,line):
  # Send string to display
 
  message = message.ljust(LCD_WIDTH," ")
 
  lcd_byte(line, LCD_CMD)
 
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
 
lcd_init()
mqttc = mqtt.Client() 
mqttc.on_message = on_message
mqttc.username_pw_set("jeffersson.pino@gmail.com","Pepino123") 
mqttc.connect("maqiatto.com", 1883) 
mqttc.subscribe("jeffersson.pino@gmail.com/Alimentador", 0)
rc=0
print("Inicio...")
i=0

while rc == 0:
	rc = mqttc.loop()
	lcd_string("ALIMENTADOR DE PERRO",LCD_LINE_2)
	buscando()
	if GPIO.input(16):
	 mqttc.publish("jeffersson.pino@gmail.com/WEB", "100")
	 lcd_string("100%",POR)
	 GPIO.output(18, True)
	 GPIO.output(19, True)
	 GPIO.output(20, True)
	 GPIO.output(21, True)
	 GPIO.output(22, True)
	 GPIO.output(23, True)
	 GPIO.output(24, True)
	 GPIO.output(25, True)
	 GPIO.output(26, True)
	 GPIO.output(27, True)
	elif GPIO.input(15):
	 lcd_string(" 80%",POR)
	 mqttc.publish("jeffersson.pino@gmail.com/WEB", "80")
	 GPIO.output(18, False)
	 GPIO.output(19, False)
	 GPIO.output(20, True)
	 GPIO.output(21, True)
	 GPIO.output(22, True)
	 GPIO.output(23, True)
	 GPIO.output(24, True)
	 GPIO.output(25, True)
	 GPIO.output(26, True)
	 GPIO.output(27, True)
	elif GPIO.input(14):
	 lcd_string(" 60%",POR)
	 mqttc.publish("jeffersson.pino@gmail.com/WEB", "60")
	 GPIO.output(18, False)
	 GPIO.output(19, False)
	 GPIO.output(20, False)
	 GPIO.output(21, False)
	 GPIO.output(22, True)
	 GPIO.output(23, True)
	 GPIO.output(24, True)
	 GPIO.output(25, True)
	 GPIO.output(26, True)
	 GPIO.output(27, True)
	elif GPIO.input(13):
	 lcd_string(" 40%",POR)
	 mqttc.publish("jeffersson.pino@gmail.com/WEB", "40")
	 GPIO.output(18, False)
	 GPIO.output(19, False)
	 GPIO.output(20, False)
	 GPIO.output(21, False)
	 GPIO.output(22, False)
	 GPIO.output(23, False)
	 GPIO.output(24, True)
	 GPIO.output(25, True)
	 GPIO.output(26, True)
	 GPIO.output(27, True)
	elif GPIO.input(12):
	 lcd_string(" 20%",POR)
	 mqttc.publish("jeffersson.pino@gmail.com/WEB", "20")
	 GPIO.output(18, False)
	 GPIO.output(19, False)
	 GPIO.output(20, False)
	 GPIO.output(21, False)
	 GPIO.output(22, False)
	 GPIO.output(23, False)
	 GPIO.output(24, False)
	 GPIO.output(25, False)
	 GPIO.output(26, True)
	 GPIO.output(27, True)
	else: 
	 lcd_string("ALERTA NO HAY COMIDA",LCD_LINE_4)
	 mqttc.publish("jeffersson.pino@gmail.com/WEB", "0")
	 lcd_string("  0%",POR)
	 GPIO.output(18, False)
	 GPIO.output(19, False)
	 GPIO.output(20, False)
	 GPIO.output(21, False)
	 GPIO.output(22, False)
	 GPIO.output(23, False)
	 GPIO.output(24, False)
	 GPIO.output(25, False)
	 GPIO.output(26, False)
	 GPIO.output(27, False)
	lcd_string("GRUPO 6",LCD_LINE_1)
	time.sleep(0.5)
	lcd_string("M. PILATUNA",LCD_LINE_1)
	time.sleep(0.5)
	lcd_string("P. MALDONADO",LCD_LINE_1)
	time.sleep(0.5)
	lcd_string("C. PILCO",LCD_LINE_1)
	time.sleep(0.5)
	lcd_string("JEFF PINO",LCD_LINE_1)
	time.sleep(0.5)
	GPIO.cleanup()
	if GPIO.input(2):
		alimentarp()
	if GPIO.input(3):
		alimentarm()
	if GPIO.input(4):
		alimentarg()
	if GPIO.input(5):
		alimentarx()
 