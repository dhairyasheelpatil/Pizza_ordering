from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask import Flask, request

pizza_put_args = reqparse.RequestParser()
pizza_put_args.add_argument("id", type=int, help="Name of the pizza is required", required=True)
pizza_put_args.add_argument("name", type=str, help="Name of the pizza is required", required=True)
pizza_put_args.add_argument("item", type=str, help="Item (pizza/beverage/apetizer)", required=True)
pizza_put_args.add_argument("toppings", type=str, help="Toppings on the pizza")
pizza_put_args.add_argument("size", type=str, help="Size of the pizza is required", required=True)
pizza_put_args.add_argument("crust", type=str, help="Crust of the pizza is required")


order_db = [{"id": 1, "name": "tim", "item": "pizza, beverage, apetizer", "toppings": "onions, extra-cheese" , "size": "small", "crust": "thin"},
		  	   {"id": 2, "name": "john", "item": "beverage, apetizer", "size": "MED"},
		       {"id": 3, "name": "sam", "item": "pizza", "toppings": "extra-cheese", "size": "Large", "crust": "thick"}]

class PizzaOrder(Resource):
	def get(self):		
		for order in order_db:
			if order['id'] == 1:
				return order
				
	def put(self):
		args = pizza_put_args.parse_args()
		return args
	