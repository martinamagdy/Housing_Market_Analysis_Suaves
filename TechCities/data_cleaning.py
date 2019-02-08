import pandas as pd
from sqlalchemy import create_engine
#import requests
#import json
import pymysql
pymysql.install_as_MySQLdb()
from mysql_conn import password
import os

# Change working directory to file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# # SQFT Dataset

sqft_raw = pd.read_csv('Raw_Data/City_MedianValuePerSqft_AllHomes.csv', encoding = 'latin-1')
#sqft_raw.head()


# Grab only rows for specified metropolitan areas
cities = ['Seattle', 'Washington', 'Detroit', 'Denver', 'Austin', 'San Francisco', 
          'Dallas', 'New York', 'Orlando', 'Raleigh', 'Durham']
metro_index = []
for city in cities:
    metro_index.append(sqft_raw.index[sqft_raw['Metro'].str.contains(city, na = False)].tolist())
    


metro_index = [item for sublist in metro_index for item in sublist]

sqft_metro = sqft_raw.iloc[metro_index]
#sqft_metro.head()


# Set up Raleigh-Durham-Chapel Hill area
sqft_metro['Metro'] = sqft_metro['Metro'].replace(['Durham-Chapel Hill', 'Raleigh'], 'Raleigh-Durham-Chapel Hill')


#Group regions under each metro area
metro_group = sqft_metro.groupby('Metro').mean()
metro_group.drop(index = ['Washington Court House', 'Austin'], columns = ['RegionID', 'SizeRank'], inplace = True)
metro_group.reset_index(inplace = True)
#metro_group



metro_group['_1996'] = (metro_group['1996-04'] + metro_group['1996-05'] + metro_group['1996-06'] + 
                          metro_group['1996-07'] + metro_group['1996-08'] + metro_group['1996-09'] + 
                          metro_group['1996-10'] + metro_group['1996-11'] + metro_group['1996-12'])/9
metro_group['_1997'] = (metro_group['1997-01'] + metro_group['1997-02'] + metro_group['1997-03'] + 
                          metro_group['1997-04'] + metro_group['1997-05'] + metro_group['1997-06'] + 
                          metro_group['1997-07'] + metro_group['1997-08'] + metro_group['1997-09'] + 
                          metro_group['1997-10'] + metro_group['1997-11'] + metro_group['1997-12'])/12
metro_group['_1998'] = (metro_group['1998-01'] + metro_group['1998-02'] + metro_group['1998-03'] + 
                          metro_group['1998-04'] + metro_group['1998-05'] + metro_group['1998-06'] + 
                          metro_group['1998-07'] + metro_group['1998-08'] + metro_group['1998-09'] + 
                          metro_group['1998-10'] + metro_group['1998-11'] + metro_group['1998-12'])/12
metro_group['_1999'] = (metro_group['1999-01'] + metro_group['1999-02'] + metro_group['1999-03'] + 
                          metro_group['1999-04'] + metro_group['1999-05'] + metro_group['1999-06'] + 
                          metro_group['1999-07'] + metro_group['1999-08'] + metro_group['1999-09'] + 
                          metro_group['1999-10'] + metro_group['1999-11'] + metro_group['1999-12'])/12
metro_group['_2000'] = (metro_group['2000-01'] + metro_group['2000-02'] + metro_group['2000-03'] + 
                          metro_group['2000-04'] + metro_group['2000-05'] + metro_group['2000-06'] + 
                          metro_group['2000-07'] + metro_group['2000-08'] + metro_group['2000-09'] + 
                          metro_group['2000-10'] + metro_group['2000-11'] + metro_group['2000-12'])/12
metro_group['_2001'] = (metro_group['2001-01'] + metro_group['2001-02'] + metro_group['2001-03'] + 
                          metro_group['2001-04'] + metro_group['2001-05'] + metro_group['2001-06'] + 
                          metro_group['2001-07'] + metro_group['2001-08'] + metro_group['2001-09'] + 
                          metro_group['2001-10'] + metro_group['2001-11'] + metro_group['2001-12'])/12
