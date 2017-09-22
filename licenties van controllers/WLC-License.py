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
                data = re.split(r'\s{2,}', line)
                if data[0].startswith("Licensed Feature"):
                    key = [some for some in data]
                elif data[0].startswith("AP Count"):
                    value = [some for some in test]

    my_dict = dict(zip(key, value))


    difference = float(my_dict['Max Count']) - float(my_dict['Current Count'])

    percentleft = 100* float(my_dict['Current Count'])/float(my_dict['Max Count'])

    print('Controller licenses:')
    print('Max Count:     '+ my_dict['Max Count'])
    print('Current Count: '+ my_dict['Current Count'])
    print('Spare:         '+ str(difference))
    print(' ')
    print(percentleft)
    if percentleft > 80:
        print('less then 20% left!!')
    return;

if __name__ == '__main__':
    try:
        user_input = input("Enter text file name:")
        check_license(user_input)
    except:
        print("Entered file does not exist!")
    
