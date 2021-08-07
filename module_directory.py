import speak_Function as sf
import takeCommand as TC

def Module_directory():
  sf.speak("Plases tell me Module Name")
  x=TC.TakeCommand()
  all_dir= dir(x)
  
  sf.speak("Directory of module  are :\n" )
  print("All directroy of module {x} is  hear :\n",all_dir)
  #sf.speak(all_dir)
# Example
if __name__ == '__main__':
    sf.speak("This Module is make for  Find all directory of any module \n ! ")  
    Module_directory()