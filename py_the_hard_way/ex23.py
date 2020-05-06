# easy_pace_seconds = 8 * 60 + 15
# tempo_seconds = 7 * 60 + 12
# miles_at_easy_pace = 1 + 1
# miles_at_tempo = 3
# total_seconds = (miles_at_easy_pace * easy_pace_seconds) + (miles_at_tempo * tempo_seconds)

# print "Total running time:", total_seconds, "seconds"

# # division for minutes_ran is integer division, so it drops the fractions
# minutes_ran = total_seconds / 60
# seconds_ran = total_seconds - (minutes_ran * 60)

# print "Running time in minutes:", (minutes_ran + seconds_ran/60.0)

# start_time_hours = 6
# start_time_minutes = 52
# start_minutes_after_midnight = start_time_hours * 60 + start_time_minutes

# end_minutes_after_midnight = start_minutes_after_midnight + minutes_ran

# end_time_hours = end_minutes_after_midnight / 60
# end_time_minutes = end_minutes_after_midnight - (end_time_hours * 60)

# end_time_str = str(end_time_hours) + ":" + str(end_time_minutes) + ":" + str(seconds_ran)
# print end_time_str



# mylist = [1, 2, 3, 4, 5, 6]

# myotherlist = [[1,2,3],'b']

# for element in myotherlist:
#     mylist.append(element)
    
# print mylist


# use the complement function
# read in lines from a file
# convert them to their DNA complement
# print the result

def complement(dna_string):
    dna_complement = {'a': 't',
                      'g': 'c',
                      't': 'a',
    #dna_complement = dict(a='t', c='g', t='a', g='c')
                      'c': 'g'}
    comp_string = ''
    for base in dna_string:
        comp_string += dna_complement.get(base, 'n')
        #if base in dna_complement:
            #comp_string += dna_complement[base]
        #else:
            #comp_string += 'n'
    return comp_string

dna_string = raw_input('Enter a DNA string file name:')
han = open(dna_string,'r').read()
comp_string = complement(han)
print "Complement is:", comp_string
