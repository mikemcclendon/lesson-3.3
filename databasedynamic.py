import sqlite3 as lite
import pandas as pd
import sys
s1 = sys.stdin.readline()

cities = (('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA'))

weather = (('New York City', 2013, 'July', 'January'),
('Boston', 2013, 'July', 'January'),
('Chicago', 2013, 'July', 'January'),
('Miami', 2013, 'August', 'January'),
('Dallas', 2013, 'July', 'January'),
('Seattle', 2013, 'July', 'January'),
('Portland', 2013, 'July', 'December'),
('San Francisco', 2013, 'September', 'December'),
('Los Angeles', 2013, 'September', 'December'))

con = lite.connect('getting_started.db')

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS cities;")
cur.execute("DROP TABLE IF EXISTS weather;")
cur.execute("CREATE TABLE weather (city, year, warm_month, cold_month);")
cur.execute("CREATE TABLE cities (name, state);")
cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
cur.executemany("INSERT INTO weather VALUES(?,?,?,?)", weather)
cur.execute("SELECT city, state, warm_month, cold_month FROM cities INNNER JOIN weather ON city = name;")

rows = cur.fetchall()
cols = [desc[0] for desc in cur.description]

df = pd.DataFrame(rows, columns=cols)
filterdf = df.loc[df.warm_month == s1.strip()]
locationlist = []

for index, row in filterdf.iterrows():
	locationlist.append(row['city'] + ', ' + row['state'] + ', ')

locationstring = ''.join(locationlist)
	
print('The cities with the warmest ' +s1 +' are ' + str(locationstring) + '.')
	