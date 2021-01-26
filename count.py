#Michael Santoro
#DU ID: 871869018
#Description: Count characters with some different flag options (i.e. ignore case) then it prints the counts

import sys

def add_frequencies(d, file, remove_case):
    '''Function takes in three parameters: a dictionary d, a file object file, and a boolean remove_case.
    The dictionary maps characters to frequencies. Your function should add the frequency counts
    of the characters in the file file to the dictionary d.
    If remove_case is false, then the each character is the key into the dictionary. If remove_case
    is true, then the lowercase of each character is the key into the dictionary.'''


    #Defines the Symbols that we would like to ignore in dictionary
    delimiters = ['!', '\n', ' ']

    #Reads in file
    f = open(str(file), mode='r', encoding='ASCII')
    file_text = f.read()

    #Check for the remove case flag and fix cases
    if remove_case:
        file_text = file_text.lower()

    #Update Dictionary 'd'
    for letter in file_text:
        if letter in delimiters:
            None

        #Increment Count
        elif letter in d.keys():
            current_count = d[letter]
            current_count += 1
            d[letter] = current_count
        #Add letter as Key
        else:
            d[letter] = 1

def main():
    d = {}
    files = []
    case_flag = True

    #Collects the file names to count
    for flag in sys.argv:
        if '.txt' == flag[-4:]:
            files.append(flag)

    #Checks for the cases flag and sets the variable accordingly
    if '-c' in sys.argv:
        case_flag = False

    #Each filename in files will call add frequencies to update the dictionary
    for file in files:
        add_frequencies(d, file, case_flag)

    #Prints just the letters with the '-l' flag
    if '-l' in sys.argv:
        index = sys.argv.index('-l')
        string_flag = sys.argv[index+1]
        for l in string_flag:
            print(f'"{l}",{d[l]}')#removed '/n' here if writing to an actual csv would need to add

    #Prints the syntax for the '-z' flag
    elif '-z' in sys.argv:
        zFlagList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for z in zFlagList:
            if z in d:
                print(f'"{z}",{d[z]}') #removed '/n' here if writing to an actual csv would need to add
            else:
                print(f'"{z}",0')#removed '/n' here if writing to an actual csv would need to add

    else:
        for i in d:
            print(f'"{i}",{d[i]}')#removed '/n' here if writing to an actual csv would need to add


main()
