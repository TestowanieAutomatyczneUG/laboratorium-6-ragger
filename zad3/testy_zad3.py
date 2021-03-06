import unittest
from zad3 import ChristmasSong

class ChristmasSongTest(unittest.TestCase):
    def setUp(self):
        self.christmasSong = ChristmasSong()


    def test_getVerse_0(self):
        self.assertEqual(self.christmasSong.getVerse(0),"On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_getVerse_2(self):
        self.assertEqual(self.christmasSong.getVerse(2),"On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_getVerses_0_2(self):
        self.assertEqual(self.christmasSong.getVerses(0,2), ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
				"On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."])

    def test_getVerses_1_2(self):
        self.assertEqual(self.christmasSong.getVerses(1,2),
                         [
                          "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."])

    def test_getVerses_to_2(self):
        self.assertEqual(self.christmasSong.getVerses(endAt=2), [
            "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
            "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
        ])

    def test_getAllVerses(self):
        self.assertEqual(self.christmasSong.getAllVerses(), [
            "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
            "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        ])

    def test_getVerses_with_no_params(self):
        self.assertEqual(self.christmasSong.getVerses(), [
            "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
            "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        ])

    def test_getVerse_negative(self):
        self.assertRaises(IndexError, self.christmasSong.getVerse, -1)

    def test_getVerse_150(self):
        self.assertRaises(IndexError, self.christmasSong.getVerse, 150)
    def test_getVerse_float(self):
        self.assertRaises(ValueError, self.christmasSong.getVerse, 1.5)

    def test_getVerses_negative(self):
        self.assertRaises(IndexError, self.christmasSong.getVerses, -1, -0)
    def test_getVerses_150_200(self):
        self.assertRaises(IndexError, self.christmasSong.getVerses, 150, 200)

    def test_getVerses_from_22(self):
        self.assertRaises(IndexError, self.christmasSong.getVerses, startAt=22)


if __name__ == "__main__":
    unittest.main()