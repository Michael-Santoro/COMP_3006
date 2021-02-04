#Michael Santoro
#DU ID: 871869018
#Description:

import count
import sys

def main():
    csvName = ''
    for flag in sys.argv:
        if '.csv' == flag[-4:]:
            csvName = flag


    f = open(str(csvName), mode='w', encoding='ASCII')
    f.write(count.print_count())

if __name__ == '__main__':
    main()
