import json
car = """ {"model" : "Civic", 
"make" : "Honda",
"variants" : ["Sedan", "Coupe"]}"""

car_dict = json.loads(car)
print(car_dict["variants"])

with open('python_aprentice/currency.json') as json_file:
    data = json.load(json_file)
    print(data)

with open('python_aprentice/car.txt', 'w') as json_file:
    json.dump(car, json_file)

