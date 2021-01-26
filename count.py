#Michael Santoro
#DU ID: 871869018
#Description: Count characters and Case
import sys

def add_frequencies(d, file, remove_case): #remove_case
    '''Function takes in three parameters: a dictionary d, a file object file, and a boolean remove_case.
    The dictionary maps characters to frequencies. Your function should add the frequency counts
    of the characters in the file file to the dictionary d.
    If remove_case is false, then the each character is the key into the dictionary. If remove_case
    is true, then the lowercase of each character is the key into the dictionary.'''
    #if remove_case:

    #Defines the Symbols that we would like to ignore
    delimiters = ['!', '\n']
    #Read File
    f = open(str(file), mode='r', encoding='ASCII')
    file_text = f.read()

    #Check Remove Case Flag
    if remove_case:
        file_text = file_text.lower()

    for letter in file_text:
        if letter in delimiters:
            None
        elif letter in d.keys():
            current_count = d[letter]
            current_count += 1
            d[letter] = current_count
        else:
            d[letter] = 1



def main():
    d = {}
    files = []

    for flag in sys.argv:
        if '.txt' == flag[-4:]:
            files.append(flag)
    for file in files:
        add_frequencies(d, file, True)


    #if '-c' in sys.argv:

    #elif '-l' in sys.argv:

    #elif '-z':

    #else:
    for i in d:
        print('"',i,'",', d[i],'\n')
        #case = True








main()
