import unittest
import day41


class TestDayXX(unittest.TestCase):

    def test_read_input(self):
        input = day41.read_input()

        self.assertIsNotNone(input)


    def test_parse_input(self):
        parsed_input = day41.parse_input(day41.read_input())
        
        for line in parsed_input:
            self.assertNotIn('\n', line)


    def test_is_in_range(self):
        self.assertTrue(day41.is_in_range(1, 1, 3))
        self.assertTrue(day41.is_in_range(2, 1, 3))
        self.assertTrue(day41.is_in_range(3, 1, 3))
        self.assertFalse(day41.is_in_range(0, 1, 3))
        self.assertFalse(day41.is_in_range(4, 1, 3))


    def test_get_first_low(self):
        self.assertEqual(day41.get_first_low(['1-2', '3-4']), 1)


    def test_get_first_high(self):
        self.assertEqual(day41.get_first_high(['1-2', '3-4']), 2)


    def test_get_second_low(self):
        self.assertEqual(day41.get_second_low(['1-2', '3-4']), 3)


    def test_get_second_high(self):
        self.assertEqual(day41.get_second_high(['1-2', '3-4']), 4)


    def test_is_in_full_range(self):
        # Both are the same range
        self.assertTrue(day41.is_in_full_range(['1-1', '1-1']))
        self.assertTrue(day41.is_in_full_range(['1-2', '1-2']))

        # First range is in second range
        self.assertTrue(day41.is_in_full_range(['1-1', '1-2'])) # Zero range touches bottom
        self.assertTrue(day41.is_in_full_range(['2-2', '1-2'])) # Zero range touches top
        self.assertTrue(day41.is_in_full_range(['2-2', '1-3'])) # Zero range in between
        self.assertTrue(day41.is_in_full_range(['1-2', '1-3'])) # Range touches bottom
        self.assertTrue(day41.is_in_full_range(['2-3', '1-3'])) # Range touches top
        self.assertTrue(day41.is_in_full_range(['2-3', '1-4'])) # Range in between
        
        # Second range is in first range
        self.assertTrue(day41.is_in_full_range(['1-2', '1-1'])) # Zero range touches bottom
        self.assertTrue(day41.is_in_full_range(['1-2', '2-2'])) # Zero range touches top
        self.assertTrue(day41.is_in_full_range(['1-3', '2-2'])) # Zero range in between
        self.assertTrue(day41.is_in_full_range(['1-3', '1-2'])) # Range touches bottom
        self.assertTrue(day41.is_in_full_range(['1-3', '2-3'])) # Range touches top
        self.assertTrue(day41.is_in_full_range(['1-4', '2-3'])) # Range in between

        # First range is not in second range
        self.assertFalse(day41.is_in_full_range(['1-2', '2-3'])) # Range touches bottom
        self.assertFalse(day41.is_in_full_range(['2-3', '1-2'])) # Range touches top


if __name__ == '__main__':
    unittest.main()