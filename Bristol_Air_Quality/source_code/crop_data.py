import pandas as pd

#read origin csv data into a dataframe
data = pd.read_csv("bristol-air-quality-data.csv", sep=';')
print(f"{data.shape[0]} data rows before the date filtering")

#convert to a datetime. This validates that all non null values are actual valid timestamps
data['Date Time'] = pd.to_datetime(data['Date Time'])

#keep all rows where [Date Time] years are greater than 2009
data = data[data["Date Time"].dt.year > 2009]
print(f"{data.shape[0]} data rows after the date filtering")

# Export data rows to cropped.csv file.
#index = false avoids writing the pandas generated index as a column
data.to_csv('cropped.csv', sep=';', index=False)