# - *- coding: utf- 8 - *-
#lipan
#C:\Users\Lee\Documents\Notepad\hardwaypython
# extra argument-----how python work
ten_thing = "Apples Oranges Crows Light Suger"
print "Wait there's not 10 things in that list,let's fix that"

stuff = ten_thing.split(' ')
more_stuff = ["Day","Night","Song","Corn","Girl","Boy"]
while len(stuff)!=10:
    next_one = more_stuff.pop()
    print "Adding: ",next_one
    stuff.append(next_one)
    print "There's %d items now." %len(stuff)

print "There we go: ",stuff

print "Let's do someThing"

print stuff[1]
print stuff[-1]  # 从最后起第一个
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
