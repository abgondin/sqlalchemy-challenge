# 10 SQLAlchemy - Climate App

## Background

A database containing climate data of Hawaii is used to do climate analysis and to create a climate app.

### Climate analysis and exploration

Python and SQLAlchemy are used to do basic climate analysis and data exploration of the climate database hawaii.sqlite.

### Climate App

A Flask API app is created with the following routes: 

/ Home page. List of all available routes.

/api/v1.0/precipitation Convert the query results to a dictionary using date as the key and prcp as the value. Returns a JSON representation of a dictionary.

/api/v1.0/stations Returns a JSON list of stations from the dataset.

/api/v1.0/tobs Query the dates and temperature observations of the most active station for the last year of data. Returns a JSON list of temperature observations (TOBS) for the previous year.

/api/v1.0/<start> and /api/v1.0/<start>/<end> Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

## Skills

SQLAlchemy ORM queries | pandas | matplotlib | Flask API |
