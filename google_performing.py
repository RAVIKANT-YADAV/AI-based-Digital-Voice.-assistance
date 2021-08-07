# Performing google search using Python code
import takeCommand as TC 
import speak_Function as sf 
import webbrowser
class Gsearch_python:
   def __init__(self,name_search):
      self.name = name_search
   def Gsearch(self):
      count = 0
      try :
         from googlesearch import search
      except ImportError:
         print("No Module named 'google' Found")
      for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=1,pause=2):
         count += 1
         #print (count)
         #print(i + '\n')
         sf.speak("Your websites is opening.....\n What is Next Command  ")
         webbrowser.open(i)
if __name__=='__main__':
   sf.speak("Witch Website want you sir  ")
   query = TC.TakeCommand()
   gs = Gsearch_python(query)
   gs.Gsearch()