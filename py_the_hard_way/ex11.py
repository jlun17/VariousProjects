from __future__ import division
print "How old are you?",
age = int(raw_input())
print "How tall are you in inches?",
height = int(raw_input())
print "How many pounds do you weigh?",
weight = int(raw_input())

print "So, you're %d years old, %d inches tall and %d lbs." % (age, height, weight)
print "Your BMI is %f." % round(((weight * 703) / (height**2)), 3)
