import speak_Function as sf
import wikipedia

def wikipedia_query():
     if 'wikipedia' in query:
        sf.speak("Searching............")
        query = query.replace("wikipedia", "")
        results =  wikipedia.summary(query, sentences=2)
        sf.speak("According to wikipedia")
        print(results)
        sf.speak(results)