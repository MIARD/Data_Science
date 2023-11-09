import pandas as pd

#read cropped.csv(task 1a result) into a dataframe
data = pd.read_csv("cropped.csv", sep=';')

# Given stations list.
stations_list = {'SiteID': [188,203,206,209,213,215,228,270,271,375,395,452,447,459,463,481,500,501], 
                 'SiteName': ['AURN Bristol Centre','Brislington Depot','Rupert Street','IKEA M32','Old Market',
                         'Parson Street School','Temple Meads Station','Wells Road','Trailer Portway P&R',
                         'Newfoundland Road Police Station',"Shiner's Garage",'AURN St Pauls','Bath Road',
                         'Cheltenham Road \ Station Road','Fishponds Road', 'CREATE Centre Roof','Temple Way','Colston Avenue']} 

# Convert stations list to a dataframe 
df_stations = pd.DataFrame(stations_list)  

# Merged both dataframes(Left outer joining based on 'SiteID','Location')
# indicator='source' adds a column to the output DataFrame called “_merge” with information on the source of each row
merged_df = pd.merge(left=data, right=df_stations, how='left', left_on=['SiteID','Location'], right_on = ['SiteID','SiteName'], indicator=True)

# Dud records(mismatch of 'SiteID' and'Location' in between both dataframes)
dud_records_df = merged_df.query('_merge != "both"')
print(f"{dud_records_df.shape[0]} dud records were found.")

# Print mismatch field values
print('\n\nDud records:\n')
print(dud_records_df[['SiteID', 'Location']])

# Correct records
result = merged_df.query('_merge == "both"')
# Remove unnecessary columns
result = result.drop(['SiteName', '_merge'], axis=1)

# Export cleaned data rows into cleaned.csv
#index = false avoids writing the pandas generated index as a column
result.to_csv('cleaned.csv', sep=';', index=False)
