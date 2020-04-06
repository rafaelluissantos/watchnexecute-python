import time

# you need watchdog library, pip install it
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    
    def __init__(self, directory, event_handler_fn):
        self.observer = Observer()
        self.directory = directory
        self.event_handler = FileEventHandler(event_handler_fn);

    def run(self):
        self.observer.schedule(self.event_handler, self.directory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(100)
        except:
            self.observer.stop()
            print("error observing directory \"%s\"" % self.directory)

        self.observer.join()


class FileEventHandler(FileSystemEventHandler):

    def __init__(self, event_handler_fn):
        self.event_handler_fn = event_handler_fn;

    def on_any_event(self, event):
        if not event.is_directory:
            self.event_handler_fn(event)

