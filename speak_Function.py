import pyttsx3
import takeCommand as TC

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def newspeak(audio):  
  engine.setProperty('voice', voices[2].id)  
  engine.setProperty('volume', 0.7)
  engine.setProperty('voice', voices[0].id)
  engine.setProperty('rate',150)
  engine.say(audio)
  engine.runAndWait()
  

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def changeVoice(query):
 if 'change voice'in query or 'change my voice'in query:
  if'female'in query:
    voice_id=2
  elif 'male' in query: 
    voice_id=1
  engine.setProperty('voice', voices[voice_id].id)  
  speak('Enjoy with new voices ')
  return voice_id
  

def ChangeVoceByName():#change voice by name when enter name go to VoiceId function for geting is no
    speak('please tell me name')
    ver=input('Enter name')
    check=VoiceId()# call function for geting voice Id 
    if check!=0:
      engine.setProperty('voice',check) # Set setProperty of engin help of voice id  
      engine.say("Now My Voice is changed. Enjoy with my new voice." )
      engine.runAndWait()
    else:
      return 0
    
  
def VoiceId(name):
  if 'hazel'in name:
    voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
  elif'ravi' in name: 
    voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_HemantM'
  elif 'sushma'in name:
    voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM'
  elif'susan' in name: 
    voice_id='ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enGB_SusanM'
  elif 'susan'in name:
    voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
  else:
    return 0 

  return voice_id  
  
def CheckAllVoice():
  voices = engine.getProperty('voices')
  i=0
  for voice in voices:
    # to get the info. about various voices in our PC 
    print("Voice:")
    print("ID: %s" %voice.id)
    print("Index no: %s" %i)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages)
    engine.setProperty('voice',voice.id) 
    voice.name=voice.name.replace("Microsoft","")
    print("Hey sir i am"+voice.name)
    engine.say("Hey sir i am"+voice.name)

    engine.runAndWait()
    i=i+1
    
  speak("total number of voice in your pc is  :"+str(i))

if __name__ == "__main__":
  # CheckAllVoice()
   #AllCheckVoice()
   #speak("change voice command")
   changeVoice('Change voice in  female voice')
   #ChangeVoceByName()