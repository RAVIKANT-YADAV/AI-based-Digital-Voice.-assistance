import webbrowser
import takeCommand as tc 
import speak_Function as sf

def search_profile_query(query):
      sf.speak("Searching ............")
      query=query.replace("search","")
      query=query.replace("on","")
      query=query.replace("facebook","")
      query=query.replace("profile","")
      webbrowser.open("https://www.facebook.com/search/top/?q=" + query)  
      sf.speak("profile is opeing  \n what is  next Command sir,  ")       
 
if __name__ == "__main__":
     sf.speak("what do tou wnat on facebook")     
     query = tc.TakeCommand().lower()
     search_profile_query(query)





    # https://www.facebook.com/search/top/?q=sushma