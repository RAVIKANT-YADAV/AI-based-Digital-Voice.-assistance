import takeCommand as TC
import webbrowser
import speak_Function as sf
import os 
import datetime


def six_sem_subject(query):
   if 'compiler design'in query or 'compiler ' in query or 'design'in query:
       compiler_design()
   elif 'computer graphic' in query:
       computer_Graphic()
   elif 'computer network' in query:
       computer_network()
   elif 'datawarehousing ' in query  or  'Data Mining 'in query:
       data_mining()
   elif 'python' in query:
       python()
   elif'english'in query:
        english()   
   elif'ai'in query or 'ai project'in query or 'anas 'in query or 'project' in query:  
       project() 
   else:
       sf.speak("This not your Syllabus \n Thanku What is nexr comand sir ")   
        
def call_function():
   while True:
     sf.speak("What du u want to Study at this time")
     query = TC.TakeCommand().lower()
     six_sem_subject(query)

def python():
    webbrowser.open("https://onlinecourses.swayam2.ac.in/cec20_cs04/announcements")
    webbrowser.open("https://onlinecourses.nptel.ac.in/noc20_cs46/announcements")
    webbrowser.open('https: //www.udemy.com/course/python-the-complete-python-developer-course/learn/lecture/17021268#overview')
def english():
    webbrowser.open('')
    sf.speak("Link not found please ")
def project():
    webbrowser.open("https://swayam.gov.in/mycourses")
    path='C:\\Users\\Aarti singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
    os.startfile(path)
def compiler_design():
    webbrowser.open("https://onlinecourses.nptel.ac.in/noc20_cs13/announcements")
    webbrowser.open("https://www.youtube.com/watch?v=XGc-HeXOJnw&list=PL-JvKqQx2Ate5DWhppx-MUOtGNA4S3spT&index=2")
    sf.speak("please study 2 hour Compiler Design \n Your Target is complete in before 3 march  Thanku ")
  
def computer_Graphic():
    webbrowser.open("https://swayam.gov.in/mycourses")
    webbrowser.open("https://www.youtube.com/watch?v=fwzYuhduME4&list=PL338D19C40D6D1732")
    sf.speak("please study 2 hour computer Graphic \n Your Target is complete in before 3 march  Thanku ")

def computer_network():
    webbrowser.open("https://onlinecourses.nptel.ac.in/noc20_cs23/course?user_email=rdntechinfo@gmail.com")
    sf.speak("please study 2 hour computer Graphic \n Your Target is complete in before 3 march  Thanku ")
def data_mining():
    webbrowser.open("https://universityacademy.co.in/courses/data-warehousing-and-data-mining/")
    sf.speak("please study 2 hour computer Graphic \n Your Target is complete in before 3 march  Thanku ")


if __name__ == "__main__":
    hour = int(datetime.datetime.now().hour)
    call_function()
  
