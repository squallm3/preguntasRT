import pandas as pd
import os
import datetime

# Read the CSV
df = pd.read_csv('./input/08_2022_csv.csv')
# Makes a list of unique dates
listUniqueDates = pd.unique(df['Fecha'])


# Convert
df['Fecha']=df['Fecha'].map(datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%A'))

print(df)
# for date in listUniqueDates:
#     print(datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%A'))


# print(listUniqueDates)
# print(len(listUniqueDates))

# print(df.groupby(['Fecha']).size())