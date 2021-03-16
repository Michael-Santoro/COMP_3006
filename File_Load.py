#Michael Santoro
#COMP 3008 - Project 6
#Calculate the mean, standard deviation, mode, and median of the values in your file.
#Generate a text file that includes:
#The above statistics
#The column names used in the file (gotten from the dataframe not hard coded)
#3 rows of your choosing from the dataframe as sample data

#Imports
import pandas as pd


def main():
    #Read in File to DataFrame
    fileName = 'numPyArray.csv'
    df = pd.read_csv(fileName)

    #Calculate Values
    mean = df.mean()
    std = df.std()
    mode = df.mode()
    median = df.median()
    columns = []
    txtName = 'statsText.txt'
    string = ''

    #Grab Columns from Data Frame
    for col in df.columns:
        columns.append(col)

    string = f'Stats for CSV {fileName}\n'
    string = string + f'Stats: '
    for i in range(len(columns)):
        string = string + f'{columns[i]}, '
    string = string[:-2]
    string = string + f'\n'

    string = string + f'Mean: '
    for i in range(len(columns)):
        string = string + f'{round(mean[i],1)}, '
    string = string[:-2]
    string = string + f'\n'

    string = string + f'Standard Deviation: '
    for i in range(len(columns)):
        string = string + f'{round(std[i],1)}, '
    string = string[:-2]
    string = string + f'\n'

    string = string + f'Mode: '
    for i in range(len(columns)):
        string = string + f'{mode[columns[i]][0]}, '
    string = string[:-2]
    string = string + f'\n'

    string = string + f'Median: '
    for i in range(len(columns)):
        string = string + f'{median[i]}, '
    string = string[:-2]
    string = string + f'\n'
    string = string + f'Sample Data: \n'
    string = string + f'{df.head(3)}'


    #Write the string from print to .txt
    f = open(str(txtName), mode='w', encoding='ASCII')
    f.write(string)




main()
