import requests
import time
from pymongo import MongoClient
DB = MongoClient("URL MONGODB")
dbname = DB["MONITORING"]
db = dbname.Monitor

# Fungsi untuk memeriksa status code dari response
def check_status_code(response):
    if response.status_code == 200:
        print("Success! Status code: ", response.status_code)
    else:
        print("Failed. Status code: ", response.status_code)
        return False

# Loop untuk memeriksa status setiap URL setiap 10 detik
while True:
    for i, url in enumerate(db.find_one({"name":"MONITOR"})["monitor_url"]):
        response = requests.get(url)
        if check_status_code(response) == False:
            print("Trying to activate URL: ", url)
            try:
                response = requests.get(url)
                if check_status_code(response) == True:
                    db.find_one({"name":"MONITOR"})["monitor_url"][i] = url
                    print("URL activated: ", url)
            except:
                print("Failed to activate URL: ", url)
    time.sleep(60)
