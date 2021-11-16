import unittest
from zad3 import ChristmasSong

class ChristmasSongTest(unittest.TestCase):
    def setUp(self):
        self.christmasSong = ChristmasSong()


    def test_getVerse_0(self):
        self.assertEqual(self.christmasSong.getVerse(0),"On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")
    def test_getVerses_0_2(self):
        self.assertEqual(self.christmasSong.getVerses(0,2), ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
				"On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."])

if __name__ == "__main__":
    unittest.main()