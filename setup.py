def install(package):
    pip.main(['install', package])
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

import pip
import os
from time import sleep
cls()


print("Welcome to the ODST modules verification.")
sleep(2)
print("Checking if the ODST modules are installed...")
sleep(1.3)
print()


###for time
print('Checking for "time"...')
sleep(1)
try:
    import time
    print("Time is already installed")
    print()
    sleep(1)
except ImportError:
    print("Time is not installed, I install it.")
    install('time')
    print("Done")


### for progress 
import pip
print('Checking for "progress"...')
sleep(1)
try:
    import progress
    print("Progress is already installed")
    print()
    sleep(1)
except ImportError:
    print("Progress is not installed, I install it.")
    install('progress')
    print("Done")


### for colored
import pip
print('Checking for "colored"...')
sleep(1)
try:
    import colored
    print("Colored is already installed")
    print()
except ImportError:
    print("Colored is not installed, I install it.")
    install('colored')
    print("Done")


print("All modules are install, now go to the Linux folder and start it with : python Linux.py")
input("Press [ENTER] key to continue")