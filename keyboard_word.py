import pyautogui
import keyboard
import time
import takeCommand as TC
import speak_Function as sf
import os 



def write_note():
        sf.speak("Notebook is opening..")
        os.system('start notepad.exe')
        sf.speak("What you wnat to write please tell me sir :")
        while True: 
            note=TC.TakeCommand().lower()
            
 
            if note !='none' and  note !='save it' or 'close notebook'or 'close notebook': 
               keyboard.release("tab")
               keyboard.press("tab")
               keyboard.write(note)
            if note =='save it' or 'close notebook'or 'close notebook' :
                sf.speak(" you want to save it")
                conf=TC.TakeCommand().lower
                if 'yes 'in conf:
                    pyautogui.keyDown("ctrl")
                    keyboard.press("s")
                    keyboard.release('s')
                    pyautogui.keyup("ctrl")   
               
          
                
        

       
#keyboard = Controller()
while True:
 query=TC.TakeCommand()
 if 'stop'in query  or 'push' in query or 'play' in query:
    keyboard.press("space")
    keyboard.release('space')


 elif 'refresh' in query:
    pyautogui.keyDown("win")
    keyboard.press("d") 
    pyautogui.keyUp("win") 
    sf.speak('start refreshing.')
    for i in range(6):

       pyautogui.keyDown("win")
       keyboard.press("f5") 
       pyautogui.keyUp("win")
    sf.speak('Complated.')
    pyautogui.keyDown("win")
    keyboard.press("d") 
    pyautogui.keyUp("win") 

 elif 'change window' in query or 'next window' in query:
   # Holds down the alt key
    pyautogui.keyDown("alt")
    keyboard.press("tab") 
    pyautogui.keyUp("alt")

 elif 'writ a note' in query or 'write someting' in query or 'want to write' in query :
   # write someting
    write_note()
    


 elif 'up' in query:
   # Holds down the alt key
    keyboard.press("up")  
    keyboard.release('up')
    

 elif 'down' in query:
   # Holds down the alt key
    keyboard.press("down") 
    keyboard.release('down') 

 elif 'left' in query:
   # Holds down the alt key
    keyboard.presss("left")  
    keyboard.release('left')
    

 elif 'right' in query or 'forward' in query:
   # Holds down the alt key
    keyboard.press("right") 
    keyboard.release('right')   
    
 
 elif 'paste' in query or 'control v'in query:
     pyautogui.keyDown("ctrl")
     keyboard.press("v") 
     keyboard.release('v')
     pyautogui.keyUp("ctrl")


 elif 'cut' in query or 'cut'in query:
     pyautogui.keyDown("ctrl")
     keyboard.press("x")       
     keyboard.release('x')
     pyautogui.keyUp("ctrl")

 elif 'copy' in query or 'copy'in query:
     pyautogui.keyDown("ctrl")
     keyboard.press("c") 
     keyboard.release('c')
     pyautogui.keyUp("ctrl")   
 

 elif 'delete' in query :
     keyboard.press("delete") 
     keyboard.release('delete')

 elif 'delete' in query and 'permanent ' or 'permanent delete' in query :
     pyautogui.keyDown("ctrl")
     pyautogui.keyDown("shift")
     keyboard.press("delete") 
     keyboard.release('deletel')
     pyautogui.keyup("shift")
     pyautogui.keyUp("ctrl")  

 # Window kyes win 

 elif  'minimise all window' in query or 'minimise window'in  query or 'minimise' in query and'all' in query:
     pyautogui.keyDown("win")
     keyboard.press("m") 
     keyboard.release('m')
     pyautogui.keyUp("win")

 elif 'minimise window' in query or'minimise' in query:
     pyautogui.keyDown("win")
     keyboard.press('down') 
     keyboard.release('down')
     pyautogui.keyUp("win") 


 elif 'maximize'in query :
     pyautogui.keyDown("win")
     keyboard.press("up") 
     keyboard.release
     pyautogui.keyUp("win")   

 elif ' maximize 'in query and 'now'in query and 'all' or 'minimise' in query and 'now' in query:
     pyautogui.keyDown("win")
     keyboard.press("d") 
     pyautogui.keyUp("win") 


 elif 'close'in query:
    pyautogui.keyDown("alt")
    keyboard.press("f4")  
    keyboard.release('f4')
    pyautogui.keyUp("alt")


