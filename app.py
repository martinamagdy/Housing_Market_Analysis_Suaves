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

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
mean_sales_count = Base.classes.mean_sales_count
median_sales_count = Base.classes.median_sales_count
median_price_sqft = Base.classes.median_price_sqft
#median_price_zip = Base.classes.median_price_zip
print(Base.classes.keys())

# Create our connection object
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def apps():
    # Perform a query to retrieve all apps
    #all_apps = session.query(Apps.name).limit(20).all()
    #apps=[]
    #for app in all_apps:
     #   s=str(app).split("'")
      #  apps.append(s[1])
    return render_template("index.html")


@app.route("/info/<name>")
def info(name):
    # Perform a query to retrieve all apps
    all_apps = session.query(Apps.name).limit(20).all()
    apps=[]
    for app in all_apps:
        s=str(app).split("'")
        apps.append(s[1])

    category = session.query(Apps.a_category).filter(Apps.name == name).all()
    c=str(category).split("'")
    category = c[1]
    apple = session.query(Apps.a_price, Apps.a_user_rating, Apps.a_size_mb, Apps.a_content_rating).\
                               filter(Apps.name == name).all()
    a=str(apple).split(",")
    apple_info=[]
    z=0
    n=0
    for aapp in a:
        apple_info.append(a[z])
        z=z+1

    google = session.query(Apps.g_price, Apps.g_user_rating, Apps.g_size_mb, Apps.g_content_rating).\
                               filter(Apps.name == name).all()   
    g=str(google).split(",")
    google_info=[]
    for gapp in g:
        google_info.append(g[n])
        n=n+1

    return render_template("Apps.html", name=name,apple_info=apple_info,google_info=google_info, category=category,apps=apps)

@app.route("/api/available")
def available():
    return (
        "<img src=\"https://img.etimg.com/thumb/msid-46065787,width-300,imgsize-83533,resizemode-4/7-things-mobile-app-developers-should-focus-on.jpg\" alt=\"apps\" width=\"800\" height=\"300\"/>"+
        "<br/>"+
        "<br/>"+
        "Available Routes:<br/>" +
        "<br/>"+
        "<a href=\"/api/routes\">/api/routes</a><br/>"+
        "Return a list of all apps<br/>"+
        "<br/>"+
        "/api/{app_name}<br/>"+
        "return apple and android info about certain app<br/>"+
        "<a href=\"/\">Return To Home page</a>"
          )

@app.route("/api/routes")
def routes():
    app_api = session.query(Apps.name,Apps.a_category,
                           Apps.a_price, Apps.a_user_rating, Apps.a_size_mb, Apps.a_content_rating,
                           Apps.g_price, Apps.g_user_rating, Apps.g_size_mb, Apps.g_content_rating).all() 
    return jsonify(app_api)

@app.route("/api/<name>")
def JSON_data(name):
    app_dict = {}
    app_dict["AppleInfo"] = {}
    app_dict["AndroidInfo"] = {}

    app_dict["name"] = name
    app_dict["category"] = (session.query(
        Apps.a_category).
        filter(Apps.name == name).all())

    apple_data = (session.query(
        Apps.a_price, 
        Apps.a_user_rating, 
        Apps.a_size_mb, 
        Apps.a_content_rating).
        filter(Apps.name == name).all())
    android_data = (session.query(
        Apps.g_price, 
        Apps.g_user_rating, 
        Apps.g_size_mb, 
        Apps.g_content_rating).
        filter(Apps.name == name).all())

    dirty_apples = list(np.ravel(apple_data))
    dirty_googles = list(np.ravel(android_data))

    apples = []
    googles = []

    for item in dirty_apples:
        apples.append(str(item))
    for item in dirty_googles:
        googles.append(str(item))
        
    app_dict = { 
        "name": name,
        "category": (session.query(Apps.a_category).filter(Apps.name == name).all()),
        'AppleInfo': {
            'Price': apples[0],
            'UserRating': apples[1],
            'FileSize': apples[2],
            'ContentRating': apples[3] 
                    },
        'AndroidInfo': {
            'Price': googles[0],
            'UserRating': googles[1],
            'FileSize': googles[2],
            'ContentRating': googles[3]
                    
                    }
    }
    return jsonify(app_dict)

@app.route("/names")
def names():
    """Return list of available cities"""
    available_cities = ['Austin, TX', 
                'Dallas-Forth Worth, TX', 
                'Denver, CO', 
                'Detroit, MI', 
                'New York City, NY', 
                'Orlando, FL', 
                'Raleigh-Durham, NC', 
                'San Francisco, CA', 
                'Seattle, WA', 
                'Washington D.C']
    return jsonify(available_cities)

@app.route("/cities")
def cities():
    """Return stats for each city for all available years"""
    #stmt = db.session.query(Samples).statement
    #df = pd.read_sql_query(stmt, db.session.bind)

    # Filter the data based on the sample number and
    # only keep rows with values above 1
    #sample_data = df.loc[df[sample] > 1, ["otu_id", "otu_label", sample]]
    # Format the data to send as json

