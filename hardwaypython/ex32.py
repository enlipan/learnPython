# - *- coding: utf- 8 - *-
#lipan
#C:\Users\Lee\Documents\Notepad\hardwaypython
the_count = [1,2,3,4]
fruits = ['apples','pears','oranges']
change = [1,'pennies',2,'dimes']

# this first kind of for-loop
for number in the_count :
    print "This is count %d" % number

# same as bove
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# mixed lists
for i in change:
    print "I got %r " % i

elements = []

for i in range(0,6):
    print "adding %d to the list" % i
    elements.append(i)

for i in range(0,-6,-1):
    print "adding %d to the list" % i
    elements.append(i)

# print all
for i in elements:
    print "elements(%d)" % i