metro_group['_2002'] = (metro_group['2002-01'] + metro_group['2002-02'] + metro_group['2002-03'] + 
                          metro_group['2002-04'] + metro_group['2002-05'] + metro_group['2002-06'] + 
                          metro_group['2002-07'] + metro_group['2002-08'] + metro_group['2002-09'] + 
                          metro_group['2002-10'] + metro_group['2002-11'] + metro_group['2002-12'])/12
metro_group['_2003'] = (metro_group['2003-01'] + metro_group['2003-02'] + metro_group['2003-03'] + 
                          metro_group['2003-04'] + metro_group['2003-05'] + metro_group['2003-06'] + 
                          metro_group['2003-07'] + metro_group['2003-08'] + metro_group['2003-09'] + 
                          metro_group['2003-10'] + metro_group['2003-11'] + metro_group['2003-12'])/12
metro_group['_2004'] = (metro_group['2004-01'] + metro_group['2004-02'] + metro_group['2004-03'] + 
                          metro_group['2004-04'] + metro_group['2004-05'] + metro_group['2004-06'] + 
                          metro_group['2004-07'] + metro_group['2004-08'] + metro_group['2004-09'] + 
                          metro_group['2004-10'] + metro_group['2004-11'] + metro_group['2004-12'])/12
metro_group['_2005'] = (metro_group['2005-01'] + metro_group['2005-02'] + metro_group['2005-03'] + 
                          metro_group['2005-04'] + metro_group['2005-05'] + metro_group['2005-06'] + 
                          metro_group['2005-07'] + metro_group['2005-08'] + metro_group['2005-09'] + 
                          metro_group['2005-10'] + metro_group['2005-11'] + metro_group['2005-12'])/12
metro_group['_2006'] = (metro_group['2006-01'] + metro_group['2006-02'] + metro_group['2006-03'] + 
                          metro_group['2006-04'] + metro_group['2006-05'] + metro_group['2006-06'] + 
                          metro_group['2006-07'] + metro_group['2006-08'] + metro_group['2006-09'] + 
                          metro_group['2006-10'] + metro_group['2006-11'] + metro_group['2006-12'])/12
metro_group['_2007'] = (metro_group['2007-01'] + metro_group['2007-02'] + metro_group['2007-03'] + 
                          metro_group['2007-04'] + metro_group['2007-05'] + metro_group['2007-06'] + 
                          metro_group['2007-07'] + metro_group['2007-08'] + metro_group['2007-09'] + 
                          metro_group['2007-10'] + metro_group['2007-11'] + metro_group['2007-12'])/12
metro_group['_2008'] = (metro_group['2008-01'] + metro_group['2008-02'] + metro_group['2008-03'] + 
                          metro_group['2008-04'] + metro_group['2008-05'] + metro_group['2008-06'] + 
                          metro_group['2008-07'] + metro_group['2008-08'] + metro_group['2008-09'] + 
                          metro_group['2008-10'] + metro_group['2008-11'] + metro_group['2008-12'])/12
metro_group['_2009'] = (metro_group['2009-01'] + metro_group['2009-02'] + metro_group['2009-03'] + 
                          metro_group['2009-04'] + metro_group['2009-05'] + metro_group['2009-06'] + 
                          metro_group['2009-07'] + metro_group['2009-08'] + metro_group['2009-09'] + 
                          metro_group['2009-10'] + metro_group['2009-11'] + metro_group['2009-12'])/12
metro_group['_2010'] = (metro_group['2010-01'] + metro_group['2010-02'] + metro_group['2010-03'] + 
                          metro_group['2010-04'] + metro_group['2010-05'] + metro_group['2010-06'] + 
                          metro_group['2010-07'] + metro_group['2010-08'] + metro_group['2010-09'] + 
                          metro_group['2010-10'] + metro_group['2010-11'] + metro_group['2010-12'])/12
metro_group['_2011'] = (metro_group['2011-01'] + metro_group['2011-02'] + metro_group['2011-03'] + 
                          metro_group['2011-04'] + metro_group['2011-05'] + metro_group['2011-06'] + 
                          metro_group['2011-07'] + metro_group['2011-08'] + metro_group['2011-09'] + 
                          metro_group['2011-10'] + metro_group['2011-11'] + metro_group['2011-12'])/12
