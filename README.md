# seBackup
Maya Script Editor Tab Content Backup

seBackup.py copies content files for any Script Editor tabs in Maya. These files are deleted and not backuped when Maya is reset or the Preference files is reset. This script will copy and compress all Script Editor tab files into a zip file and save it outside the Maya /prefs directory.

Save seBackup.py to the maya/scripts directory. To find this directory print the following code in a Maya Python Script Editor:

import os
os.environ['MAYA_APP_DIR'] + '/scripts/'

The script can then be utilized as a scheduled event or through a GUI in Maya. To use the GUI, copy the code from seBackupMayaGUI into the Script Editor and run it, or copy the code into a shelf button to run from the shelf.

Note that if the seBackup.py is run through the the OS terminal, backup files will be saved to the user's maya/script directory by default.
