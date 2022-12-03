import unittest
import day32


class TestDay32(unittest.TestCase):

    def test_read_input(self):
        input = day32.read_input()

        self.assertIsNotNone(input)


    def test_parse_input(self):
        parsed_input = day32.parse_input(day32.read_input())
        
        for line in parsed_input:
            self.assertNotIn('\n', line)


    def test_calculate_priority(self):
        self.assertEqual(day32.calculate_priority('A'), 27)
        self.assertEqual(day32.calculate_priority('Z'), 52)
        self.assertEqual(day32.calculate_priority('a'), 1)
        self.assertEqual(day32.calculate_priority('z'), 26)


    def test_get_common_item(self):
        self.assertEqual(day32.get_common_item(['a', 'a', 'a']), 'a')
        self.assertEqual(day32.get_common_item(['ab', 'ac', 'ad']), 'a')
        self.assertEqual(day32.get_common_item(['ba', 'ac', 'ad']), 'a')


    def test_get_priority(self):
        self.assertEqual(day32.get_priority(['A', 'A', 'A']), 27)
        self.assertEqual(day32.get_priority(['Ab', 'Ac', 'Ad']), 27)
        self.assertEqual(day32.get_priority(['bA', 'Ac', 'Ad']), 27)
        self.assertEqual(day32.get_priority(['Z', 'Z', 'Z']), 52)
        self.assertEqual(day32.get_priority(['Zb', 'Zc', 'Zd']), 52)
        self.assertEqual(day32.get_priority(['bZ', 'Zc', 'Zd']), 52)
        self.assertEqual(day32.get_priority(['a', 'a', 'a']), 1)
        self.assertEqual(day32.get_priority(['ab', 'ac', 'ad']), 1)
        self.assertEqual(day32.get_priority(['ba', 'ac', 'ad']), 1)
        self.assertEqual(day32.get_priority(['bz', 'zc', 'zd']), 26)
        self.assertEqual(day32.get_priority(['bz', 'zc', 'zd']), 26)
        self.assertEqual(day32.get_priority(['bz', 'zc', 'zd']), 26)


if __name__ == '__main__':
    unittest.main()