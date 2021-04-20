import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()  # reflect an existing database into a new model
Base.prepare(engine, reflect=True)  # reflect the tables

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"Dictionary with Date and Precipitation data: /api/v1.0/precipitation<br/>"
        f"Dictionary with Stations and their associated data: /api/v1.0/stations<br/>"
        f"List of Temperatures in the last year: /api/v1.0/tobs<br/>"
        f"Temperature data from start date(yyyy-mm-dd): /api/v1.0/yyyy-mm-dd<br/>"
        f"Temperature data from start date(yyyy-mm-dd) to end date(yyyy-mm-dd): /api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    )


@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    sel = [Measurement.date, Measurement.prcp]
    queryresult = session.query(*sel).all()
    session.close()

    precipitation = []
    for date, prcp in queryresult:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        precipitation.append(prcp_dict)

    return jsonify(precipitation)


@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    sel = [Station.station, Station.name, Station.latitude,
           Station.longitude, Station.elevation]
    queryresult = session.query(*sel).all()
    session.close()

    stations = []
    for station, name, lat, lon, el in queryresult:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Lat"] = lat
        station_dict["Lon"] = lon
        station_dict["Elevation"] = el
        stations.append(station_dict)

    return jsonify(stations)


@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    last_date = session.query(Measurement.date).order_by(
        (Measurement.date).desc()).first()
    last_date = dt.datetime.strptime(last_date[0], '%Y-%m-%d')
    year_from_last = last_date - dt.timedelta(days=365)
    queryresult = session.query(Measurement.tobs).filter(
        Measurement.date >= year_from_last).all()
    session.close()

    # Convert list of tuples into normal list
    tobs = list(np.ravel(queryresult))

    return jsonify(tobs)


@app.route('/api/v1.0/<start>')
def get_tempdata_start(start):
    session = Session(engine)
    queryresult = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    session.close()

    tempdata = []
    for min, avg, max in queryresult:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        tempdata.append(tobs_dict)

    return jsonify(tempdata)


@app.route('/api/v1.0/<start>/<end>')
def get_tempdata_start_end(start, end):
    session = Session(engine)
    queryresult = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()

    tempdata = []
    for min, avg, max in queryresult:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        tempdata.append(tobs_dict)

    return jsonify(tempdata)


if __name__ == '__main__':
    app.run(debug=True)
