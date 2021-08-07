from genericpath import isfile
from pandas.core.construction import is_empty_data
from pyautogui import scroll
import speak_Function as sf
import wikipedia_query as wq
import takeCommand as TC
import speech_recognition as sr
import wish as WS
import Ravistudy1 as Study
import weather as we
import whatsapp as whatsapp
import System_Status
import Mail
import System_Task as ST
import google_query1 as gq
import addNewQuery as anq
import webbrowser
import datetime
import sys
import os
import pandas as pd
import time
from Youtube_Query import search_youtube_query,Play_youtube_query

'''
command=pd.read_excel("Files//Command.xlsx")
screenshot_col=command.get('screenshot')
screenshot=list(screenshot_col)
 ''' 

#********************************************************************************************************************************************#
#*********************************************************************** . Query for stop Anas *****************************************#
WS.wish()
while True:       
    query = TC.TakeCommand().lower()  
    if 'screenshot' in query :
        ST.screenshot(query)                
#********************************************************************************************************************************************#
#                 OPEN AND CLOSE APPLICTION
#********************************************************************************************************************************************#
    if 'app' in query or 'application' in query or 'software' in query:
         ST.OpenCloseApps(query)
  
    elif 'explorer' in query or 'drive' in query: 
        if 'open' in query:           
          os.system('explorer')
          time.sleep(1)
          print(" opening")
          os.system('notepad.exe')
        elif 'close' in query: 
            time.sleep(1)
            os.system('taskkill/im explorer.exe')
#########################################################################################
#                         SHOUTDOWN
#########################################################################################
    elif 'shutwodn' in query or  'power of 'in query or 'shut down' in query :
            ST.shutdown()

    elif 'lock my pc'   in query or 'lock my leptop 'in query or 'lock my device' in query or 'off my pc' in query or 'signout my pc '   in query:
         ST.lockpc()

#########################################################################################
#                         Task perform only internet connection avilable 
#########################################################################################
    elif 'whatsapp' in query or  'power of 'in query or 'shut down' in query :
        whatsapp.whatsapp()     

    elif 'email'   in query or 'send mail 'in query or 'gmail' in query :
         Mail.send_mail(query) 

    elif 'google' in query or  'power of 'in query or 'shut down' in query :
        whatsapp.whatsapp()     
               
    elif 'website'   in query or 'send mail 'in query or 'gmail' in query :
         Mail.send_mail(query)          