# Import dependencies 
import datetime as dt
import numpy as np
import pandas as pd
# Import the SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# Import dependencies for flask
from flask import Flask, jsonify

# Set up database engine for the Flask application and access the SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect database into classes 
Base = automap_base()
Base.prepare(engine, reflect=True)

# Create variables for each of the classes to reference later
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to the database
session = Session(engine)

# Define the flask app, create a new application called app
app = Flask(__name__)

# Define the welcome route
@app.route("/")
# Create a function welcome() with a return statement
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Create a new route for the precipitation analysis
@app.route("/api/v1.0/precipitation")

# Create the precipitation function
def precipitation():
    # Calculate the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Get date and precipitation for previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    # Create a dictionary with the date as the key and the precipitation as the value
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Define a new route for the station analysis
@app.route("/api/v1.0/stations")

# Create a new function called stations()
def stations():
    # Create a query that will get all of the stations in the database
    results = session.query(Station.station).all()
    # Unravel results into a one-dimensional array and convert to a list
    stations = list(np.ravel(results))
    # Jsonify list and return as json
    return jsonify(stations=stations)

# Define a new route for the temperature analysis
@app.route("/api/v1.0/tobs")

# Create a function called temp_monthly()
def temp_monthly():
    # Calculate the date one year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    # Unravel the results into a one-dimensional array and convert that array into a list
    temps = list(np.ravel(results))
    # Jsonify temps list and return it
    return jsonify(temps=temps)
    
# Create new routes for the statistics analysis (starting and ending dates)
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create a function called stats()
def stats(start=None, end=None):
    # Create a query to select the minimum, average, and maximum temperatures from SQLite database
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    # Add an if not statement to determine starting and ending date
    # Unravel the results into a one dimensional array, and convert to a list
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
    # Calculate the temperature minimum, average, and maximum with the start and end dates
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
    

