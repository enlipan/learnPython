# - *- coding: utf- 8 - *-
#lipan
#C:\Users\Lee\Documents\Notepad\hardwaypython
def print_two(*args):
    arg1,arg2 = args
    print "arg1:%r, arg2:%r" %(arg1,arg2)

def print_one(arg1):
    print "arg1:%r" % arg1

def print_none():
    print "I got nothing"

print_two("Lee","Paul")
print_one("First!")
print_none()
