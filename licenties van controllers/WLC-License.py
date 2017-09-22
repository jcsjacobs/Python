### this script is used to disect the "show license capacity"
### on a cisco WLC controller
###
### The layout is something like:
###
###Licensed Feature    Max Count         Current Count     Remaining Count
###-----------------------------------------------------------------------
###AP Count            2000                1999                1           


import json
import re

def check_license (read_file):
    keys =[]
    value = []
    with open(read_file,'r') as file:
        for line in file:
            if not line.startswith('------'):
                test = re.split(r'\s{2,}', line)
                if test[0].startswith("Licensed Feature"):
                    d = [el for el in test]
                elif test[0].startswith("AP Count"):
                    e = [el for el in test]

    my_dict = dict(zip(d, e))


    difference = float(my_dict['Max Count']) - float(my_dict['Current Count'])

    percentleft = 100* float(my_dict['Current Count'])/float(my_dict['Max Count'])

    print('Controller licenses:')
    print('Max Count:     '+ my_dict['Max Count'])
    print('Current Count: '+ my_dict['Current Count'])
    print('Spare:         '+ str(difference))
    print(' ')
    print(percentleft)
    if percentleft > 80:
