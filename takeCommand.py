import speech_recognition as sr
import speak_Function as sf
#import check_exetion_time as check_time
#import numba 

def TakeCommand():   
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("\nListening....")
       r.pause_threshold = 0.5
       r.phrase_threshold = 0.2   # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
       r.non_speaking_duration = 0.2 
       audio=r.listen(source)
    try:
         print("Recognizing....")
         query = r.recognize_google(audio,language='en-in') 
         sf.changeVoice(query)
         print(f"User said :{query}\n")
        
       
    except Exception as e:
          print(e)
          print ("Say that again plese ........")
          return 'none'
    return query 

def  TakeCommand_conf():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("\nListening....")
       r.pause_threshold = 0.5
       r.phrase_threshold = 0.8 # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
       r.non_speaking_duration = 0.2 
       audio=r.listen(source)
          
       try:
          print("Recognizing....")
          query = r.recognize_google(audio,language='en-in') 
          print(f"User said :{query}\n")
       except Exception as e:
          print(e)
          print ("Sorry! I'm not understand   Please say Again ........")
          sf.speak ("Sorry! I'm not understand   Please say Again ........")
          return 0 

       return query  



if __name__ == "__main__":
   query= TakeCommand()
   sf.speak("now your voice is change ")
  