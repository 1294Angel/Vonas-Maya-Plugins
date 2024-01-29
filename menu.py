import sys
import importlib
from maya import cmds
import webbrowser

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
from pizzaops import fireawaypizza


"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""


window_ID = 'Vona_Tools'

#If the window is already open, close it
if cmds.window (window_ID, exists=True):
    cmds.deleteUI(window_ID)
#Open the window
cmds.window(window_ID)

#Contents of the window
cmds.rowColumnLayout()
cmds.button(label='Fireaway Pizza', command=fireawaypizza())
cmds.button()

cmds.showWindow(window_ID)

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""