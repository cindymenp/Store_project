# Store_project 

The store project is a database done with Postgresql, Python and Jupyter Lab that has as a main purpose to search specific items in the stockroom of one or many stores by name, category and city.

## psycopg2

psycopg2 has as a main purpose to be a PostgreSQL database adapter for Python.

#### Usage ####

```` 
con = psycopg2.connect(database="store_database", user="cindy", password="Flamingosis01.", host="localhost", port="5432")
cur = con.cursor()
```` 

## mpimg

mpimg is a Python library that has as a main purpose to show pictures in Python/Jupyter Lab

#### Usage ####

```` 

Displaying pictures

img_A = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod.jpeg")
img_B = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod (1).jpeg")
img_C = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod (2).jpeg")
img_D = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod (3).jpeg")
img_E = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod (5).jpeg")
img_F = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod (6).jpeg")
img_G = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod (7).jpeg")
img_H = mpimg.imread("/Users/cindymendoncapaez/Documents/hmgoepprod (8).jpeg")

```` 

## folium

folium is a Python library that has as a main purpose to show maps in Python/Jupyter Lab

#### Usage ####

```` 
m_1 = folium.Map(location=[52.370216, 4.895168], tiles='openstreetmap', zoom_start=10)

for index, row in stores_data.iterrows():
    lat = row["lat"]
    lon = row["lng"]
    name = row["store"]
    postal_code = row["postal_code"]
    map_displayed_info = '{}  {}'.format(name, postal_code)
    folium.Marker([lat, lon], popup=map_displayed_info).add_to(m_1)
    print(m_1)

m_2 = folium.Map(location=[52.370216, 4.895168], tiles='openstreetmap', zoom_start=10)

for index, row in find_categories.iterrows():
    lat = row["lat"]
    lon = row["lng"]
    name = row["store"]
    categories = row["category"]
    map_displayed_info1 = '{} : {}'.format(name, categories)
    folium.Marker([lat, lon], popup=map_displayed_info1).add_to(m_2)
    print(m_2)
    
m_3 =folium.Map(location=[52.370216, 4.895168], tiles='openstreetmap', zoom_start=10)

for index, row in find_items.iterrows():
    lat = row["lat"]
    lon = row["lng"]
    name = row["store"]
    items = row["item"]
    map_displayed_info2 = '{} : {}'.format(name, items)
    folium.Marker([lat, lon], popup=map_displayed_info2).add_to(m_3)
    print (m_3)
```` 

# Data mining store website 

The Data mining store website project was done with the purpose of mining the opening and closing hours of all the H&M stores in the Netherlands, including holidays and exceptions in the schedule.

## requests

Requests is a HTTP library for Python/Jupyter Lab

#### Usage ####

```` 
page = requests.get(url)
```` 

## bs4 

Beautiful Soup is a library that makes it easy to scrape information from web pages. 
It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.

#### Usage ####
```` 
soup = BeautifulSoup(page.content, 'html.parser')
```` 

# Installation of all libraries 

Use for all libraries the package manager [pip](https://pip.pypa.io/en/stable/) to install .

## Instructions

### mpimg

Terminal:

Python 2: pip install mpimg
//Python 3 : pip3 install mping

Jupyter Lab:

Python 2: %pip install mpimg
//Python 3 : %pip3 install mping

### folium

Termianl:

Python 2: pip install folium 
//Python 3: pip3 install folium

Jupyter Lab:

Python 2: %pip install folium 
//Python 3: %pip3 install folium

### request

Terminal:

Python 2: pip install request
//Python 3 pip3 install request

Jupyter Lab:

Python 2: %pip install request
//Python 3 %pip3 install request

### bs4 

Terminal:

Python 2: pip install bs4
//Python 3: pip3 install bs4

Jupyter Lab

Python 2: %pip install bs4
//Python 3: %pip3 install bs4

# Contributing 
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
