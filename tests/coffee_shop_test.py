import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop=CoffeeShop("The Prancing Pony",100)
        self.coffee_shop.add_drinks(1,"Mocha",3.5,50)
        self.coffee_shop.add_drinks(1,"Latte",3,50)
    
    def test_coffee_shop_has_attributes(self):
        self.assertEqual("The Prancing Pony",self.coffee_shop.name)
        self.assertEqual(100,self.coffee_shop.till)
        self.assertEqual({"mocha":[self.coffee_shop.drinks["mocha"][0],1],"latte":[self.coffee_shop.drinks["latte"][0],1]},self.coffee_shop.drinks)
    
    def test_add_drinks(self):
        self.assertEqual({"mocha":[self.coffee_shop.drinks["mocha"][0],1],"latte":[self.coffee_shop.drinks["latte"][0],1]},self.coffee_shop.drinks)
        self.coffee_shop.add_drinks(2,"Mocha")
        self.assertEqual({"mocha":[self.coffee_shop.drinks["mocha"][0],3],"latte":[self.coffee_shop.drinks["latte"][0],1]},self.coffee_shop.drinks)
        self.coffee_shop.add_drinks(1,"Crisps",1.3,20,False)
        self.assertEqual({"crisps":[self.coffee_shop.food["crisps"][0],1]},self.coffee_shop.food)
        self.coffee_shop.add_drinks(2,"Sandwich",2.5,55,False)
        self.assertEqual({"crisps":[self.coffee_shop.food["crisps"][0],1],"sandwich":[self.coffee_shop.food["sandwich"][0],2]},self.coffee_shop.food)
        self.coffee_shop.add_drinks(2,"Crisps")
        self.assertEqual({"crisps":[self.coffee_shop.food["crisps"][0],3],"sandwich":[self.coffee_shop.food["sandwich"][0],2]},self.coffee_shop.food)
    
    def test_return_menu(self):
        self.coffee_shop.add_drinks(1,"Crisps",1.3,20,False)
        self.assertEqual(set(self.coffee_shop.return_menu()),{"mocha","latte","crisps"})
    
    def test_items_customer_can_afford(self):
        self.coffee_shop.add_drinks(2,"Cappucino",3,50)
        self.coffee_shop.add_drinks(1,"Orange juice",1.99,0)
        self.coffee_shop.add_drinks(90,"Water",0,0)
        self.coffee_shop.add_drinks(1,"Crisps",1.3,20,False)
        broke_customer=Customer("Darren",2,20)
        self.coffee_shop.items_customer_can_afford(broke_customer)
        self.assertEqual(set(self.coffee_shop.items_customer_can_afford(broke_customer)),{"water","orange juice","crisps"})
    
    def test_stock_value(self):
        self.coffee_shop.add_drinks(1,"Crisps",1.3,20,False)
        self.assertEqual(self.coffee_shop.stock_value(),7.8)