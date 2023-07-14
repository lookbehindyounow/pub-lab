import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food=Food("Crisps",1.3,20)
    
    def test_food_has_attributes(self):
        self.assertEqual("Crisps",self.food.name)
        self.assertEqual(1.3,self.food.price)
        self.assertEqual(20,self.food.digestion)