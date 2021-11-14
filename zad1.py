import unittest
class Hamming:
    def distance(self, str1, str2):
        if len(str1) == len(str2):
            i = 0
            count = 0

            while (i < len(str1)):
                if (str1[i] != str2[i]):
                    count += 1
                i += 1
            return count
        if len(str1) > len(str2):
            raise ValueError("Pierwszy str dłuższy od drugiego")

class HammingTest(unittest.TestCase):
    def test_empty_strands(self):
        self.assertEqual(self.hamming.distance("", ""), 0)

    def test_single_letter_identical_strands(self):

        self.assertEqual(self.hamming.distance("A", "A"), 0)

    def test_single_letter_different_strands(self):
        self.assertEqual(self.hamming.distance("G", "T"), 1)

    def test_long_identical_strands(self):
        self.assertEqual(self.hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)

    def test_long_different_strands(self):
        self.assertEqual(self.hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    def test_disallow_first_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            self.hamming.distance("AATG", "AAA")

    def test_disallow_second_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            self.hamming.distance("ATA", "AGTG")

    @unittest.skip
    def test_disallow_left_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming.distance("", "G")

    @unittest.skip
    def test_disallow_right_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming.distance("G", "")

    # Utility functions
    def setUp(self):
        self.hamming = Hamming()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")
if __name__ == '__main__':
    unittest.main()