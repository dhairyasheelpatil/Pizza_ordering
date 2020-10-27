import requests

BASE = "http://127.0.0.1:5000/"

print("GET MENU")
response = requests.get(BASE + 'menu')
print(response.json())
input()

print("PUT orders")
user_orders = [{"id": 1, "name": "tim", "item": "pizza, beverage, apetizer", "toppings": "onions, extra-cheese" , "size": "small", "crust": "thin"},
		  	   {"id": 2, "name": "john", "item": "beverage, apetizer", "size": "MED"},
		       {"id": 3, "name": "sam", "item": "pizza", "toppings": "extra-cheese", "size": "Large", "crust": "thick"}]


for order in range(len(user_orders)):
	response = requests.put(BASE + 'order', user_orders[order])
	print(response.json())
input()

print("GET order for id == 1")
response = requests.get(BASE + 'order')
print(response.json())
input()

print("GET pricing for all items")
response = requests.patch(BASE + 'price')
print(response.json())

input()

print("GET price for small custom pizza")
response = requests.patch(BASE + 'price')
print(response.json())

