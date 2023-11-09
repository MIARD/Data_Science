### Problem Statement:

1. Model the data to a NoSQL database using MongoDB
2. Populate database
3. Query c in Task 4 to verify the implementation

### Impelmentation Steps:

##### 1. Installed MongoDB and created Database and collection by using MongoDB Compass.

    Database: AirQuality
    
    Collection: Readings


##### 2. Data modeling for NoSQL Database.

```
[
  {
	"SiteID": 203,
    "Location": "Brislington Depot",
    "geo_point_2d": "51.4417471802,-2.55995583224",
    "AirQualityReadings": [
		  {
			"DateTime": "2013-08-23 08:00:00+00:00",
			"NOx": 94.5,
			.
			.
			.
			"DateEnd": null,
			"Current": true,
			"Instrument Type": "Continuous (Reference)"
		  },
		  
		  {
			"DateTime": "2013-08-23 18:00:00+00:00",
			"NOx": 81.0,
			.
			.
			.
			"DateEnd": null,
			"Current": true,
			"Instrument Type": "Continuous (Reference)"
		  }
	  ]
	}
]

```

##### 3. Wrote python script to import JSON data into MongoDB. Some key code lines are given below.

```
# Convert dataframe to json data accroding to data model.
j = (result.groupby(['SiteID', 'Location', 'geo_point_2d'], as_index=True)
             .apply(lambda x: x[columns].to_dict('r'))
               .reset_index()
               .rename(columns={0:'AirQualityReadings'})
               .to_json(orient='records'))

```

```
# Making Connection
myclient = MongoClient("mongodb://localhost:27017/") 
   
# database 
db = myclient["AirQuality"]
   
# Created or Switched to collection 
# names: Readings
Collection = db["Readings"]

# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
Collection.insert_many(json.loads(j))

```

##### 4. Query c in Task 4 to verify the implementation and expected result.

My Pipeline: 

```
[{$project: {
  "SiteID": 1,
  "Location": 1,
  "AirQualityReadings.DateTime": 1,
  "AirQualityReadings.NO": 1,
  "AirQualityReadings.NO2": 1
}}, {$addFields: {
 AirQualityReadings: {
        $map: {
          input: "$AirQualityReadings",
          in: {
            $mergeObjects: [
              "$$this",
              {
                year :  { $substr : ["$$this.DateTime", 0, 4 ] },
                hour :  { $substr : ["$$this.DateTime", 11, 2 ] }
              }
            ]
          }
        }
      }
}}, {$match: {
   "AirQualityReadings.year": '2019',
   "AirQualityReadings.hour": '08'

    }}, {$unwind: {
  path: "$AirQualityReadings"
}}, {$group: {
  _id: "$SiteID",
  MEAN_NO: { $avg: "$AirQualityReadings.NO" },
  MEAN_NO2: { $avg: "$AirQualityReadings.NO2" }
}}]

```

My result:

![My result](http://2rsolution.com/wp-content/uploads/2021/05/c-query.jpg)