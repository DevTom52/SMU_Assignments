# import dependencies
from flask import Flask, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import sqlalchemy
import datetime as dt
import numpy as np
import pandas as pd

#create engine
engine = create_engine("sqlite:///Hawaii.sqlite")

# reflect database using automap base
Base = automap_base()

# reflect tables in sqlite file
Base.prepare(engine, reflect=True)

# Save station andmeasurements class to variables
Station = Base.classes.station
Measurements = Base.classes.measurements

# Create session in order to query db
session = Session(engine)

#create flask app
app = Flask(__name__)

#creat homepage route and show avaiable route options
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>" 
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

#create precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():

    #query precipitation measurement in descending order
    last_date = session.query(Measurements.date).order_by(Measurements.date.desc()).first()
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

@app.route("/api/v1.0/stations")
def stations():


@app.route("/api/v1.0/tobs")
def tobs():


@app.route("/api/v1.0/<start>")
def tripOne(start):

@app.route("/api/v1.0/<start>/<end>")
def tripTwo(start,end):

if __name__ == "__main__":
    app.run(debug=True)