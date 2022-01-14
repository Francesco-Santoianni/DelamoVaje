import unittest
from lezione7_1 import somma

class TestExample(unittest.TestCase):

    def test_somma(self):
        self.assertEqual(somma(2,3), 5)
    
    #if not somma(2,3) == 5:
    #   raise Exception ('Test 2+3 non passato')