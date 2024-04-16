# JSON Basics
import json

car_data = {
    "name": "audi",
    "engine": "diesel"
}

print(car_data)

# json.dumps() --> serialises json to a formatted string

car_data_json_string = json.dumps(car_data)
print(car_data_json_string
      )

# json.dump() --> Creates a stream object and expects a file object to write to

with open("New_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)