# Chrome automation the.......................................................
 elif 'close tab'in query:
    pyautogui.keyDown("ctrl")
    keyboard.press("w")  
    keyboard.release('w')
    pyautogui.keyUp("ctrl")
 elif 'new tab'in query:
    pyautogui.keyDown("ctrl")
    keyboard.press("n")  
    keyboard.release('n')
    pyautogui.keyUp("ctrl")
 elif 'next tab'in query:
    pyautogui.keyDown("ctrl")
    keyboard.press("w")  
    keyboard.release('w')
    pyautogui.keyUp("ctrl")

 elif 'history'in query and 'browser' in query:
    pyautogui.keyDown("ctrl")
    keyboard.press("h")  
    keyboard.release('h')
    pyautogui.keyUp("ctrl") 

 elif 'download'in query and 'browser' in query:
    pyautogui.keyDown("ctrl")
    keyboard.press("j")  
    keyboard.release('j')
    pyautogui.keyUp("ctrl")
 elif 'history'in query and 'browser' in query:
    pyautogui.keyDown("ctrl")
    keyboard.press("w")  
    keyboard.release('w')
    pyautogui.keyUp("ctrl")
    # Go Incognito Mode
 elif 'private tab'in query and 'Incognito' in query:
    pyautogui.keyDown("win")
    pyautogui.keyDown("shift")
    keyboard.press(" n")  
    keyboard.release('n')
    pyautogui.keyUp('shift')
    pyautogui.keyUp("ctrl") 

 #Clear Browsing Data (Ctrl + Shift + Delete)
 elif 'Clear Browsing Data'in query and 'Clear Browsing Data' in query:
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("shift")
    keyboard.press(" delete")  
    keyboard.release('delete')
    pyautogui.keyUp('shift')
    pyautogui.keyUp("ctrl") 

 


#Open Bookmarks Manager
 elif 'private tab'in query and 'Incognito' in query:
    pyautogui.keyDown("ctrl")
    keyboard.press(" b")  
    keyboard.release('b')
    pyautogui.keyUp("ctrl")



#Open a new tab, and jump to it	Ctrl + t

 elif 'Open a new tab same window 'in query and 'open new tab' in query: 
    pyautogui.keyDown("ctrl")
    keyboard.press(" t")  
    keyboard.release('t')
    pyautogui.keyUp("ctrl")

#Reopen previously closed tabs in the order they were closed	Ctrl + Shift + t  
 elif 'open 'in query and 'previous tab' in query and 'close' in query: 
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("shift")
    keyboard.press(" t")  
    keyboard.release('t')
    pyautogui.keyUp("shift")  
    pyautogui.keyUp("ctrl")
    
#jump to the next open tab	Ctrl + Tab or Ctrl + PgDn
 elif 'next 'in query and 'open tab' in query and 'go to next tab': 
    pyautogui.keyDown("ctrl")
    keyboard.press(" tab")  
    pyautogui.keyUp("ctrl") 
 #Jump to the previous open tab	Ctrl + Shift + Tab or Ctrl + PgUp   
 elif 'previous tab 'in query and 'go to previous open tab' in query: 
    pyautogui.keyDown("ctrl")
    keyboard.press(" tab")  
    pyautogui.keyUp("ctrl") 
'''


Jump to a specific tab	Ctrl + 1 through Ctrl + 8
Jump to the rightmost tab	Ctrl + 9
Open your home page in the current tab	Alt + Home
Open the previous page from your browsing history in the current tab	Alt + Left arrow
Open the next page from your browsing history in the current tab	Alt + Right arrow
Close the current tab	Ctrl + w or Ctrl + F4
Close the current window	Ctrl + Shift + w or Alt + F4
Minimize the current window	Alt + Space then n
Maximize the current window	Alt + Space then x
Quit Google Chrome	Alt + f then x
'''