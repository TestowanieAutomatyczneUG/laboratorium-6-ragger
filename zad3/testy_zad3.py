import unittest
from zad3 import ChristmasSong

class ChristmasSongTest(unittest.TestCase):
    def setUp(self):
        self.christmasSong = ChristmasSong()


    def test_getLine_0(self):
        self.assertEqual(self.christmasSong.getLine(0),"On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

if __name__ == "__main__":
    unittest.main()