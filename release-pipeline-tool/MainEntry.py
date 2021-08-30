import getopt
import sys

from ArchiveHandler import ArchiveHandler
from CreateHandler import CreateMain
from DeleteHandler import DeleteHandler
from consts import optional_arguments_name


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "-c", optional_arguments_name)
    except getopt.GetoptError:
        print("arguments must be set [ command: create, delete, archive ] ")
        sys.exit(2)

    for opt, arg in opts:
        print('opt: %s, arg: %s' % (opt, arg))
        if opt == '--command':
            if arg == 'create':
                CreateMain.handle(sys.argv[1:])
            elif arg == 'delete':
                DeleteHandler.handle(sys.argv[1:])
            elif arg == 'archive':
                ArchiveHandler.handle(sys.argv[1:])
            else:
                print
                'Command not supported, support only: create, delete, archive'
                sys.exit()


if __name__ == '__main__':
    print
    sys.argv
    if sys.argv.__len__() == 1:
        print("arguments must be set [ command: create, delete, archive ] ")
        sys.exit(2)

    main(sys.argv[1:])
