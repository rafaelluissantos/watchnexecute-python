
from watcher import Watcher
from executor import Executor

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Watch directory and execute cmd.')
    parser.add_argument('directory', metavar='dir', help='directory to watch')
    parser.add_argument('cmd', metavar='cmd', help='cmd to be executued for each new file')
    args = parser.parse_args()

    print("watching directory \"%s\"" % args.directory)
    print("will execute \"%s\" for directory modified files." % args.cmd)

    e = Executor(args.cmd)
    event_fn = lambda event: e.execute(event.src_path)
    w = Watcher(args.directory, event_fn)
    w.run()