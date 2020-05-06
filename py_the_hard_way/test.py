#Display Value from 1 TO 3  
for i in range(1,4):
    print "",i,"value of loop"

# Loop for dictionary data type
mydata = {"Fahim":"Pakistan", "Vedon":"China", "Bill":"USA"  }  
for user, country in mydata.iteritems():
    print user, "belongs to " ,country



# Test dictionary

person_dict = {'name': 'john',
               'age': 18,
               'grade': 12}
print(person_dict['age'])


# List
my_list = ['john', 'catherine', 'claire', 'amy']
print(my_list[2])
