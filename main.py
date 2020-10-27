from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import Menu
import PizzaOrder
import Price


app = Flask(__name__)
api = Api(app)
api.add_resource(PizzaOrder.PizzaOrder, "/order")
api.add_resource(Menu.Menu, "/menu")
api.add_resource(Price.Price, "/price")


if __name__ == "__main__":
	app.run(debug=True)