metro_group['_2012'] = (metro_group['2012-01'] + metro_group['2012-02'] + metro_group['2012-03'] + 
                          metro_group['2012-04'] + metro_group['2012-05'] + metro_group['2012-06'] + 
                          metro_group['2012-07'] + metro_group['2012-08'] + metro_group['2012-09'] + 
                          metro_group['2012-10'] + metro_group['2012-11'] + metro_group['2012-12'])/12
metro_group['_2013'] = (metro_group['2013-01'] + metro_group['2013-02'] + metro_group['2013-03'] + 
                          metro_group['2013-04'] + metro_group['2013-05'] + metro_group['2013-06'] + 
                          metro_group['2013-07'] + metro_group['2013-08'] + metro_group['2013-09'] + 
                          metro_group['2013-10'] + metro_group['2013-11'] + metro_group['2013-12'])/12
metro_group['_2014'] = (metro_group['2014-01'] + metro_group['2014-02'] + metro_group['2014-03'] + 
                          metro_group['2014-04'] + metro_group['2014-05'] + metro_group['2014-06'] + 
                          metro_group['2014-07'] + metro_group['2014-08'] + metro_group['2014-09'] + 
                          metro_group['2014-10'] + metro_group['2014-11'] + metro_group['2014-12'])/12
metro_group['_2015'] = (metro_group['2015-01'] + metro_group['2015-02'] + metro_group['2015-03'] + 
                          metro_group['2015-04'] + metro_group['2015-05'] + metro_group['2015-06'] + 
                          metro_group['2015-07'] + metro_group['2015-08'] + metro_group['2015-09'] + 
                          metro_group['2015-10'] + metro_group['2015-11'] + metro_group['2015-12'])/12
metro_group['_2016'] = (metro_group['2016-01'] + metro_group['2016-02'] + metro_group['2016-03'] + 
                          metro_group['2016-04'] + metro_group['2016-05'] + metro_group['2016-06'] + 
                          metro_group['2016-07'] + metro_group['2016-08'] + metro_group['2016-09'] + 
                          metro_group['2016-10'] + metro_group['2016-11'] + metro_group['2016-12'])/12
metro_group['_2017'] = (metro_group['2017-01'] + metro_group['2017-02'] + metro_group['2017-03'] + 
                          metro_group['2017-04'] + metro_group['2017-05'] + metro_group['2017-06'] + 
                          metro_group['2017-07'] + metro_group['2017-08'] + metro_group['2017-09'] + 
                          metro_group['2017-10'] + metro_group['2017-11'] + metro_group['2017-12'])/12
metro_group['_2018'] = (metro_group['2018-01'] + metro_group['2018-02'] + metro_group['2018-03'] + 
                          metro_group['2018-04'] + metro_group['2018-05'] + metro_group['2018-06'] + 
                          metro_group['2018-07'] + metro_group['2018-08'] + metro_group['2018-09'] + 
                          metro_group['2018-10'] + metro_group['2018-11'] + metro_group['2018-12'])/12
#metro_group.head()


# # Sales Count Dataset

us_state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
    'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
    'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
    'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY',
    'District of Columbia': 'DC'
}



sales_raw = pd.read_csv('Raw_Data/Sale_Counts_Seas_Adj_City.csv', encoding = 'latin-1')
#sales_raw.head()



# Change state names to abbreviations
sales_raw = sales_raw.replace({'StateName' : us_state_abbrev})



# Group regions into their metropolitan areas
sales_raw['RegionID'] = sales_raw['RegionID'].astype(int).astype(str)
sqft_metro['RegionID'] = sqft_metro['RegionID'].astype(str)

sales = list(sqft_metro['RegionID'])

sales_index = []
for sale in sales:
  if len(sales_raw.loc[sales_raw['RegionID'] == sale].index) > 0:
    sales_index.append(sales_raw.loc[sales_raw['RegionID'] == sale].index[0])

sales_metro = sales_raw.iloc[sales_index]



# Generate list of metro area names
metro_names = list(sqft_metro.Metro.unique())
metro_names.remove('Washington Court House')
metro_names.remove('Austin')

metro_names = ['Seattle-Tacoma-Bellevue',
 'Washington-Arlington-Alexandria',
 'Detroit-Warren-Dearborn',
 'Denver-Aurora-Lakewood',
 'Austin-Round Rock',
 'Orlando-Kissimmee-Sanford',
 'Raleigh-Durham-Chapel Hill', 'Dallas-Fort Worth-Arlington', 'San Francisco-Oakland-Hayward', 'New York-Newark-Jersey City']



