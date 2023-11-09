### Problem Statement

1. Read CSV file, Crop, Cleanse and Refactor the Data.
2. Create and Implement a Normalized Database.
3. Write Python scripts to generate the required SQL and populate MySQL database 
4. Design, Write and Run SQL Queries.
5. Model, implement and query a selected NoSQL database.

#### The way I worked:
1. Read and understand the requirements.
2. Plan and looking for solutions.
3. R&D for the required knowledge.
4. Implementation for the expected results. 

#### What I learned:
1. Basic and intermediate python programming skills.
2. Read csv file, Crop, Cleanse and Refactor the Data by using python library pandas.
2. Design ER digram by using MySQL workbench and implement & populate Mysql database.  
3. MySQL query practice. 
4. Model data for NOSQL database by using MongoDB, Populate NoSQL database and query practice.  

#### The problem I faced:

First, I struggled to run the DB script generated from the forward engineering of MySQL workbench in the MySQL server.  The VISIBLE keyword was not working in my MySQL version. When I removed this keyword, the script was run successfully.   

```
 INDEX `fk_AirQuality_Location_idx` (`SiteID` ASC) VISIBLE,
 
```
Next, when I was importing JSON data into the MongoDB database, it was failed to import data because the JSON document size was more than 16MB. To resolve this issue, I split the data station-wise. Then I was able to import all data into the MongoDB database.

```
# Split data station-wise
result = result.query('SiteID == 203')


j = (result.groupby(['SiteID', 'Location', 'geo_point_2d'], as_index=True)
             .apply(lambda x: x[columns].to_dict('r'))
               .reset_index()
               .rename(columns={0:'AirQualityReadings'})
               .to_json(orient='records'))
 
```

#### Strength:
1. Previous work experience and programming knowledge.
2. Python programming syntax was very easy to understand.


#### Weakness:
1. NoSQL database
2. The better way to write code.

This is the first time; I am working on the NoSQL database. I do believe that NoSQL database is an important part of the field of data science. I need to focus more on this part. However, this assignment has introduced me to NoSQL for further development.

I am still new to python programming. I do believe that I can develop my python programming skills gradually. It's just more practice to develop the skills.

Finally, It was a fun and happy coding practice that helped to introduce myself to data science programming.   

