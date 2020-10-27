```
└─╼ python3 test.py
GET MENU
{'items': [{'pizza': ['custom', 'margarieta', 'buffalo', 'hawaiian']}, {'beverage': ['Coke', 'lemonade']}, {'apetizer': ['wings', 'fries']}]}

PUT orders
{'id': 1, 'name': 'tim', 'item': 'pizza, beverage, apetizer', 'toppings': 'onions, extra-cheese', 'size': 'small', 'crust': 'thin'}
{'id': 2, 'name': 'john', 'item': 'beverage, apetizer', 'toppings': None, 'size': 'MED', 'crust': None}
{'id': 3, 'name': 'sam', 'item': 'pizza', 'toppings': 'extra-cheese', 'size': 'Large', 'crust': 'thick'}

GET order for id == 1
{'id': 1, 'name': 'tim', 'item': 'pizza, beverage, apetizer', 'toppings': 'onions, extra-cheese', 'size': 'small', 'crust': 'thin'}

GET pricing for all items
[{'pizza': [{'custom': {'Small': 10, 'Med': 15, 'Large': 20}}, {'margarieta': {'Small': 10, 'Med': 15, 'Large': 20}}, {'buffalo': {'Small': 10, 'Med': 15, 'Large': 20}}, {'hawaiian': {'Small': 10, 'Med': 15, 'Large': 20}}]}, {'beverage': [{'Coke': {'Small': 10, 'Med': 15, 'Large': 20}}, {'lemonade': {'Small': 10, 'Med': 15, 'Large': 20}}]}, {'apetizer': [{'wings': {'Small': 10, 'Med': 15, 'Large': 20}}, {'fries': {'Small': 10, 'Med': 15, 'Large': 20}}]}]

GET price for small custom pizza
[{'pizza': [{'custom': {'Small': 10, 'Med': 15, 'Large': 20}}, {'margarieta': {'Small': 10, 'Med': 15, 'Large': 20}}, {'buffalo': {'Small': 10, 'Med': 15, 'Large': 20}}, {'hawaiian': {'Small': 10, 'Med': 15, 'Large': 20}}]}, {'beverage': [{'Coke': {'Small': 10, 'Med': 15, 'Large': 20}}, {'lemonade': {'Small': 10, 'Med': 15, 'Large': 20}}]}, {'apetizer': [{'wings': {'Small': 10, 'Med': 15, 'Large': 20}}, {'fries': {'Small': 10, 'Med': 15, 'Large': 20}}]}]


```