# Dictionary of metro aread and states
metro_agg = []
for i in range(0, len(metro_names)):
    state = list(sqft_metro.loc[sqft_metro.Metro == metro_names[i]].State.unique())
    metro_agg.append({metro_names[i] : state})

#metro_agg



sales_agg = pd.DataFrame()
WA_cities = []
for i in range(0, len(metro_names)):
    for j in range(0, len(metro_agg[i][metro_names[i]])):
        WA_sales = sales_metro.loc[sales_metro.StateName == metro_agg[i][metro_names[i]][j]]
        WA_metro = sqft_metro.loc[sqft_metro.State == metro_agg[i][metro_names[i]][j]]
        for value in WA_sales.RegionName.unique():
            if value in WA_metro.RegionName.unique() and (list((WA_metro.loc[WA_metro.RegionName == value].Metro) == metro_names[i])[0]):
                WA_cities.append(value)
#         WA_cities = [value for value in WA_sales.RegionName.unique() if (value in WA_metro.RegionName.unique()) and (WA_metro.Metro == metro_names[i])]

        # RegionID for every city in Seattle metro area
        WA_agg = WA_sales.loc[sales_metro['RegionName'].isin(WA_cities)]
        WA_agg['Metro'] = metro_names[i]
        sales_agg = sales_agg.append(WA_agg, ignore_index = True)
#sales_agg.head()



list((WA_metro.loc[WA_metro.RegionName == value].Metro) == metro_names[i])[0]



sales_group_mean = sales_agg.groupby('Metro').mean()
sales_group_mean.drop(columns = ['SizeRank'], inplace = True)
sales_group_mean.reset_index(inplace = True)
#sales_group_mean



sales_group_mean['_2008'] = (sales_group_mean['2008-03'] + sales_group_mean['2008-04'] + sales_group_mean['2008-05'] +
                         sales_group_mean['2008-06'] + sales_group_mean['2008-07'] + sales_group_mean['2008-08'] +
                         sales_group_mean['2008-09'] + sales_group_mean['2008-10'] + sales_group_mean['2008-11'] +
                         sales_group_mean['2008-12'])
sales_group_mean['_2009'] = (sales_group_mean['2009-01'] + sales_group_mean['2009-02'] + sales_group_mean['2009-03'] + 
                          sales_group_mean['2009-04'] + sales_group_mean['2009-05'] + sales_group_mean['2009-06'] + 
                          sales_group_mean['2009-07'] + sales_group_mean['2009-08'] + sales_group_mean['2009-09'] + 
                          sales_group_mean['2009-10'] + sales_group_mean['2009-11'] + sales_group_mean['2009-12'])
sales_group_mean['_2010'] = (sales_group_mean['2010-01'] + sales_group_mean['2010-02'] + sales_group_mean['2010-03'] + 
                          sales_group_mean['2010-04'] + sales_group_mean['2010-05'] + sales_group_mean['2010-06'] + 
                          sales_group_mean['2010-07'] + sales_group_mean['2010-08'] + sales_group_mean['2010-09'] + 
                          sales_group_mean['2010-10'] + sales_group_mean['2010-11'] + sales_group_mean['2010-12'])
sales_group_mean['_2011'] = (sales_group_mean['2011-01'] + sales_group_mean['2011-02'] + sales_group_mean['2011-03'] + 
                          sales_group_mean['2011-04'] + sales_group_mean['2011-05'] + sales_group_mean['2011-06'] + 
                          sales_group_mean['2011-07'] + sales_group_mean['2011-08'] + sales_group_mean['2011-09'] + 
                          sales_group_mean['2011-10'] + sales_group_mean['2011-11'] + sales_group_mean['2011-12'])
sales_group_mean['_2012'] = (sales_group_mean['2012-01'] + sales_group_mean['2012-02'] + sales_group_mean['2012-03'] + 
                          sales_group_mean['2012-04'] + sales_group_mean['2012-05'] + sales_group_mean['2012-06'] + 
                          sales_group_mean['2012-07'] + sales_group_mean['2012-08'] + sales_group_mean['2012-09'] + 
                          sales_group_mean['2012-10'] + sales_group_mean['2012-11'] + sales_group_mean['2012-12'])
