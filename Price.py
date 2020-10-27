from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask import Flask, request


price_db = [{"pizza": [{"custom": {"Small": 10, "Med": 15, "Large": 20}},
		   			   {"margarieta": {"Small": 10, "Med": 15, "Large": 20}},
		   			   {"buffalo": {"Small": 10, "Med": 15, "Large": 20}},
		   			   {"hawaiian": {"Small": 10, "Med": 15, "Large": 20}}
		   			  ]},
			{"beverage": [{"Coke": {"Small": 10, "Med": 15, "Large": 20}}, 
					      {"lemonade": {"Small": 10, "Med": 15, "Large": 20}}
						 ]},
			{"apetizer": [{"wings": {"Small": 10, "Med": 15, "Large": 20}}, 
					      {"fries": {"Small": 10, "Med": 15, "Large": 20}}
			 			 ]}]


class Price(Resource):
	def get(self):
		return {"price": price_db[0]['pizza'][0]['custom']['Small']}
	def patch(self):
		return price_db
				
	def put(self):
		args = pizza_put_args.parse_args()
		return args
	