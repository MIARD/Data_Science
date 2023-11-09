# Install pymysql if it's not available
# !pip install pymysql
import pandas as pd
from sqlalchemy import create_engine

#read cleaned.csv into a dataframe
data = pd.read_csv("cleaned.csv", sep=';')

# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="",
                               db="measuring_air_quality"))


# Table: location
# Prepare dataframe to insert stations
#------------------------------------------------------------
#------------------------------------------------------------


# Given stations list.
stations_list = {'Id': [188,203,206,209,213,215,228,270,271,375,395,452,447,459,463,481,500,501], 
                 'Location': ['AURN Bristol Centre','Brislington Depot','Rupert Street','IKEA M32','Old Market',
                         'Parson Street School','Temple Meads Station','Wells Road','Trailer Portway P&R',
                         'Newfoundland Road Police Station',"Shiner's Garage",'AURN St Pauls','Bath Road',
                         'Cheltenham Road \ Station Road','Fishponds Road', 'CREATE Centre Roof','Temple Way','Colston Avenue']} 

# Convert stations list to a dataframe 
df_given_stations = pd.DataFrame(stations_list) 

# Select unique stations from dataset with first row values 
df_data_stations = data.drop_duplicates('SiteID', keep='first')
# Select necessary columns 
df_data_stations = df_data_stations[['SiteID', 'Location', 'geo_point_2d']]

# Make sure all stations are available in the list. There are only 14 stations in the main dataset.
# Left joining makes sure all stations are available.
merged_df_stations = pd.merge(left=df_given_stations, right=df_data_stations, how='left', left_on=['Id','Location'], right_on = ['SiteID','Location'])
# Select necessary columns 
merged_df_stations = merged_df_stations[['Id', 'Location', 'geo_point_2d']]
# Replace nan to empty string.
merged_df_stations = merged_df_stations.where(merged_df_stations.notna(), '')


# Table: airquality
# Prepare dataframe to insert data
#------------------------------------------------------------
#------------------------------------------------------------

# Remove unnecessary columns
data = data.drop(['Location', 'geo_point_2d'], axis=1)
# Auto increamental Id column.
data.insert(0, 'Id', 'AUTO')
# Replace nan to empty string.
data = data.where(data.notna(), '')


# Populate the database 'measuring_air_quality'
#------------------------------------------------------------
#------------------------------------------------------------

# Insert merged_df_stations DataFrame into MySQL table 'location' 
merged_df_stations.to_sql('location', con = engine, if_exists = 'append', chunksize = 1000, index=False)

# Insert data DataFrame into MySQL table 'airquality' 
data.to_sql('airquality', con = engine, if_exists = 'append', chunksize = 1000, index=False)