sales_group_mean['_2013'] = (sales_group_mean['2013-01'] + sales_group_mean['2013-02'] + sales_group_mean['2013-03'] + 
                          sales_group_mean['2013-04'] + sales_group_mean['2013-05'] + sales_group_mean['2013-06'] + 
                          sales_group_mean['2013-07'] + sales_group_mean['2013-08'] + sales_group_mean['2013-09'] + 
                          sales_group_mean['2013-10'] + sales_group_mean['2013-11'] + sales_group_mean['2013-12'])
sales_group_mean['_2014'] = (sales_group_mean['2014-01'] + sales_group_mean['2014-02'] + sales_group_mean['2014-03'] + 
                          sales_group_mean['2014-04'] + sales_group_mean['2014-05'] + sales_group_mean['2014-06'] + 
                          sales_group_mean['2014-07'] + sales_group_mean['2014-08'] + sales_group_mean['2014-09'] + 
                          sales_group_mean['2014-10'] + sales_group_mean['2014-11'] + sales_group_mean['2014-12'])
sales_group_mean['_2015'] = (sales_group_mean['2015-01'] + sales_group_mean['2015-02'] + sales_group_mean['2015-03'] + 
                          sales_group_mean['2015-04'] + sales_group_mean['2015-05'] + sales_group_mean['2015-06'] + 
                          sales_group_mean['2015-07'] + sales_group_mean['2015-08'] + sales_group_mean['2015-09'] + 
                          sales_group_mean['2015-10'] + sales_group_mean['2015-11'] + sales_group_mean['2015-12'])
sales_group_mean['_2016'] = (sales_group_mean['2016-01'] + sales_group_mean['2016-02'] + sales_group_mean['2016-03'] + 
                          sales_group_mean['2016-04'] + sales_group_mean['2016-05'] + sales_group_mean['2016-06'] + 
                          sales_group_mean['2016-07'] + sales_group_mean['2016-08'] + sales_group_mean['2016-09'] + 
                          sales_group_mean['2016-10'] + sales_group_mean['2016-11'] + sales_group_mean['2016-12'])
sales_group_mean['_2017'] = (sales_group_mean['2017-01'] + sales_group_mean['2017-02'] + sales_group_mean['2017-03'] + 
                          sales_group_mean['2017-04'] + sales_group_mean['2017-05'] + sales_group_mean['2017-06'] + 
                          sales_group_mean['2017-07'] + sales_group_mean['2017-08'] + sales_group_mean['2017-09'] + 
                          sales_group_mean['2017-10'] + sales_group_mean['2017-11'] + sales_group_mean['2017-12'])
sales_group_mean['_2018'] = (sales_group_mean['2018-01'] + sales_group_mean['2018-02'] + sales_group_mean['2018-03'] + 
                          sales_group_mean['2018-04'] + sales_group_mean['2018-05'] + sales_group_mean['2018-06'] + 
                          sales_group_mean['2018-07'] + sales_group_mean['2018-08'] + sales_group_mean['2018-09'] + 
                          sales_group_mean['2018-10'] + sales_group_mean['2018-11'] + sales_group_mean['2018-12'])
#sales_group_mean.head()



sales_group_median = sales_agg.groupby('Metro').median()
sales_group_median.drop(columns = ['SizeRank'], inplace = True)
sales_group_median.reset_index(inplace = True)
#sales_group_median



sales_group_median['_2008'] = (sales_group_median['2008-03'] + sales_group_median['2008-04'] + sales_group_median['2008-05'] +
                         sales_group_median['2008-06'] + sales_group_median['2008-07'] + sales_group_median['2008-08'] +
                         sales_group_median['2008-09'] + sales_group_median['2008-10'] + sales_group_median['2008-11'] +
                         sales_group_median['2008-12'])
sales_group_median['_2009'] = (sales_group_median['2009-01'] + sales_group_median['2009-02'] + sales_group_median['2009-03'] + 
                          sales_group_median['2009-04'] + sales_group_median['2009-05'] + sales_group_median['2009-06'] + 
                          sales_group_median['2009-07'] + sales_group_median['2009-08'] + sales_group_median['2009-09'] + 
                          sales_group_median['2009-10'] + sales_group_median['2009-11'] + sales_group_median['2009-12'])
