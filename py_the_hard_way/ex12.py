from __future__ import division
age = int(raw_input("How old are you? "))
height = int(raw_input("How tall are you in inches? "))
weight = int(raw_input("How many pounds do you weigh? "))
print "So, you're %d years old, %d inches tall and %d lbs." % (age, height, weight)
print "Your BMI is %f." % round(((weight * 703) / (height**2)), 3)
