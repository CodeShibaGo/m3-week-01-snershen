import unittest
from reversed_strings import reverse_string

class TestReverseString(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("Hello"), "olleH")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string("12345"), "54321")
        self.assertEqual(reverse_string("Coding"), "gnidoC")
        self.assertEqual(reverse_string(""), "")

if __name__ == '__main__':
    unittest.main()