sales_group_median['_2010'] = (sales_group_median['2010-01'] + sales_group_median['2010-02'] + sales_group_median['2010-03'] + 
                          sales_group_median['2010-04'] + sales_group_median['2010-05'] + sales_group_median['2010-06'] + 
                          sales_group_median['2010-07'] + sales_group_median['2010-08'] + sales_group_median['2010-09'] + 
                          sales_group_median['2010-10'] + sales_group_median['2010-11'] + sales_group_median['2010-12'])
sales_group_median['_2011'] = (sales_group_median['2011-01'] + sales_group_median['2011-02'] + sales_group_median['2011-03'] + 
                          sales_group_median['2011-04'] + sales_group_median['2011-05'] + sales_group_median['2011-06'] + 
                          sales_group_median['2011-07'] + sales_group_median['2011-08'] + sales_group_median['2011-09'] + 
                          sales_group_median['2011-10'] + sales_group_median['2011-11'] + sales_group_median['2011-12'])
sales_group_median['_2012'] = (sales_group_median['2012-01'] + sales_group_median['2012-02'] + sales_group_median['2012-03'] + 
                          sales_group_median['2012-04'] + sales_group_median['2012-05'] + sales_group_median['2012-06'] + 
                          sales_group_median['2012-07'] + sales_group_median['2012-08'] + sales_group_median['2012-09'] + 
                          sales_group_median['2012-10'] + sales_group_median['2012-11'] + sales_group_median['2012-12'])
sales_group_median['_2013'] = (sales_group_median['2013-01'] + sales_group_median['2013-02'] + sales_group_median['2013-03'] + 
                          sales_group_median['2013-04'] + sales_group_median['2013-05'] + sales_group_median['2013-06'] + 
                          sales_group_median['2013-07'] + sales_group_median['2013-08'] + sales_group_median['2013-09'] + 
                          sales_group_median['2013-10'] + sales_group_median['2013-11'] + sales_group_median['2013-12'])
sales_group_median['_2014'] = (sales_group_median['2014-01'] + sales_group_median['2014-02'] + sales_group_median['2014-03'] + 
                          sales_group_median['2014-04'] + sales_group_median['2014-05'] + sales_group_median['2014-06'] + 
                          sales_group_median['2014-07'] + sales_group_median['2014-08'] + sales_group_median['2014-09'] + 
                          sales_group_median['2014-10'] + sales_group_median['2014-11'] + sales_group_median['2014-12'])
sales_group_median['_2015'] = (sales_group_median['2015-01'] + sales_group_median['2015-02'] + sales_group_median['2015-03'] + 
                          sales_group_median['2015-04'] + sales_group_median['2015-05'] + sales_group_median['2015-06'] + 
                          sales_group_median['2015-07'] + sales_group_median['2015-08'] + sales_group_median['2015-09'] + 
                          sales_group_median['2015-10'] + sales_group_median['2015-11'] + sales_group_median['2015-12'])
sales_group_median['_2016'] = (sales_group_median['2016-01'] + sales_group_median['2016-02'] + sales_group_median['2016-03'] + 
                          sales_group_median['2016-04'] + sales_group_median['2016-05'] + sales_group_median['2016-06'] + 
                          sales_group_median['2016-07'] + sales_group_median['2016-08'] + sales_group_median['2016-09'] + 
                          sales_group_median['2016-10'] + sales_group_median['2016-11'] + sales_group_median['2016-12'])
sales_group_median['_2017'] = (sales_group_median['2017-01'] + sales_group_median['2017-02'] + sales_group_median['2017-03'] + 
                          sales_group_median['2017-04'] + sales_group_median['2017-05'] + sales_group_median['2017-06'] + 
                          sales_group_median['2017-07'] + sales_group_median['2017-08'] + sales_group_median['2017-09'] + 
                          sales_group_median['2017-10'] + sales_group_median['2017-11'] + sales_group_median['2017-12'])
sales_group_median['_2018'] = (sales_group_median['2018-01'] + sales_group_median['2018-02'] + sales_group_median['2018-03'] + 
                          sales_group_median['2018-04'] + sales_group_median['2018-05'] + sales_group_median['2018-06'] + 
                          sales_group_median['2018-07'] + sales_group_median['2018-08'] + sales_group_median['2018-09'] + 
                          sales_group_median['2018-10'] + sales_group_median['2018-11'] + sales_group_median['2018-12'])
