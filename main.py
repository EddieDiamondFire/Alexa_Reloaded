import alexa
import sys
from common import utils as u

# TODO add a debug option

# Check current version of Speech Recognition
u.print_version("Speech Recognition", alexa.check_version())

if not(sys.version_info.major == 3 and sys.version_info.minor >= 9):
    print("This python program requires to be running on 3.9 +")
    print("Your current python version is " + str(sys.version_info.major) + "." + str(sys.version_info.minor))
    exit(1)


print("Starting Alexa")
alexa.start_alexa_program()






