car = {
    "name":"Mustang",
    "Brand":"Ford",
    "Coloir": "red",
    "Year": 2018,
    "Milage":20
    


}
# car['type']='Electric'
# car.update({'type':'electric'})
# print(car)  

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.clear()
# print(car)

# Copy dictionary
car_1 = car.copy()
car_1 = dict(car)

car['color'] = 'White'
print(car_1)

