from mock import Mock, patch
import unittest

from m_calls import add, num_mgr, Employee, get_call

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

    @patch.object(Employee, 'get_name', return_value = 'MC Bobs')
    def test_emp_class(self, mock_get_name):
        emp = Employee('MC', 20, 'M')
        self.assertEquals(emp.get_name(), 'MC Bobs')

    def test_get_call(self):
        my_requests_module = Mock()
        my_requests_module.get.return_value = 404
        with patch.dict('sys.modules', my_requests_module=my_requests_module):
            import my_requests_module
            self.assertEquals(
                get_call('http://www.manojkumarmc.com'),
                404
            )






if __name__ == '__main__':
    unittest.main()
