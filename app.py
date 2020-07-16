import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flash import Flask, jsonify

###############################
# Database Setup
###############################

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
#reflect the tables
Base.prepared(engine,flected=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.Station

# Create our session from python to the DB
session = Session(engine)


###############################
# Flask Setup
###############################
app = Flask(__name__)

@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:<br/>
    /api/v1.0/precipitation
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end<br/>
    ''')

    @app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data for the last year"""
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()

    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)


@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations """
    results = session.query(Station.station.all()

    stations = list(np.ravel (results))

    return jsonify(stations=stations) # { stations: ()}

@app.route("/api/v1.0/tobs")
def temp_monthly():
    """Return the temp observation for previous year """
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    results = session.query(Measurement.tobs).\
        filter(Measurement.Station == 'USC0051928').\
        filter(Measurement.date >= previous_year).all()

    # unravel results into 1D list and convert to a python
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")  
def stats(start =None, end=None):

    sell = (func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))

    #calculate TMIN TAVG TMAX with start 
    if not end:
        results = session.query(*sell).\
            filter(Measurement.date >=start).all()
        temps = list(np.ravel (results)
        return jsonify(temps)

    #calculate TMIN TAVG TMAX with start and stop
    results = session.query(*sell).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()

    temps = list(np.ravel(results))
    return jsonify(temps)


    
    
    
    if_name_ "" '_main_':
        app.run(debug=false)

