import pandas as pd
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
from mysql_conn import password
import sys

# sys.path.append("../Data")


def run_db():
    price_agg = pd.read_csv(r'/price_agg.csv', encoding='latin-1')
    metro_group = pd.read_csv('../Data/metro_group.csv')
    sales_group_mean = pd.read_csv('../Data/sales_group_mean.csv')
    sales_group_median = pd.read_csv('../Data/sales_group_median.csv')


    connection_string = (f"root:{password}@localhost")

    engine = create_engine(f"mysql://{connection_string}")
    engine.execute("DROP DATABASE IF EXISTS real_estate")
    engine.execute("CREATE DATABASE real_estate")

    engine.execute("USE real_estate")
    price_agg.to_sql(
        name = 'median_price_zip', con = engine,
        if_exists = 'replace', chunksize = 75)
    with engine.connect() as con:
        con.execute('ALTER TABLE `median_price_zip` ADD PRIMARY KEY (`index`);')

    engine.execute("USE real_estate") 
    sales_group_mean.to_sql(
        name = 'mean_sales_count', con = engine,
        if_exists = 'replace')
    with engine.connect() as con:
        con.execute('ALTER TABLE `mean_sales_count` ADD PRIMARY KEY (`index`);')

    engine.execute("USE real_estate") 
    sales_group_median.to_sql(
        name = 'median_sales_count', con = engine,
        if_exists = 'replace')
    with engine.connect() as con:
        con.execute('ALTER TABLE `median_sales_count` ADD PRIMARY KEY (`index`);')

    engine.execute("USE real_estate") 
    metro_group.to_sql(
        name = 'median_price_sqft', con = engine,
        if_exists = 'replace')
    with engine.connect() as con:
        con.execute('ALTER TABLE `median_price_sqft` ADD PRIMARY KEY (`index`);')