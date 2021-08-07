import webbrowser as web
import time
import keyboard
import speak_Function as sf
import takeCommand as TC
import System_Status as S_status


def find_name(query):
    query = query.replace("whatsapp", "")
    query = query.replace("send message", "")
    query = query.replace("whatsapp message to", "")
    name=query
    sf.speak(f"What are the massege {name}:")
    return query

def find_number():
    number="7088555189"
    #with open("data.cvc",'r') as number_file:# A file that content multiplae whatspp no and name    
    #content=number_file.readlines()
    # number
    # 
    # 
def whatsapp(number,message):
    numb = '+91' + number
    open_chat = "https://web.whatsapp.com/send?phone=" + numb + "&text=" + message
    time.sleep(3)
    web.open(open_chat)
    time.sleep(30)
    keyboard.press('enter')
    sf.speak(" Please wait, I am sending.... ")


def Whatsapp_Groups(group_id , message):
    open_chat = "https://web.whatsapp.com/accept?code=" + group_id
    web.open(open_chat)
    time.sleep(30)
    keyboard.press('enter')
    time.sleep(3)
    keyboard.write(message)
   # time.sleep(1)
    keyboard.press('enter')


number = '7088555189'# find_number().number
message ="https://www.javatpoint.com/python-variables "

def send_message(query):
  if S_status.connect():
    if 'singal' in query or 'now'  in query:
        whatsapp(number,message)
        
    elif 'group 'in query and 'groups' or 'now' in query:
             
             # group_id juast like  mobile no Go to excal data sheet and 
             # take group name or person name and find number orid
             # Whatsapp_Groups(group_id , message)  
             Whatsapp_Groups(number, message) 
    else:
            sf.speak('sorry i am unable to take screenshot')    
  else:
      sf.speak('Sorry sir, i am not connected to internet ')























'''
def whatsapp(number,message):
    numb = '+91' + number
    open_chat = "https://web.whatsapp.com/send?phone=" + numb + "&text=" + message
    web.open(open_chat)
    time.sleep(40)
    keyboard.press('enter')
    sf.speak(" Please wait, I am send.... ")

def Whatsapp_Groups(group_id , message):
    open_chat = "https://web.whatsapp.com/accept?code=" + group_id
    web.open(open_chat)
    time.sleep(15)
    keyboard.press('enter')
    time.sleep(3)
    keyboard.write(message)
    time.sleep(1)
    keyboard.press('enter')

def find_name(query):
    query = query.replace("whatsapp", "")
    query = query.replace("send message", "")
    query = query.replace("whatsapp message to", "")
    name=query
    sf.speak(f"What are the massege {name}:")
    

def find_number():
    number="7088555189"
    #with open("data.cvc",'r') as number_file:# A file that content multiplae whatspp no and name    
    #content=number_file.readlines()
    # number
    # 
    # 

if __name__ == '__main__':
    query=TC.TakeCommand().lower()
    #query=module.TC.TakeCommand().lower()
    number='7088555189'
    find_name(query)
    #message=module.TC.TakeCommand()
    message=TC.TakeCommand()
    whatsapp(number,message)
'''