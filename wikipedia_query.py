from audioop import ulaw2lin
from sys import implementation
import speak_Function as sf
import wikipedia
import takeCommand as TC

def wikipedia_query(query):
     #if 'wikipedia' in query:
        sf.speak("Searching............")
        query = query.replace("wikipedia", "")
        results =  wikipedia.summary(query, sentences=2)
        sf.speak("According to wikipedia")
        print(results)
        sf.speak(results)
if __name__ == "__main__":
 query=TC.TakeCommand()
 wikipedia_query(query)