"""

Script Editor Tab Content Backup GUI

This code will open a window that will allow user to select where to save the ZIP file gereated in seBackup.py.

This only backs up the script editor tab content for the version of Maya in which it is run.

Copy this code onto your Maya shelf for easy access.


"""

import maya.cmds as mc
import seBackup as seb
from PySide import QtCore, QtGui

class scriptsBackup():
    def __init__(self):
        
        if mc.window('scrBckup', exists = True): 
            mc.deleteUI('scrBckup') 
        
        self.backupWindow = mc.window( 'scrBckup', t = "Script Editor Backup", iconName = 'Script Editor Backup', w = 250 )
        mc.rowColumnLayout( nc = 1, cal = [1, 'left'], rs = [1, 7], cs = [1, 20], cw = [1, 200] )
        
        mc.separator( st = 'none', h = 17 )
        
        mc.text( label='This tool allows you to backup \n the content in the Script Editor \n tabs to a zip file and save it to \n a destination of your choice.' )
        mc.button( l = 'Select Directory to Save Zip File', c = self.selectDestination, w = 50 )
        
        mc.separator( h = 25, st = 'in' )
        
        mc.text( label='After you have selected a location, \n click the button below to create \n the zip file.' )
        mc.button( l = 'Create Zip File', c = self.getCurrentVersion, w = 50 )
        
        mc.separator( h = 25, st = 'in' )
        
        mc.button( l = 'Close Window', c = self.closeWindow, w = 50 )
        
        mc.separator( st = 'none', h = 17 )
        
        mc.showWindow( )
        
        
        
    def selectDestination(self, *args):
        self.scriptDir = QtGui.QFileDialog.getExistingDirectory()

    
    def getCurrentVersion(self, *args):
        # Get Version of Maya in which this script is being run. 
        self.currentVersion = mc.about(v=True)
        
        # Gets the name of the Installation version (2015 vs 2015-x64)
        self.mayaVersion = seb.seBackup().getInstalledMayaVersions(self.currentVersion)
        
        # Backs up Script Editor files
        seb.seBackup().scriptEditorBackup(self.mayaVersion, self.scriptDir)  
        
    def closeWindow(self, *args):
        mc.deleteUI(self.backupWindow, wnd = 1)
            

window = scriptsBackup()

# import seBackup as seb
# seb.seBackup().scriptEditorBackup()
