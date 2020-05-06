your_list = 'abcdefghijklmnopqrstuvwxyz'
password = raw_input("Password?")
complete_list = []
for current in xrange(2):
    a = [i for i in your_list]
    print "outer loop", a
    for y in xrange(current):
        a = [x+i for i in your_list for x in a]
        print "inner loop", a
        if a == password:
            print a
            break
    complete_list = complete_list+a
#print len(complete_list)
#print complete_list
#print complete_list[:5]
