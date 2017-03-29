import unittest
from mock import MagicMock, patch


class RequesterTestCase(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.mock_request = MagicMock(name='requests')
        modules = {
            'requests': self.mock_request,
        }
        self.module_patcher = patch.dict('sys.modules', modules)
        self.module_patcher.start()
        import m_calls
        print m_calls
        self.m_calls = m_calls

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.module_patcher.stop()

    @patch('m_calls.requests')
    def test_m_calls_with_requests(self, mock_requests):
        mock_requests.get.side_effect = [200]
        self.assertEquals(
            self.m_calls.get_call('http://www.manojkumarmc.com'),
            200
        )
        mock_requests.get.assert_called_once_with(
            'http://www.manojkumarmc.com'
        )



if __name__ == '__main__':
    unittest.main()

