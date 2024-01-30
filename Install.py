import sys
import importlib
import os



"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Set The Name Of My Folder For My Addons
addonfolder="Vonas-Maya-Plugins"
pluginlocationtextfolder_loc="pluginlocation.txt"
addonfolderpath = ""
"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Setup Definitions
def initialisepluginlocation(filepath):
    print(filepath)
    filepath_to_check = filepath
    if filepath_to_check not in sys.path:
        print("Adding "+filepath_to_check+" to python\n")
        sys.path.append(filepath_to_check)
        overwritefile(filepath_to_check)
    #Informing that the filepath already exists
    if filepath_to_check in sys.path:
        print("Filepath is already in python\n")

def readpluginlocation(pluginlocation):
    plugin_filepath = addonfolderpath+pluginlocation
    with open(plugin_filepath  , "r") as instfileloc:
        readfilecontents = instfileloc.read()
        print(readfilecontents)
        return(readfilecontents)

def overwritefile(filetooverride):
    #addonfolderpath = addonfolderpath+pluginlocationtextfolder_loc
    with open(filetooverride,"w") as f:
        f.write(filetooverride)
    print(filetooverride)
#J:/Vonas Maya Scripts/
def gatherfilepath():
    basefilepath = str(input("Please specify the filepath to this folder \n eg - J:/Vonas Maya Scripts/VonTools - \n")) 
    basefilepath_end = basefilepath.endswith("/" or strip(' \ '))
    basefilepath_finalchar = len(basefilepath) -1

    if basefilepath_end == True: #if the final character is either \ or /
        addonfolderpath = basefilepath + addonfolder
        addonfolderpath = addonfolderpath+"/"
        return(addonfolderpath)

    
    if basefilepath_end == False: #if the final character is not either \ or /
        basefilepath = basefilepath+"/"
        addonfolderpath = basefilepath + addonfolder
        addonfolderpath = addonfolderpath+"/"
        return(addonfolderpath)
"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Force Maya To Recognise The Fucking Files Exist Every Time I Open It Again
addonfolderpath = gatherfilepath() # Set the filepath to all of my .py files for all definitions

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

initialisepluginlocation(addonfolderpath)
temp = addonfolderpath+pluginlocationtextfolder_loc
overwritefile(temp)

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Open The Menu
importlib.import_module("menu")
import menu
"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
