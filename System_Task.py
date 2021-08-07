#########################################################################################
# 1.Screenshot():        tack screen shot 
# 2.cleanTempFile ()     remove all temporary files
# 3.RefresPC()            Rfress My PC
# 4
# 5
# 6
# 7
# 8
# 9                 
#########################################################################################
from math import sin
import sys
import os
import pyautogui
import time
import speak_Function as sf
import takeCommand as TC
from tkinter import filedialog
import random

#1.def singal_screenshot():
def screenshot(query):
       # query = query.replace('screenshot','') 
        if 'Take a screeenshot' in query or 'single'  in query:
             singal_screenshot()
    
        elif 'multiple 'in query and 'multiple screenshot' or 'more then one' in query:
             multi_screenshot() 
             return
        elif 'folder'in query or 'disk' in query or 'drive'in query:
            singal_screenshot_folder()
            return
        elif 'name'in query or 'with' in query:
            singal_screenshot_name()
            return
        elif 'none' in query :
            sf.speak('Sorry i am unable to take screenshot') 
            print('Sorry i am unable to take screenshot')
            return
        else:
            sf.speak('sorry i am unable to take screenshot')    

def singal_screenshot():

    # name_of_ss="ANAS"
    #path=("Screenshot/"+ name_of_ss+ ".png") 
    name_of_ss = str(random.random()) # genarate a rendom number flot no random alwaysa craete a float so fisrt conver into str2
    path=("screenshot/"+ name_of_ss+ ".png")
    pyautogui.screenshot(path)
    sf.speak('Screenshots done ')
    print('Screenshot Done ')

# 2.Screenshot in a spesific folder():  Working....for finding root 
def singal_screenshot_folder():
    path="screenshot/img.png"
    sf.speak(" Name of screenshot ")
    name_of_ss=TC.TakeCommand()
    path= path+''+name_of_ss+ '.png'
    pyautogui.screenshot(path)
  

# 2.Screenshot in a spesific  with name():    
def singal_screenshot_name():
    sf.speak(" Name of screenshot ")
    name_of_ss=TC.TakeCommand().replace("","")
    name_of_ss=name_of_ss.replace("","")
    print(name_of_ss)
    path=("screenshot/"+ name_of_ss+ ".png")
    
    pyautogui.screenshot(path)
    sf.speak("Screenshot Done its name is"+name_of_ss)
    
def singal_screenshot_name_folder():
    sf.speak(" Name of screenshot ")
    name_of_ss=TC.TakeCommand()
    path=("screenshot/"+ name_of_ss+ ".png")
    pyautogui.screenshot(path)
    sf.speak("Screenshot Done its name is"+name_of_ss)


# 2.def multi_screenshot():
def multi_screenshot():
    sf.speak("number of Screenshots  you wnat to take")
    No_of_ss=int(input("number of Screenshots  you want to take: "))
    sf.speak(" Name of screenshot ")
    name_of_ss=(input("Tell me any singal  name for save screenshot: "))
    sf.speak("Time Diffraction of Screenshots in Second")
    t=int((input("Tell me time Diffreance of Screenshots in Second :")))
    i=1
    while i<No_of_ss:
        pyautogui.screenshot("screenshot/"+name_of_ss+""+str(i)+".png")
        sf.speak(str(i)+'screenshot Done')
        print(str(i)+' screenshot Done')
        i+=1
        time.sleep(t)
    sf.speak('All Multiple Screenshot Done')


#########################################################################################

#                        OPEN AND CLOSE APPLICTION

#########################################################################################
def OpenCloseApps(query):    
    if 'notepad' in query and 'open'in query or 'open text editor' in query:
         
         os.system('notepad.exe')
         sf.speak("Notepad opening")
         print("it's open Enjoy with Notepade")

    elif 'notepad' in query and 'close'in query :
        os.system('taskkill/im notepad.exe')  
        sf.speak("Notepad closed")
        print("Notepad closed")

    elif 'explorer' in query: 
        if 'open' in query:           
          os.system('explorer')

        elif 'close' in query: 
         os.system('taskkill/im explorer.exe')

    elif 'cmd' in query and 'command promat'in query :
         sf.speak("Cmd opening")
         print("it's open Enjoy with Notepade")
         os.system('cmd.exe')
         




#########################################################################################

#                         SHOUTDOWN

#########################################################################################

   
def shutdown():
    sf.speak(' You want to shoutdown just Say yes or NO')
    print(' You want to shoutdown just Say yes or NO')
    check=TC.TakeCommand().lower()
    print(check)
    if check=='yes':
        sf.speak(' Your PC is Shutdown')
        print('Your PC is Shutdown.')
        os.system('shutdown /r')
    else:
      sf.speak('ok. i do not  shutdown pc ')
def lockpc():
    sf.speak(' You want to lock your PC  just Say yes or NO')
    print(' You want to lock your PC  just Say yes or NO')
    check=TC.TakeCommand().lower()
    if check=='yes':
        sf.speak(' YOur PC is Locking')
        print('YOur PC is Locking...')
        os.system('shutdown /l')
    else:
      sf.speak('ok.  i am not locking Pc')

    
if __name__ == "__main__":
    singal_screenshot()
    #singal_screenshot_name()
   # multi_screenshot()
    #set_for_multitimes_SS()
    #singal_screenshot_folder()
    
    #shutdown()
    #lockpc()

