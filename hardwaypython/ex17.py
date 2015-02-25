# - *- coding: utf- 8 - *-
#lipan
#C:\Users\Lee\Documents\Notepad\hardwaypython
from sys import argv
from os.path import exists

script, from_file,to_file = argv

print "copying from %r to %r " %(from_file,to_file)

#we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "the input file is %d bytes long" % len(indata)
print "does the output file exists? %r" % exists(to_file)
print "ready,hit Return to continue,Ctrl-C to abort \n"
raw_input("?")

out_file = open(to_file,'w')
out_file.write(indata)

print "Alright,all done"

out_file.close()
in_file.close()
