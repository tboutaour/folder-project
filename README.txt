Pequeño proyecto para añadir una funcionalidad para la gestión de ficheros.
En el fichero folder_project.py se encuentra el código para que cualquier archivo
que se aparezca en las descargas se mueva según su extensión a una carpeta del sistema.

El código establece todas las bases necesarias. Para añadir extensiones se deben
modificar los condicionales.

Para añadir este programa por defecto en macOS se debe realizar un fichero plist.

En el se debe asignar el fichero folder_project en cuestión, así como el intérprete de python correcto.
Mover a la carpeta /Library/LaunchDaemons

Al fichero se le debe de dar permisos:
sudo chown root /Library/LaunchDaemons/tonibous.osx.move_file.plist
sudo chgrp wheel /Library/LaunchDaemons/tonibous.osx.move_file.plist

Para cargar el fichero en el sistema:
sudo launchctl load /Library/LaunchDaemons/tonibous.osx.move_file.plist
