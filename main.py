import alexa
import sys
from common import utils as u

print("Debug?: ")
debug = input()

while True:
    if debug == "False":
        debug_mode = False
        break
    elif debug == "True":
        debug = True
    else:
        print("Please say if you want debug mode on...")

        print("Debug?: ")
        debug = input()
        if debug == "False":
            debug_mode = False
            break
        elif debug == "True":
            debug = True
        else:
            print("Please say if you want debug mode on...")


def debug_message(package_name, message):
    if debug_mode:
        u.print_version(package_name, message)


# Check current version of Speech Recognition
debug_message("Speech Recognition", alexa.check_version())

if not (sys.version_info.major == 3 and sys.version_info.minor >= 9):
    print("This python program requires to be running on 3.9 +")
    print("Your current python version is " + str(sys.version_info.major) + "." + str(sys.version_info.minor))
    exit(1)

print("Starting Alexa")
alexa.start_alexa_program()
