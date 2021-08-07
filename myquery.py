import pandas
import speak_Function as sf
import wikipedia_query as wq
import takeCommand as TC
import speech_recognition as sr
import wish as WS
import Ravistudy1 as Study
import weather as we
import webbrowser
import datetime
import sys
import os
import google_query1 as gq
import addNewQuery as anq
from Youtube_Query import search_youtube_query,Play_youtube_query
import pandas as pd
import System_Task as ST
import FlolderFile as FF

def myquery():  
 while True:
    query = TC.TakeCommand().lower()
#********************************************************************************************************************************************#
#*********************************************************************** . Query for stop Anas *****************************************#
    if 'nothing' in query or 'abort' in query or 'stop' in query or 'sleep' in query or 'rest'in query:
            sf.speak('Bye Sir,You can call me any time.')
            break; 
    elif 'Bye'  in query:
           sf.speak('Have Good day. I am going to close my service Thanks to use my service')
           sys.exit()      
#    
#********************************************************************************************************************************************#
#*********************************************************************** 1. script for Search any thing on Google(google_queary1.py) **************************************# 
    elif 'google'in query:
          gq.google_search_Que(query)
# 
#***********************************************************************************************************************************************      
#*************************************************************************2.script for Search anything on Wikipedia (wikipedia_query.py) **************************************** 
    elif 'wikipedia' in query:
          wq.wikipedia_query(query)       
#
#**********************************************************************************************************************************************#
#*********************************************************************** 3. script for Search any thing on facebook (facebook_Queary.py) **************************************# 
   
# 
# #********************************************************************************************************************************************#
#*********************************************************************** 4. Script for Search any thing on Youtube and play (Youtube_Query.py) ******************************# 
    elif 'youtube'in query:
          if 'search'in query:
                search_youtube_query(query)
          else:
                Play_youtube_query(query)
#          
#********************************************************************************************************************************************#
#*********************************************************************** 5. Script for opening any websites ( google_queary1.py)*****************************************#
    elif 'website' in query :
            gs = gq.Gsearch_python(query)
            gs.Gsearch()
    
#********************************************************************************************************************************************#
#*********************************************************************** 6.  Other Queary ( google_queary1.py)*****************************************#
    elif 'want to study' in query:
            sf.speak("What du u want to Study at this time")
            query = TC.TakeCommand().lower()
            Study.six_sem_subject(query)
    
#
#
# **************************************** 1. for opening any Operting System file or application ***********************************************
    elif'play music' in query:
          music_dir= 'C:\\Users\\Aarti singh\\Music\\2015'
          songs=os.listdir(music_dir)
          os.startfile(os.path.join(music_dir,songs[0]))
 
    elif 'open anydesk' in query :
          path="C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe"
          os.startfile(path)
    elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          sf.speak(f"Sir the time is {strTime}")

    elif 'open visul code' in query:
          path='C:\\Users\\Aarti singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
          os.startfile(path)
          sf.speak("Visul code is open enjoy with coding sir ")  
    elif 'open chrome' in query  :
          path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
          os.startfile(path)
          sf.speak("Google Chrome  is open  \n What is next command sir ")
          


#********************************************************************************************************************************************#
#*********************************************************************** 5. Current Wether Report  *****************************************#
    elif 'weather' in query :
          we.watherreporter()
            
    elif 'screenshot' in query  :
          ST.screenshot(query)
    elif 'folder' in query and 'create' in query :
           FF.main(query) 
#********************************************************************************************************************************************#
#*********************************************************************** 6.  *****************************************#
    
     