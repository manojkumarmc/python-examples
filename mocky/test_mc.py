
from mock import Mock, patch
import unittest

from m_calls import add

class MyTestCase(unittest.TestCase):

    @patch('m_calls.add', return_value = 100)
    def test_my_add(self, mock_add):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(mock_add(1, 2), 100)

if __name__ == '__main__':
    unittest.main()
