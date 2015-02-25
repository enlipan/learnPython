# - *- coding: utf- 8 - *-
#lipan
#C:\Users\Lee\Documents\Notepad\hardwaypython
print "Let's practice everything"
print "You\'d need to know \' about escape with \\ that do \n new lines and \t tabs"

print "-"*10
poem="""
\tThe lovely world
with logic so firmly planted
cannot discernj \n the needs of love
nor comprehend passion from intution
and requires an explanation
\n\twhere there is none.
"""

print poem
print "-"*10

input_file = raw_input("input filename > ")
in_file =open(input_file)
content = in_file.read()
print "The file content: \n %s" % content
in_file.close()


print "*"*10
def secret_formula(started):
    jelly_beans = started * 100
    jars = jelly_beans / 50
    crates = jars / 100
    return jelly_beans,jars,crates

start_point = 10000
beans,jars,creats = secret_formula(start_point)

print "beans: %d ,jars: %d ,crates: %d " % (beans,jars,creats)
