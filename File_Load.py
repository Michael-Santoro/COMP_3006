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
    print(df)
    mean = df.mean()
    std = df.std()
    mode = df.mode()
    median = df.median()
    columns = []
    txtName = 'statsText.txt'
    string = ''

    for col in df.columns:
        columns.append(col)
    print(columns)

    # #Write the string from print to .txt
    # f = open(str(csvNa), mode='w', encoding='ASCII')
    # f.write(string)


    #print(mean[1],mean)
    #print(mode, type(mode), mode['Column 1'][0])




main()
