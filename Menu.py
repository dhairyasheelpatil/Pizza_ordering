from flask_restful import Resource


menu = {"items": [{"pizza": ["custom", "margarieta", "buffalo", "hawaiian"]}, 
			      {"beverage": ["Coke", "lemonade"]},
		   		  {"apetizer": ["wings", "fries"]}]}

class Menu(Resource):
	def get(self):
		return menu