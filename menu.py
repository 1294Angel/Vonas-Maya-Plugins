import sys
import importlib
from maya import cmds
import webbrowser

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Importing required definitions from python files

#from pizzaops import fireawaypizza # 01
from scriptrunner import runscriptfile #02
from scriptrunner import checkandaddfilepath #03

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Setting Up Button Commands


"""def fireawaypizza_button_01():
    fireawaypizza()"""
def runscriptfile_button_02():
    runscriptfile()
def checkandaddfilepath_button_03():
    checkandaddfilepath()



"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
def menu_createwindow():
    window_ID = 'Vona_Tools'

    #If the window is already open, close it
    if cmds.window (window_ID, exists=True):
        cmds.deleteUI(window_ID)
    #Open the window
    cmds.window(window_ID)

    #Contents of the window
    cmds.rowColumnLayout()
    #cmds.button(label='Fireaway Pizza',align='center', command="fireawaypizza_button_01()")
    cmds.button(label='Run Custom Script', command="runscriptfile_button_02()")
    cmds.button(label='Setup Python Script Folder', command="checkandaddfilepath_button_03()")


    cmds.showWindow(window_ID)

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
menu_createwindow()