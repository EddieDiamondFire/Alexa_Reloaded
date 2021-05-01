import alexa
import sys
from common import utils as u
from common import file

config_file = file.config_load()


def debug_mode():
    if config_file["general"].get("debug_mode"):
        print("Debug mode is enabled!")
        return True
    elif config_file["general"].get("debug_mode"):
        return False
    else:
        return False


def debug_message(package_name, message):
    if debug_mode():
        u.print_version(package_name, message)


# Check current version of Speech Recognition
debug_message("Speech Recognition", alexa.check_version())

if not (sys.version_info.major == 3 and sys.version_info.minor >= 9):
    print("This python program requires to be running on 3.9 +")
    print("Your current python version is " + str(sys.version_info.major) + "." + str(sys.version_info.minor))
    exit(1)

print("Starting Alexa")
alexa.start_alexa_program()
