import socket
import time
import RPi.GPIO as GPIO
import time
import RPi.GPIO as GPIO
import time
import RPi.GPIO as GPIO 
import time
#set the GPIO default settings
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
#definde pin numbers
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
x = 0
RELAIS_1_GPIO = 18
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
servo1 = GPIO.PWM(16,50) 
servo2 = GPIO.PWM(22,50)
servo1.start(0)
servo2.start(0)
#start server communication
ClientSocket = socket.socket()
host = '10.0.0.13'
port = 8080
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
Response = ClientSocket.recv(1024)
dataX = 0
dataY = 0
previousY = 0
previousX = 0
dutyCycle = 0
a = 0
shoot = 0
servoOne = False
servoTwo = False
move = 0
while True:
    #ask the server for data 
    ClientSocket.send(str.encode("Input"))
    Response = ClientSocket.recv(1024)
    message = Response.decode('utf-8')
    #extract the x, y, and shoot information
    data = message[3:]
    dataX = int(data[:3]) - 100
    dataY = data[5:]
    dataY = int(dataY[:-1]) - 100
    screen = int(data[-1])
    if(shoot == 1):
        screen = 1
    #move the cannon if the change is big enough
    if (abs(dataY - previousY) < 5):
        servoOne = True
        servo1.ChangeDutyCycle(0)
        dutyCycle = 0
    else:
        angle = abs((float(dataY)-450)/2.77)
        servoOne = False
        if(move == 0):
            servo1.ChangeDutyCycle(2+(angle/18))
        else:
            servo1.ChangeDutyCycle(0)
        dutyCycle = 2+(angle/18)
    previousY = dataY
    if (abs(dataX - previousX) < 5):
        servo2.ChangeDutyCycle(0)
        servoTwo = True
    else:
        angle = abs((float(dataX) - 700)/4)
        servoTwo = False
        if(move == 0):
            servo2.ChangeDutyCycle(2+(angle/18))
        else:
            servo2.ChangeDutyCycle(0)
    previousX = dataX
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)
    servo2.ChangeDutyCycle(0)
    #lock both servos and then shoot 
    if((servoOne == True) and (servoTwo == True)):
        shoot = 1
    #check the light sensor to see if the ball has been shot yet
    if(GPIO.input(8) == GPIO.LOW):
        if((shoot == 1) and (screen == 1)):
            GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
            shoot = 1
            move = 1
        else:
            move = 0
            GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
            shoot = 0
    #stop the pump when the light senor is unblocked (once the ball is shot)
    else:
        move = 0
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) 
        shoot = 0

