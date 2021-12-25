import sys

from gui import constants
from gui.newcontrol import GUI

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("OK")
        json_file = sys.argv[1]
        constants.ga.load_from_json(file_name=json_file)
        GUI()
    else:
        print("no json path added ")
        print("exit program")
        sys.exit()

