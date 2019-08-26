from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(FOLDER_TO_TRACK):
            print(filename)
            if filename.endswith('.epub'):
                folder_destination = BOOK_DIRECTORY
                src = FOLDER_TO_TRACK + "/" + filename
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)

FOLDER_TO_TRACK = "/Users/tonibous/Downloads"
BOOK_DIRECTORY = "/Users/tonibous/Documents/Libros"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, FOLDER_TO_TRACK, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
