# - *- coding: utf- 8 - *-
#lipan
#C:\Users\Lee\Documents\Notepad\hardwaypython
print  "You  enter a dark room with two doors,do you go through door #1 or #2?"
door = int(raw_input("> "))

if door == 1:
    print "1 .take the cake."
    print "2 .Scream at the bear."
    bear = int(raw_input("> "))

    if bear == 1:
        print "good job!"
    elif bear == 2:
        print "good job!"
    else:
        print "well, doing %s is probably better."  % bear

elif door == 2:
    print "you stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries"
    print "2. Yellow jacket clothesins"
    print "Uderstanding revolvers yelling melodies"

    insanity = int(raw_input("> "))
    if insanity == 1:
        print "Your body survice powered by a mind of jello."
    else:
        print "the insanity rots your eyes into a pool of muck."
else:
    print "You stumble a round and fall on a knife and die."
