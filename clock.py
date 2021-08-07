import datetime
from genericpath import isfile
import time
import takeCommand as TC
import winsound
import speak_Function as sf

def Current_time():
    Time=datetime.datetime.now()

def Current_hour():
    hour = datetime.datetime.now().hour
    if hour>12:
     h_in_12_formate=hour-12 #change 24 formate to 12 formate.
    (h_in_12_formate) # now h_in_12_hour is current hour in 12 hour format

def Current_minute():
    minute =datetime.datetime.now().minute

def Current_second():
    second = datetime.datetime.now().second


def SetAlerm(set_alerm_time):
    print(set_alerm_time)
    while True:
        time.sleep(1)
        dureation=1
        current_time = datetime.datetime.now()
        now= current_time.strftime("%H:%M:%S")
        min=current_time.strftime("%H:%M")
        Date=current_time.strftime("%d %m %Y")
        print('The Set date is',Date)
        print(min)
        print(set_alerm_time)
        if min==set_alerm_time:
            winsound.PlaySound("ytuy",winsound.SND_LOOP)
            print('Its Wekup time')
        elif(min>=set_alerm_time):
            break

def alarm_time():
 query=TC.TakeCommand()
 am=query.find("a.m.")
 pm=query.find("p.m.")
 global atime;
 if am !=-1 or pm !=-1:
  if am !=-1:  # .inf return alwaya -1 if index not found 
    s=am-6
    l=am
    x=slice(s,l) # slice ti innd vlauce of edex starting to ending index no 
    atime=(query[x])  
  if pm!=-1:    # .inf return alwaya -1 if index not found   
    s = pm-6
    l = pm
    hours = slice(s,l)# use slice for cut all unnesesery word only time and AM PM
    atime = (query[s]).lower()  # to conver in to upper besose system time is also uppater likw 12:30AM
  print(atime) #alarm time that taken by user
  atime=int(atime)
  atime=atime-24
  print(atime)
  
  

  while True:
        global hour_in_12_format # varibal for Globle use
        time.sleep(1)
        current_time = datetime.datetime.now()
        now= current_time.strftime("%H:%M")
        hour = datetime.datetime.now()
        min=datetime.datetime.now().minute  


        print('The Set date is',atime)
        print(now)
        print(atime)
        
 else:
     print('Not set')

def change_time_formate():  # change time formate 24 to 12
        current_time = datetime.datetime.now()   
        now= current_time.strftime("%H:%M:%S")
        min=current_time.strftime("%H:%M")
        Date=current_time.strftime("%d %m %Y")
        print('The Set date is',Date)


SetAlerm('13:47')
#alarm_time()