# - *- coding: utf- 8 - *-
#lipan
#C:\Users\Lee\Documents\Notepad\hardwaypython
from sys import argv
script, input_file =argv

def print_all(args):
    print args.read()

def rewind(args):
    args.seek(0)

def print_a_line(line_count,arg):
    print line_count,arg.readline()
current_file = open(input_file)

print "First,print the whole file:\n"

print_all(current_file)
# print the whole file use read() method

print "Now,rewind:"
rewind(current_file)
# print the line  which already read by the program

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)
