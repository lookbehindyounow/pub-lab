from src.drink import Drink
from src.food import Food

class Pub:
	def __init__(self,name=str,till=float):
		self.name=name
		self.till=till
		self.drinks={}
		self.food={}
	
	# The drinks & food dictionaries are organised as such: {
	# "item name": [<object>, quantity in stock(int)],
	# "other item name": [<other_object>, quantity in stock(int)]
	# }
	def add_stock(self,quantity,name,price=None,alcohol_rejuvination=None,is_drink=True):
		if name.lower() in self.drinks: # if the item is on the drinks menu, increase the quantity of stock
			self.drinks[name.lower()][1]+=quantity
		elif name.lower() in self.food: # if it's on the food menu
			self.food[name.lower()][1]+=quantity
		# if it's on neither menu & the other arguments have been passed for initialisaton of a new object
		elif price is not None and alcohol_rejuvination is not None:
			if is_drink: # add new drink
				drink=Drink(name,price,alcohol_rejuvination)
				self.drinks[name.lower()]=[drink,quantity]
			else: # or new food
				food_product=Food(name,price,alcohol_rejuvination)
				self.food[name.lower()]=[food_product,quantity]
		else: # if it's not on either menu but no arguments have been passed to give the new item any attributes
			print(name+" does not currently exist on the menu."+
	 			  " If you wish to add it use the syntax: "+
				  "add_drink(quantity(int), name(str), price(float), caffeine content(int), is_drink(bool)."+
				  " You only need to fill in is_drink if making a new food item, where you would write False")
    
	# This function is just here cause it's a lot of code that would've otherwise been written twice in the sell method.
	def stock_check(self,name,stock_dict):
		if name in stock_dict: # if requested item is on given menu
			if stock_dict[name][1]>0: # if in stock
				item=stock_dict[name][0]
				stock_dict[name][1]-=1
				self.till+=item.price
				return item # returns purchased item to sell method
			else:
				print("we're all out of those")
		else:
			print("sorry kid we don't sell none of that here")
    
	def sell(self,name,customer,is_drink):
		if is_drink:
			if customer.age<18:
				print("too young go home no coffee for you")
			elif customer.drunkness>=40:
				print("you've had enough pal I'm calling you a taxi before you hurt yourself or someone else")
			else:
				return self.stock_check(name,self.drinks) # returns drink object to buy method in customer class
		else:
			return self.stock_check(name,self.food) # same thing for food
	
	def return_menu(self):
		return list(self.drinks.keys())+list(self.food.keys())
	
	def items_customer_can_afford(self,customer):
		return [drink for drink in self.drinks if self.drinks[drink][0].price<customer.wallet]+[food_product for food_product in self.food if self.food[food_product][0].price<customer.wallet] # the longest line for the nastiest list comprehension
	
	# for each drink & food item increase total by price * quantity
	def stock_value(self):
		total=0
		for drink in self.drinks:
			total+=self.drinks[drink][1]*self.drinks[drink][0].price
			print(total)
		for food_product in self.food:
			total+=self.food[food_product][1]*self.food[food_product][0].price
			print(total)
		return total