import takeCommand as TC
import webbrowser
import speak_Function as sf

def six_sem_subject(query):
  
   if 'compiler design'in query or 'compiler ' in query or 'design'in query:
       webbrowser.open("https://www.youtube.com/watch?v=XGc-HeXOJnw&list=PL-JvKqQx2Ate5DWhppx-MUOtGNA4S3spT&index=2")
       sf.speak("please study 2 hour Compiler Design \n Your Target is complete in before 3 march  Thanku ")

   if 'computer graphic' in query:
       webbrowser.open("https://www.youtube.com/watch?v=fwzYuhduME4&list=PL338D19C40D6D1732")
       sf.speak("please study 2 hour computer Graphic \n Your Target is complete in before 3 march  Thanku ")

   if 'computer network' in query:
       webbrowser.open("https://www.youtube.com/watch?v=fwzYuhduME4&list=PL338D19C40D6D1732")
       sf.speak("please study 2 hour computer Graphic \n Your Target is complete in before 3 march  Thanku ")

   if 'datawarehousing ' in query  or  'Data Mining 'in query:
       webbrowser.open("https://www.youtube.com/watch?v=fwzYuhduME4&list=PL338D19C40D6D1732")
       sf.speak("please study 2 hour computer Graphic \n Your Target is complete in before 3 march  Thanku ")
def extra(query):
    if 'python' in query:
        webbrowser.open('https://www.udemy.com/course/python-the-complete-python-developer-course/learn/lecture/17021268#overview')

if __name__ == "__main__":
    sf.speak("What du u want to Study at this time")
    query = TC.TakeCommand().lower()
    six_sem_subject(query)

