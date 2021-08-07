import webbrowser
import takeCommand as TC
import speak_Function as sf

# secah on google and open it on chreom
def google_search_Que(query):   
        query= query.replace("google","")
        query= query.replace("on","")
        query= query.replace("search","")
        webbrowser.open("https://google.com/search?q=%s" % query)
        sf.speak("you command is open \n now what i do sir ")  

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

def SearchFromGoogle (query):
    import wikipedia as googleScrap
    query= query.replace("google","")
    query= query.replace("on","")
    query= query.replace("tell","")
    query= query.replace("","")
    query= query.replace("search","")
    query= query.replace("on","")
    query= query.replace("search","")
    query= query.replace("on","")
    query= query.replace("search","")
    try:
      
       googleScrap.search(query)
       result=googleScrap.summary(query,1)
       print(result)
       sf.speak(result)
    except:
       print("Sorry i am Unable to search Try again ")  
       sf.speak("Sorry i am Unable to search Try again ")   

if __name__ == "__main__":
    sf.speak("How i can help you sir  :")
    query = TC.TakeCommand().lower()
    SearchFromGoogle(query)
    