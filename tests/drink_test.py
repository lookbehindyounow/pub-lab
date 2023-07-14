import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink=Drink("Vanilla mocha cappuchino flatte",4,50)
    
    def test_drink_has_attributes(self):
        self.assertEqual("Vanilla mocha cappuchino flatte",self.drink.name)
        self.assertEqual(4.0,self.drink.price)
        self.assertEqual(50,self.drink.caffeine)