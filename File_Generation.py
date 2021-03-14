#Michael Santoro
#COMP 3008 - Project 6
# Using numpy, generate a 10 column by 1000 row matrix of values (this values may be whatever you want. Get Creative!)
#
# Create a csv file using this data. Please choose 10 column names for the file.

import numpy as np
import random

def main():
    list = []
    csvName = 'numPyArray.csv'
    ColumnHeaders = ''
    string = ''
    #Create String of Column Headers
    for j in range(1,11):
        ColumnHeaders += f'Column {j},'
    ColumnHeaders += '\n'
    # Find Random numbers and Append to List
    for i in range(10000):
        number = random.randint(1,100)
        list.append(number)
    a = np.array(list).reshape(10,1000)
    print(a.shape)
    string = np.array2string(a, separator=',', max_line_width = 45, threshold = 10000)
    string.replace('[', '')
    string.replace(']','')
    string = ColumnHeaders + string

    #Write the string from print to .csv
    f = open(str(csvName), mode='w', encoding='ASCII')
    f.write(string)
main()
