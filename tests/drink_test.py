import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink=Drink("Beer",3.5,5)
    
    def test_drink_has_attributes(self):
        self.assertEqual("Beer",self.drink.name)
        self.assertEqual(3.5,self.drink.price)
        self.assertEqual(5,self.drink.alcohol)