import time
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from enviroplus import gas, weather, light

# MongoDB configuration
MONGO_URI = "mongodb+srv://diegoavelasco:pK68IRuhlJiKUkk8@clustersmartcube.23vmt.mongodb.net/?retryWrites=true&w=majority&appName=ClusterSmartCube"
client = MongoClient(uri, server_api=ServerApi('1'))
DB_NAME = "enviro_data"
COLLECTION_NAME = "sensor_reading"
db = client["sample_mflix"]

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def get_sensor_data():
    """Read data from Pimoroni Enviro sensors."""
    return {
        "temperature": weather.temperature(),  # In °C
        "pressure": weather.pressure(),        # In hPa
        "humidity": weather.humidity(),        # In %
        "light": light.light(),                # In Lux
        "timestamp": time.time()              # Unix timestamp
    }

def main():
    while True:

        # Get sensor data
        data = get_sensor_data()
        print(f"Collected Data: {data}")
        
        # Insert into MongoDB
        collection.insert_one(data)
        print("Data inserted into MongoDB.")

        # Wait before next reading (e.g., 10 seconds)
        time.sleep(10)




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting program...")
        client.close()
