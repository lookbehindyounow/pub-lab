import unittest
from src.customer import Customer
from src.coffee_shop import CoffeeShop

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.shop=CoffeeShop("The Prancing Pony",100)
        self.shop.add_drinks(4,"Mocha",3.5,50)
        self.shop.add_drinks(1,"Flat White",3,45)
        self.customer=Customer("Kev",20,45)
    
    def test_has_attributes(self):
        self.assertEqual("Kev",self.customer.name)
        self.assertEqual(20,self.customer.wallet)
        self.assertEqual(45,self.customer.age)
        self.assertEqual(0,self.customer.energy)
    
    def test_buy(self):
        self.customer.buy("Mocha",self.shop)
        self.assertEqual(103.5,self.shop.till)
        self.assertEqual(16.5,self.customer.wallet)
        self.assertEqual(50,self.customer.energy)
    
    def test_shop_checks(self):
        underage_customer=Customer("Timmy",100,3)
        underage_customer.buy("Mocha",self.shop)
        self.assertEqual(underage_customer.wallet,100)
        buzzing_customer=Customer("Fast Eddie",40,30)
        [buzzing_customer.buy("Mocha",self.shop)for i in range(4)]
        self.assertEqual(buzzing_customer.energy,150)
    
    def test_stock(self):
        self.customer.buy("Latte",self.shop)
        self.customer.buy("Flat white",self.shop)
        self.customer.buy("Flat white",self.shop)
        self.assertEqual(self.customer.energy,45)
    
    def test_buy_food(self):
        self.shop.add_drinks(1,"Crisps",1.3,20,False)
        self.customer.buy("crisps",self.shop,False)
        self.assertEqual(self.customer.energy,-20)
        self.assertEqual(self.customer.wallet,18.7)