from pytube import YouTube #The module Youtube  for downlode any video from youtube 
import webbrowser          # The Module WebBrowser Is use for browsering anything on browser 
import takeCommand as TC   # userDefine module for tackeing command from user in voice mode  
import speak_Function as sf # 
import urllib.request
import urllib.parse
import re
def Play_youtube_query(query): 
      sf.speak("Playing............")
     # query= query.replace("youtube play on ","")
      query_string = urllib.parse.urlencode({"search_query" : query})
      html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
      search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
      webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])  
      sf.speak("youtube is Open Enjoy with Youtube \n what is  next Command sir,  ")

def search_youtube_query(query) :  
       sf.speak("Searching............") 
       query = query.replace("on youtube","")
       webbrowser.open("https://youtube.com/search?q=%s" % query)
       sf.speak("youtube is Open Enjoy with Youtube \n next Command sir,  ") 

def downlode_youtubeVideo_query(query):
      query_string = urllib.parse.urlencode({"search_query" : query})
      html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
      downlode_Link= re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
      sf.speak("Downlodeing............")
      webbrowser.open("http://www.youtube.com/watch?v=" + downlode_Link[0])  

if __name__ == "__main__":
        
        sf.speak("What do u want to On youtube ")
        query = TC.TakeCommand().lower()
        
        if 'search' in query :
            search_youtube_query(query)
        elif 'play' in query:
            Play_youtube_query(query)
        elif'downlode' in query:
            downlode_youtubeVideo_query(query)         
