import unittest
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub=Pub("The Chanter",100)
        self.pub.add_stock(4,"Beer",3.5,5)
        self.pub.add_stock(1,"Wine",8,13)
    
    def test_pub_has_attributes(self):
        self.assertEqual("The Chanter",self.pub.name)
        self.assertEqual(100,self.pub.till)
        self.assertEqual({"beer":[self.pub.drinks["beer"][0],4],"wine":[self.pub.drinks["wine"][0],1]},self.pub.drinks)
    
    def test_add_stock(self):
        self.assertEqual({"beer":[self.pub.drinks["beer"][0],4],"wine":[self.pub.drinks["wine"][0],1]},self.pub.drinks)
        self.pub.add_stock(2,"beer")
        self.assertEqual({"beer":[self.pub.drinks["beer"][0],6],"wine":[self.pub.drinks["wine"][0],1]},self.pub.drinks)
        self.pub.add_stock(1,"Crisps",1.3,2,False)
        self.assertEqual({"crisps":[self.pub.food["crisps"][0],1]},self.pub.food)
        self.pub.add_stock(2,"peanuts",2.99,7,False)
        self.assertEqual({"crisps":[self.pub.food["crisps"][0],1],"peanuts":[self.pub.food["peanuts"][0],2]},self.pub.food)
        self.pub.add_stock(2,"Crisps")
        self.assertEqual({"crisps":[self.pub.food["crisps"][0],3],"peanuts":[self.pub.food["peanuts"][0],2]},self.pub.food)
    
    def test_return_menu(self):
        self.pub.add_stock(1,"Crisps",1.3,2,False)
        self.assertEqual(set(self.pub.return_menu()),{"beer","wine","crisps"})
    
    def test_items_customer_can_afford(self):
        self.pub.add_stock(2,"Vodka Coke",7.2,15)
        self.pub.add_stock(1,"Orange juice",1.5,0)
        self.pub.add_stock(90,"Water",0,0)
        self.pub.add_stock(1,"Crisps",1.3,2,False)
        broke_customer=Customer("Darren",2,20)
        self.pub.items_customer_can_afford(broke_customer)
        self.assertEqual(set(self.pub.items_customer_can_afford(broke_customer)),{"water","orange juice","crisps"})
    
    def test_stock_value(self):
        self.pub.add_stock(1,"Crisps",1.3,2,False)
        self.assertEqual(self.pub.stock_value(),23.3)