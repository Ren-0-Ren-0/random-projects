import mysql.connector
import requests
from datetime import datetime, timezone, timedelta

api_key = "put_your_api_key_here"  # Replace with your OpenWeatherMap API key

def get_city_coordinates(city_name):
    """Get latitude and longitude of a city using the current weather API"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        return lat, lon
    else:
        print(f"Error getting coordinates for {city_name}: {data.get('message')}")
        return None, None

def unix_to_localtime(unix_time, timezone_offset):
    utc_time = datetime.fromtimestamp(unix_time, tz=timezone.utc)  # aware UTC datetime
    local_time = utc_time + timedelta(seconds=timezone_offset)
    return local_time
# Input city name here
input_city = "Kathmandu,NP"

lat, lon = get_city_coordinates(input_city)
if lat is None or lon is None:
    exit()

cnt = 10  # number of nearby cities

# Find nearby cities with lat/lon
url = f"https://api.openweathermap.org/data/2.5/find?lat={lat}&lon={lon}&cnt={cnt}&units=metric&appid={api_key}"

response = requests.get(url)
data = response.json()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="********",
    database="weatherdb"
)
cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100),
    temperature FLOAT,
    weather_description VARCHAR(255),
    datetime_local DATETIME
)
"""
cursor.execute(create_table_query)

insert_query = """
INSERT INTO weather_data (city, temperature, weather_description, datetime_local)
VALUES (%s, %s, %s, %s)
"""

for city in data["list"]:
    name = city["name"]
    temp = city["main"]["temp"]
    description = city["weather"][0]["description"]

    timezone_offset = city.get("timezone", 0)  # timezone offset in seconds

    dt_local = unix_to_localtime(city["dt"], timezone_offset)

    print(f"\n📍 {name}")
    print(f"🌡 Temperature: {temp}°C")
    print(f"☁ Weather: {description}")
    print(f"🕒 Local Time: {dt_local}")

    cursor.execute(insert_query, (name, temp, description, dt_local))

conn.commit()
cursor.close()
conn.close()

print("\n✅ Data inserted successfully into MySQL.")
