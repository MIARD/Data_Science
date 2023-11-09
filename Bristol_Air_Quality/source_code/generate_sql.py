import pandas as pd

# This function generates sql insert queries
# SOURCE is dataframe,TARGET is table name
# Return insert queries
def SQL_INSERT_STATEMENT_FROM_DATAFRAME(SOURCE, TARGET):
    sql_texts = []
    for index, row in SOURCE.iterrows():       
        sql_texts.append('INSERT INTO '+TARGET+' VALUES '+ str(tuple(row.values))+';')        
    return '\n\n'.join(sql_texts)


#read cleaned.csv into a dataframe
data = pd.read_csv("cleaned.csv", sep=';')



# Table: location
# Prepare dataframe to generate insert statements
#------------------------------------------------------------
#------------------------------------------------------------


# Given stations list.
stations_list = {'SiteID': [188,203,206,209,213,215,228,270,271,375,395,452,447,459,463,481,500,501], 
                 'SiteName': ['AURN Bristol Centre','Brislington Depot','Rupert Street','IKEA M32','Old Market',
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
merged_df_stations = pd.merge(left=df_given_stations, right=df_data_stations, how='left', left_on=['SiteID','SiteName'], right_on = ['SiteID','Location'])
# Select necessary columns 
merged_df_stations = merged_df_stations[['SiteID', 'SiteName', 'geo_point_2d']]
# Replace nan to empty string.
merged_df_stations = merged_df_stations.where(merged_df_stations.notna(), '')


# Table: airquality
# Prepare dataframe to generate insert statements
#------------------------------------------------------------
#------------------------------------------------------------

# Remove unnecessary columns
data = data.drop(['Location', 'geo_point_2d'], axis=1)
# Auto increamental Id column.
data.insert(0, 'Id', 'AUTO')
# Replace nan to empty string.
data = data.where(data.notna(), '')



# Writing sql in a file
f = open('pollution_data.sql', 'w')
f.write('\n-- Table: location \n')
f.write('-- ---------------------------------------- \n')
f.write(SQL_INSERT_STATEMENT_FROM_DATAFRAME(merged_df_stations, 'location'))
f.write('\n\n\n-- Table: airquality \n')
f.write('-- ---------------------------------------- \n')
f.write(SQL_INSERT_STATEMENT_FROM_DATAFRAME(data, 'airquality'))
f.close()
