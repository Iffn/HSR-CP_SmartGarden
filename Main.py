
def sendRainState():
        #Get Data
        url = "https://api.forecast.io/forecast/" + key + "/" + locLat + "," + locLong
        response = urllib.urlopen(url).read()

        #Interpret Data
        posRain = response.find('"precipType":"rain"')
        if(posRain != -1):
                posComma2 = response.rfind(",",0,posRain)
                posComma1 = response.rfind(",",0,posComma2)
                rainChance = float(response[posComma1+21:posComma2])
                print(rainChance)
                
                if (rainChance>=0.5):
                        ser.write('2&') #it will rain
                else :
                        ser.write('3&') #it will not rain
                
	


def getValuesAndPublsih():
        ser.write('1&')

        #Arduino sends messages
        
        myTrashString = ser.readline()
        #recTemp = int(ser.readline())
        #print(recTemp)
        #recHumAir = int(ser.readline())
        #print(recHumAir)
        recHumEarth = int(ser.readline())
        print(recHumEarth)
        recLight = int(ser.readline())
        print(recLight)
        
        #publish
		
        sendString =  " ; Humidity Earth: " + str(recHumEarth) + " ; Light: " + str(recLight)
        #""" "Temperature: " + str(recTemp) + " ; Humidity Air: " + str(recHumAir) +"""
        publish.single("/SmartGarden/Station1", sendString, hostname=publisherAdress)
		
		
	#Console Output
        
        



import serial,time,urllib
from datetime import datetime
import paho.mqtt.publish as publish

ser = serial.Serial('/dev/ttyACM0',9600)

#User defined Data:
getDataIntervall = 19 #in minutes, minimum 2
sendWeatherIntervall = 19 #in hours, minimum 2
key = "" #use your own key from https://developer.forecast.io/
locLat = "47.2267" #position rapperswil -> gets zurich
locLong = "08.8167"
publisherAdress = "localhost"

#System Variables, don't change these:
gotValues = False
sentWeather = False

print("setup complete")


while(1):
        #Get Data from Arduino
        if(datetime.now().second%getDataIntervall==0):
                if(gotValues == False):
                        print("getValues")
                        getValuesAndPublsih()
                        gotValues = True
        else:
                gotValues = False
                
        #Get and process weather data
        if(datetime.now().second%sendWeatherIntervall==10):
                if(sentWeather == False):
                        print("getRainData")
                        sendRainState()
                        sentWeather = True
        else:
                sentWeather = False











