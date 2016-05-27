"""

Script Editor Tab Content Backup

Save this file to your maya/scripts directory. To find this directory print the following code:

import os
os.environ['MAYA_APP_DIR'] + '/scripts/'


"""
import maya.cmds as mc
import os
import os.path
import zipfile
import datetime
import re

class seBackup(object):

    def __init__(self):
        pass
    
    def scriptEditorBackup(self, mayaVersion = None, directory = None):
        
        if mayaVersion:
            self.mayaVersions = mayaVersion # If provided, use specific version of Maya
        else:
            self.mayaVersions = self.getInstalledMayaVersions() # If not provided, get all versions of Maya

        # If a directory is not otherwise specified, Get user scripts directory
        if directory:
            self.scriptDirector = directory + '/'
        else:
            self.scriptDirector = os.environ['MAYA_APP_DIR'] + '/scripts/'
        
        print 'Destination: ' + self.scriptDirector

        # Gets date and time into a unique string
        pattern = r'(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})\.(\d+)'
        expression = re.compile(pattern)
        now =  expression.sub(r'\1\2\3\4\5\6', str(datetime.datetime.now()))
        
        # Versions and Location of script editor tabs
        self.scrEdTmpDir = {}
        for vers in self.mayaVersions:
            self.scrEdTmpDir[vers] = '%s/%s/prefs/scriptEditorTemp/' % (os.environ['MAYA_APP_DIR'], vers)
        
        
        # Create ZIP File
        for vers in self.mayaVersions:
            # name of zip file to be created
            tempZIP = '%smaya%s_scriptBackup_%s.zip' % (self.scriptDirector, vers, now)
            
            # all files in scriptEditorTemp
            files = os.listdir(self.scrEdTmpDir[vers])
            #print files
            
            # creates script file
            zf = zipfile.ZipFile(tempZIP, "w")
            
            for file in files:
                zf.write(self.scrEdTmpDir[vers] + file, file)
            
            zf.close()

            print 'Version: ' + vers
            print 'scriptEditorTemp Location: ' + self.scrEdTmpDir[vers]
            print 'ZIP File: ' + tempZIP

        print "Backup Successful!"

    
    def getInstalledMayaVersions(self, mayaVersion = None):
        
        # Get All directories in user Maya directory
        self.mayaDir = os.listdir(os.environ['MAYA_APP_DIR'])
        
        self.versions = []
        
        # Gets directory name for vurrent version (including -x64 if included)
        for dir in self.mayaDir:    
            if mayaVersion: # Specified version of Maya
                found = re.search(r'%s-?x?\d?\d?' % mayaVersion, dir) # match object        
                if found:
                    self.versions.append(found.group())
            else: # All installed versions of Maya
                found = re.search(r'\d{4}-?x?\d?\d?', dir) # match object
                if found:
                    self.versions.append(found.group())        

        return self.versions
        

if __name__ == '__main__':
    seb = seBackup().scriptEditorBackup()
