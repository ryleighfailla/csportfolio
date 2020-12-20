import grovepi
import math
from grovepi import *
from time import sleep
from math import isnan
import json
# SIG,NC,VCC,GND
sensor = 4  # The Sensor goes on digital port 4.

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

#connect red LED to digital port 5, green LED to digital port 6, blue LED to digital port 7
rled=5
gled=6
bled=7


while True:
    try:
        [temp,humidity] = grovepi.dht(sensor,0)
        ftemp=(temp*1.8)+32
        hum=humidity
        if math.isnan(ftemp) == False and math.isnan(humidity) == False:
            print("temp = %.02f F humidity =%.02f%%"%(ftemp, humidity))
        t=str(ftemp)
        h=str(hum)

#defining the temperature parameters 
        if ftemp > 60 and ftemp < 85 or hum > 80:
            grovepi.digitalWrite(gled,1)
        else:
            grovepi.digitalWrite (gled,0)
        if ftemp < 60 and ftemp >=85 or hum > 80:
            grovepi.digitalWrite(bled,1)
        else:
            grovepi.digitalWrite(bled,0)
        if ftemp > 95:
            grovepi.digitalWrite(rled,1)
        else:
            grovepi.digitalWrite(rled,0)

        #measure every 1 minutes (60 seconds)
        time.sleep(60)

    except IOError:
        print ("Error")
             






#create json array
temp_hum_data ={
    "TempF" : ftemp,
    "Humidity": hum
    }

#writing temperature readings to json file
def store_json(data: dict, temp_hum_data:str):
	with open ("temp_hum.json","w") as json_stored:
  	  json_dump(temp_hum_data, json_stored)

store_json(temp_hum_data, "temp_hum.json")

#opening the json file
with open ("temp_hum.json", "r") as openfile:
	json_object=json.load(openfile)

print(json_object)
print(type(json_object)