
from mock import Mock, patch
import unittest

from m_calls import add, num_mgr

class MyTestCase(unittest.TestCase):

    def test_my_add(self):
        self.assertEqual(add(1, 2), 3)

    @patch('m_calls.add', return_value = 100)
    def test_my_add_mck(self, mock_add):
        self.assertEqual(mock_add(1, 2), 100)

    @patch('m_calls.add')
    @patch('m_calls.multi')
    def test_num_mgr(self,  mock_multi, mock_add):
        mock_add.return_value = 20
        mock_multi.return_value = 100

        self.assertEquals(num_mgr(10,10),
                          {'sum':20,
                           'product': 100}
                          )

        mock_add.assert_called_once_with(10,10)
        mock_multi.assert_called_once_with(10,10)



if __name__ == '__main__':
    unittest.main()
