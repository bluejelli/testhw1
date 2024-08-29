import unittest
from HelloWorld import HelloWorld
class HelloTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.happy_face = HelloWorld()
        self.sad_face = HelloWorld("Bye bye world.")
        self.mild_face = HelloWorld("oh hey.")
        self.passive_aggressive = HelloWorld("Oh its you!")
        self.displeased =   HelloWorld("**eye roll**")

 
    def test_default(self):
        self.assertEqual((self.happy_face.__repr__()).upper(), "HELLO WORLD!")
    
    def test_sad(self):
        self.assertEqual((self.sad_face.__repr__()).upper(), str("Bye bye world.").upper())
    
    def test_mild(self):
        self.assertEqual((self.mild_face.__repr__()).upper(), str("oh hey.").upper())
    
    def test_passive_aggressive(self):
        self.assertEqual((self.passive_aggressive.__repr__()).upper(), str("Oh its you!").upper())
    
    def test_displeased(self):
        self.assertEqual((self.displeased.__repr__()).upper(), str("**eye roll**").upper())

#if __name__ == "__main__":
#    unittest.main()