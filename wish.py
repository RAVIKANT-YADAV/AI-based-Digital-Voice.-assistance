import speak_Function as sf
import datetime
def wish():
    hour=datetime.datetime.now().hour
    if hour >=0 <= hour < 12:
        sf.speak("Good morning")
    elif hour >= 12 and hour < 18:
       sf.speak("Good Afternoon !")
    else:
        sf.speak("Good Night dear sushma   ")
    sf.speak("I'm an AG3 ASSISTANT, can I help you Sir?.")


if __name__ == "__main__":
     sf.speak(" This Module is made for  wish  to sting of the program  according to time \n ! ")  
     sf.speak("I'm an AG3 ASSISTANT,dear sir, have any orders for me?")
     wish()
         
    
   



