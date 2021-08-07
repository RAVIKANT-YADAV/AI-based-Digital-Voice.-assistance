import os
import sys
import speak_Function as sf
import takeCommand as TC


#********************************************************************************************************************************************#
#*********************************************************************** . Query for stop Anas *****************************************#
 
def main(query): 
 if 'Create floder' in query or 'in cureent' in query or 'same' in query :               
       if 'any other loction' in query or 'diffrent location' in query:
              CreateFolderAnyware() 
              return 
       else:
            print('')   
 CreateFolderHear()
 return

           
#********************************************************************************************************************************************#
#########################################################################################
####                       Create Folders
#########################################################################################
# 1.CraetePrijectDir()
# 2.
# 3.
# 4.                
#########################################################################################

def find_root():
        sf.speak("Please Tell me location  Like. desktop Downlode or any other drive'''")
        path=TC.TakeCommand_conf()
        
        if 'd'in path or 'd drive' in path or 'd folder' in path:
           path=os.chdir("D://")
        elif 'desktop'in path :
           path=os.chdir("dsktop")
        elif 'c'in path or 'c drive' in path or 'c folder' in path:
            path=os.chdir("c://")
        else :
            return 0
        print(path)    
        
def serch_folder(name):
    root="."

def CreateFolderHear():
    root="."
    folderCreat_name (root)
    
def CreateFolderAnyware():
    sf.speak("Please Tell me location Like desktop or any other drive'''")
    path=TC.TakeCommand()
    path=path.lower()
    if path !=0:
        if 'd'in path or 'd drive' in path or 'd folder' in path:
           root=os.chdir("d://")
           folderCreat_name(root)
           return
        elif 'desktop'in path :
          root=os.chdir("dsktop")
          folderCreat_name(root)
         
    
        elif 'c'in path or 'c drive' in path or 'c folder' in path:
           root=os.chdir("c://")
           folderCreat_name(root)
        
    else:
        sf.speak("Sorry Folder is not created Try again")
        CreateFolderAnyware()



def folderCreat_name (root):
    sf.newspeak("Please tell Me folder name : ")
    folderName=TC.TakeCommand()
    path=path=f"{root}/{folderName}".lower().replace("","")
    if not os.path.exists(path):
        os.makedirs(path)
        print("Folder Is created It's Name is :",folderName)
        sf.speak("Folder Is created It's Name is :"+folderName+"")
    else:
        print("folder Name Allredy Exists")
        sf.speak("Folder Name Allready Exists")
        sf.speak("What i do now May i delete old file and create new folder")
        path=TC.TakeCommand() 
        if 'and create'in path or 'remove and create'in path :
            ver=TC.TakeCommand()
            if 'yes'in ver:
              os.remove(path)
              os.makedirs(path)
              print("Old Folder Deleted And New Folder Is created It's Name is :"+folderName+"")
              sf.speak("Old Folder Deleted And New Folder Is created It's Name is :"+folderName+"")
            else:
               print('Folder not Created ')
               sf.speak('Folder not Created' )
          
        if path!='none':
          os.makedirs(path)
          print("Old Folder Deleted And New Folder Is created It's Name is :"+folderName+"")
          sf.speak("Folder Is created It's Name is :"+folderName+"")
        else : 
            print("Sorry Iam  unable Create folder try again ")
            sf.speak("Sorry unable Create folder try again ")

       




def CraetePrijectDir():
 root="."
 project="Anas"
 level="assese"
 type="chareter"
 name="body"
 task="design"
 e=1
 for e in range(50):
    path=f"{root}/{project}/{level}/{type}/{name}_{e}/{task}".lower().replace("","")
    print(path)
     
    if not os.path.exists(path):
         os.makedirs(path)
    else:
         os.remove(path)   






def openExplorer():  
  os.system('explorer')


def OpenFolder(query):
    root="."
    if 'open folder' in query:
         os.startfile(root)
    


def showAllAtiveTask():
    task=os.system('tasklist')    


    

   

if __name__ == '__main__':

    
    #OpenFolder(query)
    showAllAtiveTask()
    


#********************************************************************************************************************************************#
#########################################################################################
####                      
#########################################################################################
# 1.CraetePrijectDir()
# 2.
# 3.
# 4.                
#########################################################################################