import psycopg2
import psycopg2 as pg
import pandas as pd
import pandas.io.sql as psql
from IPython import display
import matplotlib.image as mpimg
from matplotlib import rcParams
import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import MarkerCluster
import csv

# Access to Postgres
con = psycopg2.connect(database="store_database", user="cindy", password="Flamingosis01.", host="localhost",
                       port="5432")
cur = con.cursor()

#Importing tables from Postgres

pd.DataFrame(psql.read_sql("SELECT * FROM stores", con))  # Displaying raw data from dable 'stores'

pd.DataFrame(psql.read_sql("SELECT * FROM items", con))  # Displaying framed table 'items'

pd.DataFrame(psql.read_sql("SELECT * FROM categories", con))  # Displaying framed table 'categories'

#Joinng 'categories' and 'store_items' tables

psql.read_sql("""
  SELECT categories.id, categories.name, store_items.item_id, store_items.store_id
  FROM categories AS categories
  LEFT JOIN store_items AS store_items ON categories.parent_id = store_items.store_id
;""", con)

#Joinng 'opening times' and 'opening times exceptions' tables

pd.DataFrame(psql.read_sql("""
SELECT
    opening_times.store_id, 
    opening_times.monday, 
    opening_times.tuesday, 
    opening_times.wednesday, 
    opening_times.thursday, 
    opening_times.friday, 
    opening_times.saturday, 
    opening_times.sunday, 
    opening_time_exceptions.date,
    opening_time_exceptions.time      
FROM opening_times 
JOIN opening_time_exceptions ON opening_times.store_id = opening_time_exceptions.store_id 
""", con))

 # Displaying joined framed tables 'items' and 'stores'

pd.DataFrame(psql.read_sql("""
SELECT 
    stores.name , 
    items.name 
FROM items 
JOIN stores ON stores.id = stores.id 
INNER JOIN store_items ON store_items.item_id = items.id;
""", con)) 

# Displaying pictures
# read images
img_A = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod.jpeg")
img_B = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod (1).jpeg")
img_C = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod (2).jpeg")
img_D = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod (3).jpeg")
img_E = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod (5).jpeg")
img_F = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod (6).jpeg")
img_G = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod (7).jpeg")
img_H = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod (8).jpeg")

ax = plt.subplots(1, 2)
ax[0].imshow(img_A),
ax[1].imshow(img_B),

ax = plt.subplots(1, 2)
ax[0].imshow(img_C),
ax[1].imshow(img_D),

ax = plt.subplots(1, 2)
ax[0].imshow(img_E),
ax[1].imshow(img_F),

ax = plt.subplots(1, 2)
ax[0].imshow(img_G),
ax[1].imshow(img_H),


def path_to_image_html(path):
    return '<img src="' + path + '" width="60" >'


pd.set_option('display.max_colwidth', None)

image_cols = ['imageUrls', 'otherImageUrls']

# Create the dictionariy to be passed as formatters
format_dict = {}
for image_col in image_cols:
    format_dict[image_col] = path_to_image_html
    
#Joining 'stores' and 'categories' tables

pd.DataFrame(psql.read_sql("""
SELECT stores.name , 
    categories.name 
FROM categories 
INNER JOIN stores ON stores.id = stores.id 
INNER JOIN store_categories ON store_categories.categories_id = categories.id;"""
                           , con))

# Displaying joined framed tables 'stores' and 'categories' through a map

pd.DataFrame(psql.read_sql("""

SELECT stores_locations.name, 
    latitude_longitude_nl.city ,
    latitude_longitude_nl.lat,
    latitude_longitude_nl.lng,
    latitude_longitude_nl.admin_name 
FROM latitude_longitude_nl 
INNER JOIN join_store_locations ON join_store_locations.store_id  = latitude_longitude_nl.city_id
INNER JOIN stores_locations ON join_store_locations.store_id  = stores_locations.id """
                           , con))


m_1 = folium.Map(location=[52.370216, 4.895168], tiles='openstreetmap', zoom_start=10)

# Find stores location
stores_data = pd.read_csv(
    '/Users/cindymendoncapaez/opt/anaconda3/lib/python3.8/site-packages/folium/join_table_stores_loc.csv')

# Drop rows with missing locations
stores_data.dropna(subset=['id', 'lat', 'lng'], inplace=True)

# Print the first five rows of the table
stores_data.head()

for index, row in stores_data.iterrows():
    lat = row["lat"]
    lon = row["lng"]
    name = row["store"]
    postal_code = row["postal_code"]
    map_displayed_info = '{}  {}'.format(name, postal_code)
    folium.Marker([lat, lon], popup=map_displayed_info).add_to(m_1)
    print(m_1)


# find categories in stores trough a map

find_categories = pd.read_csv(
    '/Users/cindymendoncapaez/opt/anaconda3/lib/python3.8/site-packages/folium/find_categories.csv')

# Drop rows with missing locations
find_categories.dropna(subset=['lat', 'lng'], inplace=True)

# Print the first five rows of the table
find_categories.head()

m_2 = folium.Map(location=[52.370216, 4.895168], tiles='openstreetmap', zoom_start=10)

for index, row in find_categories.iterrows():
    lat = row["lat"]
    lon = row["lng"]
    name = row["store"]
    categories = row["category"]
    map_displayed_info1 = '{} : {}'.format(name, categories)
    folium.Marker([lat, lon], popup=map_displayed_info1).add_to(m_2)
    print(m_2)


pd.DataFrame(psql.read_sql("""
SELECT join_item_stores.id,
    join_item_stores.item,
    join_item_stores.store,
    join_item_stores.city, 
    join_item_stores.postal_code, 
    join_item_stores.lat, 
    join_item_stores.lng 
FROM join_item_stores 
WHERE  join_item_stores.item = 'Long Fit T-shirt' 
GROUP BY join_item_stores.id, 
    join_item_stores.item, 
    join_item_stores.store,
    join_item_stores.city, 
    join_item_stores.postal_code, 
    join_item_stores.lat, 
    join_item_stores.lng"""
                           , con))

df.to_csv('join_item_stores.csv', index=False, header=False)

# find item in stores through a map

find_items = pd.read_csv(
    '/Users/cindymendoncapaez/opt/anaconda3/lib/python3.8/site-packages/folium/join_item_stores.csv')

# Drop rows with missing locations
find_items.dropna(subset=['lat', 'lng'], inplace=True)

# Print the first five rows of the table
find_items.head()

m_3 =folium.Map(location=[52.370216, 4.895168], tiles='openstreetmap', zoom_start=10)

for index, row in find_items.iterrows():
    lat = row["lat"]
    lon = row["lng"]
    name = row["store"]
    items = row["item"]
    map_displayed_info2 = '{} : {}'.format(name, items)
    folium.Marker([lat, lon], popup=map_displayed_info2).add_to(m_3)
    print (m_3)

print("Database opened successfully")
