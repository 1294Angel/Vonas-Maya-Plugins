import sys
import importlib


filepath_to_check = ""
scriptfile_to_run = ""



"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Setting Up Definitions

#Folder Additions
def collectfilepath():
    #Gathering Filepath Destination
    userinput_filepath = str(input("Please Paste Required Filepath\nFor Example: J:/Vonas Maya Scripts/Vonas-Maya-Plugins/ \n"))
    #Setting as global variable
    return(userinput_filepath)

def checkandaddfilepath(userinput_filepath):
    #Checking whether or not the filepath is already in pythons directories --- To avoid putting a TON of the same filepath in -- Allows this to be used as a double check as well
    filepath_to_check = collectfilepath()
    if filepath_to_check not in sys.path:
        print("Adding "+filepath_to_check+" to python\n")
        sys.path.append(filepath_to_check)
    #Informing that the filepath already exists
    if filepath_to_check in sys.path:
        print("Filepath is already in python\n")


#Script Running
def collectscriptfile():
    #Gathering The Name Of The Script To Run
    userinput_scriptfile = ""
    userinput_scriptfile = str(input("Please Paste Required File Name"))
    return(userinput_scriptfile)

#attempting to run the script file
def runscriptfile():
    scriptfile_to_run = collectscriptfile()
    print("\nRunning --"+scriptfile_to_run+"--\n")
    #Running a script 
    module = importlib.import_module(scriptfile_to_run)



"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Actual Running Script
"""
print("\n-\n-\n-\n-\n-\n-")

question_addfile = str(input("Would you like to add a file directory? (y/n)\n"))
#If they want to add a file then run the proper definitions
if question_addfile != "y":
    print("No File Directory Needs Adding \n")
else:
    checkandaddfilepath()


question_runscript = str(input("Would you like to run a script? (y/n) \n"))
#if they want to run a script run the proper definitions
if question_runscript != "y":
    print("No Script Needs Running \n")
else:
    runscriptfile()
"""
#J:/Vonas Maya Scripts/Vonas-Maya-Plugins/
#VonTool_1