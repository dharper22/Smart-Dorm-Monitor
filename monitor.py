import random
from datetime import datetime


def determine_status(temperature, humidity):
    if temperature > 78:
        return "Room is too hot"

    if temperature < 65:
        return "Room is too cold"

    if humidity > 60:
        return "Room is too humid"

    if humidity < 30:
        return "Room is too dry"

    return "Room is comfortable"


temperature = round(random.uniform(62, 82), 1)
humidity = round(random.uniform(25, 70), 1)
current_time = datetime.now().strftime("%Y-%m-%d %I:%M %p")

status = determine_status(temperature, humidity)

print("SMART DORM ENVIRONMENT MONITOR")
print("--------------------------------")
print(f"Time: {current_time}")
print(f"Temperature: {temperature}°F")
print(f"Humidity: {humidity}%")
print(f"Status: {status}")