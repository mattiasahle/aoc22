import unittest
import template


class TestDayXX(unittest.TestCase):

    def test_read_input(self):
        input = template.read_input()

        self.assertIsNotNone(input)


    def test_parse_input(self):
        parsed_input = template.parse_input(template.read_input())
        
        for line in parsed_input:
            self.assertNotIn('\n', line)


if __name__ == '__main__':
    unittest.main()