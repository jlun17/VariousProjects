name  = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
# 1 inch = 2.54 cm
# 1 lb = .454 kg
print "Let's talk about %s." % name
print "He's %d inches tall, or %d centimeters tall." %(height, height * 2.54)
print "he's %d pounds heavy, or %d kilograms." %(weight, weight * .454)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight)


print "I have %r dogs." % height
print "My name is %r." % name
print "My name is %s." % name
print "I have %d dogs." % height
print "I have %s dogs." % height
print "I have % dogs." % height
print "john%hug" % height
print "john%11g is here" % 74.01
print "john%11g is here" % 744.01
print "john%11g is here" % 7444.01
print "john%11f.2 is here" % 74.10

print "john%11s is here" % "lundstrom"
print "I have %r dogs." % height

file_handle = open("tmp/google.html")
print "%r" % file_handle
