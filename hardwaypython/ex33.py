# - *- coding: utf- 8 - *-
#lipan
#C:\Users\Lee\Documents\Notepad\hardwaypython
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    print "the persent num is",i
    num = int(raw_input("input the number  i will adding > "))
    i += num
    print "Numbers now :",numbers
    print "the top number is %d" % i

print "the numbers:"
for num in numbers:
    print num
