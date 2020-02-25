Little project to add functionality to file explorer system.
folder_project.py have the code to move Download files to other folders by file extension.
To add functionality you have to add the necessary code to the conditional part.
To add this program to default in macOS you have to make a plist file.
In this file you have to assign the folder_project file, as the python interpreter.

cd /Library/LaunchDaemons

The file must have some permisions (MacOS):
sudo chown root /Library/LaunchDaemons/tonibous.osx.move_file.plist
sudo chgrp wheel /Library/LaunchDaemons/tonibous.osx.move_file.plist

System file load:
sudo launchctl load /Library/LaunchDaemons/tonibous.osx.move_file.plist
