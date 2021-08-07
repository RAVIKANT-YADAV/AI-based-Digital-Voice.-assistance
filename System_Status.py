import urllib.request
import urllib
import psutil

def connect(host='http://iitdeveloper.com'):
    try:
        global status
        urllib.request.urlopen(host) #Python 3.x
        status='connect'
        return True

    except:
        status='noconnect'
        return False 
def connection():
    status="connected" if connect()  else "nointernet" 
    print(status)

connection()  

    # python script showing battery details


# function returning time in hh:mm:ss
def convertTime(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	return "%d:%02d:%02d" % (hours, minutes, seconds)


def battery():
# returns a tuple
   battery = psutil.sensors_battery()
   print("Battery percentage : ", battery.percent)
   print("Power plugged in : ", battery.power_plugged)
      # converting seconds to hh:mm:ss
   print("Battery left : ", convertTime(battery.secsleft))

    