#sales_group_median.head()


# # Median Sale Prices Dataset


price_raw = pd.read_csv('Raw_Data/Sale_Prices_Zip.csv', encoding = 'latin-1')
price_raw.rename(columns = {'RegionName':'ZipCode'}, inplace = True)
#price_raw.head()


# ### Aggregate list of zip codes by metro area


zip_raw = pd.read_csv('Raw_Data/Zip_Zhvi_AllHomes.csv', encoding = 'latin-1')
zip_raw.rename(columns = {'RegionName':'ZipCode'}, inplace = True)
#zip_raw.head()



# filter zip codes by metro area
zip_metro = zip_raw.loc[zip_raw['Metro'].isin(metro_names)]

# Create Realeigh-Durham-Chapel Hill area
zip_NC = zip_raw.loc[zip_raw['Metro'].isin(['Raleigh', 'Durham-Chapel Hill'])]
zip_NC['Metro'] = 'Raleigh-Durham-Chapel Hill'
zip_metro = zip_metro.append(zip_NC)

# Create dictionary of zip codes by metro area
zip_agg = []
for i in range(0, len(metro_names)):
    zip_agg.append({metro_names[i]:list((zip_metro.loc[zip_metro['Metro'] == metro_names[i]].ZipCode).values)})



price_agg = pd.DataFrame()

# metro area, all zips, single zip
for i in range(0, len(metro_names)):
    zipper = zip_agg[i][metro_names[i]]

    metro_zips = price_raw.loc[price_raw['ZipCode'].isin(zipper)]
    metro_zips['Metro'] = metro_names[i]
    price_agg = price_agg.append(metro_zips)
#price_agg.head()



price_agg = price_agg.groupby('Metro').mean()
price_agg.drop(columns = ['SizeRank', 'ZipCode', 'RegionID'], inplace = True)
price_agg.reset_index(inplace = True)
#price_agg



price_agg['_2008'] = (price_agg['2008-03'] + price_agg['2008-04'] + price_agg['2008-05'] +
                         price_agg['2008-06'] + price_agg['2008-07'] + price_agg['2008-08'] +
                         price_agg['2008-09'] + price_agg['2008-10'] + price_agg['2008-11'] +
                         price_agg['2008-12'])
price_agg['_2009'] = (price_agg['2009-01'] + price_agg['2009-02'] + price_agg['2009-03'] + 
                          price_agg['2009-04'] + price_agg['2009-05'] + price_agg['2009-06'] + 
                          price_agg['2009-07'] + price_agg['2009-08'] + price_agg['2009-09'] + 
                          price_agg['2009-10'] + price_agg['2009-11'] + price_agg['2009-12'])
price_agg['_2010'] = (price_agg['2010-01'] + price_agg['2010-02'] + price_agg['2010-03'] + 
                          price_agg['2010-04'] + price_agg['2010-05'] + price_agg['2010-06'] + 
                          price_agg['2010-07'] + price_agg['2010-08'] + price_agg['2010-09'] + 
                          price_agg['2010-10'] + price_agg['2010-11'] + price_agg['2010-12'])
price_agg['_2011'] = (price_agg['2011-01'] + price_agg['2011-02'] + price_agg['2011-03'] + 
                          price_agg['2011-04'] + price_agg['2011-05'] + price_agg['2011-06'] + 
                          price_agg['2011-07'] + price_agg['2011-08'] + price_agg['2011-09'] + 
                          price_agg['2011-10'] + price_agg['2011-11'] + price_agg['2011-12'])
price_agg['_2012'] = (price_agg['2012-01'] + price_agg['2012-02'] + price_agg['2012-03'] + 
                          price_agg['2012-04'] + price_agg['2012-05'] + price_agg['2012-06'] + 
                          price_agg['2012-07'] + price_agg['2012-08'] + price_agg['2012-09'] + 
                          price_agg['2012-10'] + price_agg['2012-11'] + price_agg['2012-12'])
