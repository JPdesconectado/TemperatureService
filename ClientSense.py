import random
import time
import requests
import datetime

while True:
    temperature = random.randrange(0, 40)
    moisture = random.randrange(0, 100)
    luminosity = random.randrange(1, 50)
    format_temperature = str(temperature)+" °C"
    format_moisture = str(moisture)+" %"
    format_luminosity = str(luminosity)+" sóis"
    current_time = datetime.datetime.now()

    format_hour = "{:02d}".format(current_time.hour)
    format_minute = "{:02d}".format(current_time.minute)
    format_time = "{}:{}".format(format_hour, format_minute)
    format_day = "{:02d}".format(current_time.day)
    format_month = "{:02d}".format(current_time.month)
    format_year = "{:02d}".format(current_time.year)
    format_date =  "{}/{}/{}".format(format_day, format_month, format_year)
    params ={
        'temperature': format_temperature,
        'moisture': format_moisture,
        'luminosity': format_luminosity,
        'date': format_date,
        'hour': format_time
    }
    requests.post('http://127.0.0.1:5000/dados', json=params)
    print("Dados enviados...")
    time.sleep(10)

