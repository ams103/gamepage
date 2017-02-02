import random, os, sys
from time import sleep
from typewriter import Typewriter

from attributes import Attributes
#typewriter delays the text and print it out one sign at the time.
races = ["Dwarf", "Elf","Human", "Orc"]

Typewriter("Welcome to xxx!!!")
print()
Typewriter("Important commands: !attributes, !racelist, !classlist, !stats")
print()
Typewriter("What do you wish to be called? ")
name = input()
Typewriter("What race do you wanna be? Type \"!raceinfo\"" "to find out details.")
print()
Typewriter("Do wish to be a dwarf, elf, human or an orc? ")
print()

race = input()

r = len(races)

for r in races:
    if races == "!raceinfo":
        print(r, end='')
        sys.stdout.flush()
        sleep(0.45)
        print()
    """else races == "!dwarf":
        for attributes in Attributes:
            print (dwarf, end='')
            sys.stdout.flush()
            sleep(0.45)
            print()"""