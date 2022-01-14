import unittest
from lezione7 import Example

class TestExample(unittest.TestCase):

    def test_somma(self):
        somma_prova1 = Example(5, 4)
        
        self.assertEqual(somma_prova1.somma(), 9)

if __name__ == '__main__':
    unittest.main()