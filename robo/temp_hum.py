import sys

import Adafruit_DHT

sensor = 11
pin = 25
while True:
   f = open('/home/pi/data/temp_hum.txt','w')
   sys.stdout = f
   humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
   if humidity is not None and temperature is not None:
       print >> f,('{0:0.1f}  {1:0.1f}'.format(temperature, humidity))
   else:
       print('Failed to get reading. Try again!')
       sys.exit(1)
time.sleep(5) 