price_agg['_2013'] = (price_agg['2013-01'] + price_agg['2013-02'] + price_agg['2013-03'] + 
                          price_agg['2013-04'] + price_agg['2013-05'] + price_agg['2013-06'] + 
                          price_agg['2013-07'] + price_agg['2013-08'] + price_agg['2013-09'] + 
                          price_agg['2013-10'] + price_agg['2013-11'] + price_agg['2013-12'])
price_agg['_2014'] = (price_agg['2014-01'] + price_agg['2014-02'] + price_agg['2014-03'] + 
                          price_agg['2014-04'] + price_agg['2014-05'] + price_agg['2014-06'] + 
                          price_agg['2014-07'] + price_agg['2014-08'] + price_agg['2014-09'] + 
                          price_agg['2014-10'] + price_agg['2014-11'] + price_agg['2014-12'])
price_agg['_2015'] = (price_agg['2015-01'] + price_agg['2015-02'] + price_agg['2015-03'] + 
                          price_agg['2015-04'] + price_agg['2015-05'] + price_agg['2015-06'] + 
                          price_agg['2015-07'] + price_agg['2015-08'] + price_agg['2015-09'] + 
                          price_agg['2015-10'] + price_agg['2015-11'] + price_agg['2015-12'])
price_agg['_2016'] = (price_agg['2016-01'] + price_agg['2016-02'] + price_agg['2016-03'] + 
                          price_agg['2016-04'] + price_agg['2016-05'] + price_agg['2016-06'] + 
                          price_agg['2016-07'] + price_agg['2016-08'] + price_agg['2016-09'] + 
                          price_agg['2016-10'] + price_agg['2016-11'] + price_agg['2016-12'])
price_agg['_2017'] = (price_agg['2017-01'] + price_agg['2017-02'] + price_agg['2017-03'] + 
                          price_agg['2017-04'] + price_agg['2017-05'] + price_agg['2017-06'] + 
                          price_agg['2017-07'] + price_agg['2017-08'] + price_agg['2017-09'] + 
                          price_agg['2017-10'] + price_agg['2017-11'] + price_agg['2017-12'])
price_agg['_2018'] = (price_agg['2018-01'] + price_agg['2018-02'] + price_agg['2018-03'] + 
                          price_agg['2018-04'] + price_agg['2018-05'] + price_agg['2018-06'] + 
                          price_agg['2018-07'] + price_agg['2018-08'] + price_agg['2018-09'] + 
                          price_agg['2018-10'] + price_agg['2018-11'] + price_agg['2018-12'])
price_agg['coordinates'] = ['30.26, -97.74','32.75, -97.33','39.73, -104.99',
                        '42.33, -83.04','40.71, -74.00','28.53, -81.37',
                        '35.77, -78.63','37.77, -122.41','47.60, -122.33','38.90, -77.03']
# price_agg.dropna(inplace = True)
# price_agg.head(10)


# # MySQL Connection


# Define database within MySQL client
connection_string = (f"root:{password}@localhost")

engine = create_engine(f"mysql://{connection_string}")
engine.execute("DROP DATABASE IF EXISTS real_estate")
engine.execute("CREATE DATABASE real_estate")



engine.execute("USE real_estate")
# engine.table_names()



engine.execute("USE real_estate")
price_agg.to_sql(
    name = 'median_price_zip', con = engine,
    if_exists = 'replace', chunksize = 75)
with engine.connect() as con:
    con.execute('ALTER TABLE `median_price_zip` ADD PRIMARY KEY (`index`);')



engine.execute("USE real_estate") # select new db
sales_group_mean.to_sql(
    name = 'mean_sales_count', con = engine,
    if_exists = 'replace')
with engine.connect() as con:
    con.execute('ALTER TABLE `mean_sales_count` ADD PRIMARY KEY (`index`);')



engine.execute("USE real_estate") # select new db
sales_group_median.to_sql(
    name = 'median_sales_count', con = engine,
    if_exists = 'replace')
with engine.connect() as con:
    con.execute('ALTER TABLE `median_sales_count` ADD PRIMARY KEY (`index`);')



engine.execute("USE real_estate") # select new db
metro_group.to_sql(
    name = 'median_price_sqft', con = engine,
    if_exists = 'replace')
with engine.connect() as con:
    con.execute('ALTER TABLE `median_price_sqft` ADD PRIMARY KEY (`index`);')

