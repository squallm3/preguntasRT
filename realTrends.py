from tabnanny import verbose
import pandas as pd
import os
import datetime
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV
df = pd.read_csv('./input/08_2022_csv.csv')
# Convert date column into date object
df['Fecha'] = pd.to_datetime(df['Fecha'], infer_datetime_format=True)
# Convert date complete format to only day / hour format
df['Fecha'] = df['Fecha'].dt.strftime('%A %H')
# Group by date / hour
groupedByDateHour = df.groupby(['Fecha']).size()

# print(df)
# print(listUniqueDates)
print(groupedByDateHour)

