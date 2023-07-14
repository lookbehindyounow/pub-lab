import unittest
from src.customer import Customer
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.pub=Pub("The Chanter",100)
        self.pub.add_stock(20,"Beer",3.5,5)
        self.pub.add_stock(1,"Wine",8,13)
        self.customer=Customer("Kev",20,45)
    
    def test_has_attributes(self):
        self.assertEqual("Kev",self.customer.name)
        self.assertEqual(20,self.customer.wallet)
        self.assertEqual(45,self.customer.age)
        self.assertEqual(0,self.customer.drunkness)
    
    def test_buy(self):
        self.customer.buy("Beer",self.pub)
        self.assertEqual(103.5,self.pub.till)
        self.assertEqual(16.5,self.customer.wallet)
        self.assertEqual(5,self.customer.drunkness)
    
    def test_pub_checks(self):
        underage_customer=Customer("Timmy",100,3)
        underage_customer.buy("Beer",self.pub)
        self.assertEqual(underage_customer.wallet,100)
        plastered_customer=Customer("Gaz",40,30)
        [plastered_customer.buy("Beer",self.pub)for i in range(9)]
        self.assertEqual(plastered_customer.drunkness,40)
    
    def test_stock(self):
        self.customer.buy("Mojito",self.pub)
        self.customer.buy("wine",self.pub)
        self.customer.buy("Wine",self.pub)
        self.assertEqual(self.customer.drunkness,13)
    
    def test_buy_food(self):
        self.pub.add_stock(1,"Crisps",1.3,2,False)
        self.customer.buy("Beer",self.pub)
        self.customer.buy("crisps",self.pub,False)
        self.assertEqual(self.customer.drunkness,3)
        self.assertEqual(self.customer.wallet,15.2)