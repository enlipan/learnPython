# - *- coding: utf- 8 - *-
#lipan
#C:\Users\Lee\Documents\Notepad\hardwaypython
def add(a,b):
    print "Adding %d + %d" % (a,b)
    return a+b

def subtract(a,b):
    print "subtracting %d - %d" %(a,b)
    return a-b

def divide(a,b):
    print "dividing %d / %d " %(a,b)
    return a/b

age = add(1,2)
height = subtract(77,2)

print "age %r, height %r " %(age,height)

what= divide(add(2,2),subtract(3,1))
# inside out  由里向外解析
print what
