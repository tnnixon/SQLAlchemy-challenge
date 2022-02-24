from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import datetime as dt

# Database setup
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session from Python to DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data for the last year."""
    
    # Calculate the date 1 year ago from last date in database
    oneYearLater = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query for the date and precipitation for the last year
    prcpResult = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>=oneYearLater).all()

    session.close()

    #Dictionary with date as the key and precipitation as the value
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    """Returns a list of stations"""
    results = session.query(Station.station).all()

    session.close()

    # Unravel results into 1D array and convert to list
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def tempMonthly():
    """Returns the temperature observations (tobs) for previous year"""
    
    #Calculate the date 1 year ago from last date in database
    oneYearLater = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the primary station for all tobs for the last year
    tempResult = session.query(Measurement.tobs).filter(Measurement.station=="USC00519281").filter(Measurement.date>=oneYearLater).all()

    session.close()

    # Unravel results into 1D array and convert to list
    temps = list(np.ravel(tempResult))
    return jsonify(temps=temps)



if __name__ == "__main__":
    app.run(debug=True)
