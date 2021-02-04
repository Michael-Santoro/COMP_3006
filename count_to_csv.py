#Michael Santoro
#DU ID: 871869018
#Description: This file will take the output of count and write to a .csv file

import count
import sys

def main():
    csvName = ''
    for flag in sys.argv:
        #Find the '.csv' filename
        if '.csv' == flag[-4:]:
            csvName = flag

    #Write the string from print to .csv
    f = open(str(csvName), mode='w', encoding='ASCII')
    f.write(count.print_count())

if __name__ == '__main__':
    main()
