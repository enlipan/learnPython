# - *- coding: utf- 8 - *-
#lipan
tabby_cat = "\tI'm tabble in.\r"
persian_cat = "\fI'm split \non a line."
backslash_cat = "I'm \\ a \\ cat. \a"

fat_cat = """
I'll so a list:
\t*Cat food
\t*Fishes
\t*Catnip\n*Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

key = True
while key:
	for i in ["/","- ","|","\\","|"]:
		print "%r\r" % i
		print "%s\r" % i
		if i == "|":
			key = False
