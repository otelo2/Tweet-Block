#List of kpop artists and bands from 2010 onwards. 
# Source: https://en.wikipedia.org/wiki/List_of_K-pop_artists
# Source: https://en.wikipedia.org/wiki/List_of_South_Korean_idol_groups_(2010s)

#Makes the txt file 'kpopers.txt' into a python list
with open('kpopers.txt') as input_file:
    kpop_list = [line.strip() for line in input_file]
