import unittest
from unittest.mock import patch, mock_open
import ex3


class TestTotal(unittest.TestCase):
    def test_calculate_total(self):
        mock_file = "10.6\n20\n16.69"
        with patch('builtins.open', mock_open(read_data=mock_file)):
            result = ex3.calculate_total('fake_path.txt')

        assert result == 47.29


if __name__ == '__main__':
    unittest.main()
