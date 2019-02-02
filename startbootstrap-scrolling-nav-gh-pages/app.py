from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, jsonify,render_template
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from mysql_conn import password
import numpy as np
import pymysql
pymysql.install_as_MySQLdb()

connection_string = (f"root:{password}@localhost/real_estate")
engine = create_engine(f"mysql://{connection_string}")
#engine = create_engine('sqlite://cities.sqlite')


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
mean_sales_count = Base.classes.mean_sales_count
median_sales_count = Base.classes.median_sales_count
median_price_sqft = Base.classes.median_price_sqft
median_price_zip = Base.classes.median_price_zip
print(Base.classes.keys())

# Create our connection object
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def home():
    
    return render_template("index.html")

#  Define main behavior
if __name__ == "__main__":
    app.run(debug=True)