#mean_sales_count = Base.classes.mean_sales_count
#median_sales_count = Base.classes.median_sales_count
#median_price_sqft = Base.classes.median_price_sqft
#median_price_zip = Base.classes.median_price_zip

    city_dict = {}
    results = (session.query(mean_sales_count.Metro).all())
    city_list = list(np.ravel(results))
    print(city_list)
    city_ST = {'Austin-Round Rock': 'Austin, TX', 
                'Dallas-Fort Worth-Arlington': 'Dallas-Forth Worth, TX', 
                'Denver-Aurora-Lakewood': 'Denver, CO', 
                'Detroit-Warren-Dearborn': 'Detroit, MI', 
                'New York-Newark-Jersey City': 'New York City, NY', 
                'Orlando-Kissimmee-Sanford': 'Orlando, FL', 
                'Raleigh-Durham-Chapel Hill': 'Raleigh-Durham, NC', 
                'San Francisco-Oakland-Hayward': 'San Francisco, CA', 
                'Seattle-Tacoma-Bellevue': 'Seattle, WA', 
                'Washington-Arlington-Alexandria': 'Washington D.C'}
    for city in city_list:
        mean_results = ((session.query(mean_sales_count._2008,
                        mean_sales_count._2009,
                        mean_sales_count._2010,
                        mean_sales_count._2011,
                        mean_sales_count._2012,
                        mean_sales_count._2013,
                        mean_sales_count._2014,
                        mean_sales_count._2015,
                        mean_sales_count._2016,
                        mean_sales_count._2017,
                        mean_sales_count._2018
                        )).
                        filter(mean_sales_count.Metro == city).all())
        mean_results_list = list(np.ravel(mean_results))       
        median_results = ((session.query(median_sales_count._2008,
                        median_sales_count._2009,
                        median_sales_count._2010,
                        median_sales_count._2011,
                        median_sales_count._2012,
                        median_sales_count._2013,
                        median_sales_count._2014,
                        median_sales_count._2015,
                        median_sales_count._2016,
                        median_sales_count._2017,
                        median_sales_count._2018
                        )).
                        filter(median_sales_count.Metro == city).all())
        median_results_list = list(np.ravel(median_results))  
        sqft_results = ((session.query(median_price_sqft._1996,
                        median_price_sqft._1997,
                        median_price_sqft._1998,
                        median_price_sqft._1999,
                        median_price_sqft._2000,
                        median_price_sqft._2001,
                        median_price_sqft._2002,
                        median_price_sqft._2003,
                        median_price_sqft._2004,
                        median_price_sqft._2005,
                        median_price_sqft._2006,
                        median_price_sqft._2007,
                        median_price_sqft._2008,
                        median_price_sqft._2009,
                        median_price_sqft._2010,
                        median_price_sqft._2011,
                        median_price_sqft._2012,
                        median_price_sqft._2013,
                        median_price_sqft._2014,
                        median_price_sqft._2015,
                        median_price_sqft._2016,
                        median_price_sqft._2017,
                        median_price_sqft._2018
                        )).
                        filter(median_price_sqft.Metro == city).all())
        sqft_results_list = list(np.ravel(sqft_results))  
        city_dict[city_ST[city]] = {
            "Metro Area": city,
            "Mean Sales Per Year": {
                "2008": str(mean_results_list[0]),
                "2009": str(mean_results_list[1]),
                "2010": str(mean_results_list[2]),
                "2011": str(mean_results_list[3]),
                "2012": str(mean_results_list[4]),
                "2013": str(mean_results_list[5]),
                "2014": str(mean_results_list[6]),
                "2015": str(mean_results_list[7]),
                "2016": str(mean_results_list[8]),
                "2017": str(mean_results_list[9]),
                "2018": str(mean_results_list[10])
            },
            "Median Sales Per Year": {
                "2008": str(median_results_list[0]),
                "2009": str(median_results_list[1]),
                "2010": str(median_results_list[2]),
                "2011": str(median_results_list[3]),
                "2012": str(median_results_list[4]),
                "2013": str(median_results_list[5]),
                "2014": str(median_results_list[6]),
                "2015": str(median_results_list[7]),
                "2016": str(median_results_list[8]),
                "2017": str(median_results_list[9]),
                "2018": str(median_results_list[10])
            },
            "Median Price Per Square Foot": {
                "1996": str(sqft_results_list[0]),
                "1997": str(sqft_results_list[1]),
                "1998": str(sqft_results_list[2]),
                "1999": str(sqft_results_list[3]),
                "2000": str(sqft_results_list[4]),
                "2001": str(sqft_results_list[5]),
                "2002": str(sqft_results_list[6]),
                "2003": str(sqft_results_list[7]),
                "2004": str(sqft_results_list[8]),
                "2005": str(sqft_results_list[9]),
                "2006": str(sqft_results_list[10]),
                "2007": str(sqft_results_list[11]),
                "2008": str(sqft_results_list[12]),
                "2009": str(sqft_results_list[13]),
                "2010": str(sqft_results_list[14]),
                "2011": str(sqft_results_list[15]),
                "2012": str(sqft_results_list[16]),
                "2013": str(sqft_results_list[17]),
                "2014": str(sqft_results_list[18]),
                "2015": str(sqft_results_list[19]),
                "2016": str(sqft_results_list[20]),
                "2017": str(sqft_results_list[21]),
                "2018": str(sqft_results_list[22])
            }
        }
    return jsonify(city_dict)

#  Define main behavior
if __name__ == "__main__":
    app.run(debug=True)