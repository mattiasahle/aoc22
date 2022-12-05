import unittest
import day51


class TestDayXX(unittest.TestCase):

    def test_read_input(self):
        input = day51.read_input()

        self.assertIsNotNone(input)


    def test_parse_input(self):
        parsed_input = day51.parse_input(day51.read_input())
        
        for line in parsed_input:
            self.assertNotIn('\n', line)


if __name__ == '__main__':
    unittest.main()