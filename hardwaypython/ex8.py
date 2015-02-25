# - *- coding: utf- 8 - *-
#lipan
formatter = "%s %r %r %r"
print formatter % (u'你',2,3,4)#in python2  use u'你' show unicode
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
			"I had this thing",
			"that you could type up right",
			"But it didn't sing",
			"so I said goodnight"
			)
			