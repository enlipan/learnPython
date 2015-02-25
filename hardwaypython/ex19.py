# - *- coding: utf- 8 - *-
#lipan
#C:\Users\Lee\Documents\Notepad\hardwaypython
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %d cheese" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Good! \n"

print "We give the function numbers directly"
cheese_and_crackers(20,30)


print "Or,we can use variable from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can do this too!"
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)

user_amount_cheese = int(raw_input("cheese input: "))
user_amount_cracker = int(raw_input("crackers input: "))
cheese_and_crackers(user_amount_cheese,user_amount_cracker)
