from math import log
import smtplib,ssl
import takeCommand as TC
import speak_Function as sf
import Read_Write_in_File as Rd
import Number_Emails as datas
import pandas as p
import datetime as dt
import re
import time
import check_internet_Connection as connection


data = p.read_excel("Files//Email_numbers.xlsx")# read data from data file here that is a excal file 
email_col=data.get('Email')
Emails=list(email_col)


def login():
 if connection.connect() :
   sender_email="maill.iitdeveloper@gmail.com"
   password="RK@900#900"
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.starttls()
   server.login(sender_email,password) 
   print('Loging...')
   return server
 else:
  sf.speak('Sorry sir, you are not connected to internet ')
 # set connection with your gmail singal persons    

def singal_mail_now(message):
  try:
     server=login()
     sender_email='mail.iitdeveloper@gmail.com'
     rec_email='rdntechinfo@gmail.com'
     server.sendmail(sender_email,rec_email,message)
     sf.speak("Massage is sent.  Thanks for Using")
     print("Massage is sent  \n Thanks for Using! ")
  except Exception as e:
     print(e)
  finally:
    server.quit() 
    
def bulk_mail_now(message):
    list_of_email=Emails
    senderemail='mail.iitdeveloper@gmail.com'
    server=login()
    server.sendmail(senderemail,list_of_email,message)
    sf.speak("Massage is sent.  Thanks for Using")
    print("Massage is sent.   Thanks for Using! ")
   

def singal_schedule_email(message):
        set_time()  
        singal_mail_now(message)
       

def bulk_schedule_mail(message):
    set_time()
    bulk_mail_now(message)
  

def set_time():
    y=2021
   # sf.speak("Which month ?")
   # m=TC.TakeCommand()
   # m=int(m)     
    m=int(input("Which month :"))
    d=int(input('Tell me date:')) 
    h=int(input("witch O'clock : "))
    mi=int(input('Minute :'))
    s= 00
    send_time=dt.datetime(y,m,d,h,mi,s)
    print(send_time.timestamp())
    print(time.time())
    if send_time.timestamp()<=time.time():
      print("You are tring to Enter past Date. please Enter Future date: ")
      set_time()
    else:
        x=time.sleep(send_time.timestamp()- time.time())    
        return x;

def TakeData():
  subject='Teting for ANAS'
  body='this massage send by ANAS autometic '
  message='Subject:{}  \n \n{}'.format(subject,body)
  return message

def find_user_name(email):
 try:
        eReg = "(\w+)@((\w+\)+(com))"
        r=re.match(eReg,email)
        print (r.group(1))
        print (r.group(2))

 except Exception as e:
     print(e)
def send_mail(query):
 if connection.connect() :# chack connection isdone or not 
  message=TakeData()
  #########################################################
  if 'singal' in query or 'singal'  in query:
          singal_mail_now(message)
          return
    
  elif 'bulk 'in query and 'multiple screenshot' or 'more then one' in query:
          bulk_mail_now(message) 
          return

  elif 'singal'in query and 'schedul' in query:
          singal_schedule_email(message)
          return

  elif 'bulk'in query or 'schedul' in query:
           bulk_schedule_mail()
           return

  else:
            sf.speak('Sorry sir  i am unable to send mail Please try again')  

 else:
   sf.speak('Sorry sir, you are not connected to internet ')



find_user_name('sharmasushma051@gmail.com')