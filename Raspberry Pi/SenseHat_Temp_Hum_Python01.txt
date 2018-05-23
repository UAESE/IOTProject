# Sense Hat Temp & Hum Reading Python Code V0.1

#import module 
from sense_hat import SenseHat

#clean start
sense = SenseHat()
sense.clear()

#calculate temp
temp = sense.get_temperature_from_pressure()
temp = round(temp, 1)
print("Temperature: %s C" % temp)

#calculate humidity 
humidity = sense.get_humidity()
humidity = round(humidity, 2)

print("Humidity: %s %%rH" % humidity)