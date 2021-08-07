import takeCommand as tc 
import speak_Function as sf


import os

def read(filePath):

 with open(filePath, 'r') as file1:
  content=file1.readlines()
  #print(content) 
  #sf.speak(content)


def write():
 with open("data.txt","a") as file1: # write data in a file in append mode.
  addNew = tc.TakeCommand().lower()
  l1=input("Enter your new massase")
  
  file1.write('\n')        # \n is placed to indicate EOL (End of Line)
  file1.writelines(l1)
  file1.writelines(addNew)

  

if __name__ == "__main__":
   read('email.txt')
   #write()#

 #os.system("C:\\Windows\\notepad.exe")   

 