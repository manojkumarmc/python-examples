import unittest
import sys
from hypothesis import given
from hypothesis import strategies as st
sys.path.append('/Users/mcbobs/projects/python/python-examples')

from airport_list import list_airports

class TestRunner(unittest.TestCase):

    @given(s1 = st.sampled_from(['ABC','DEF','GHI']),
           s2 = st.sampled_from(['XYZ','HOO']))
    def test_airport_lister(self, s1, s2):
        ap = 'This flight goes from {} to {}'.format(s1, s2)
        self.assertEquals(len(list_airports(ap)), 2)



if __name__ == "__main__":
    unittest.main()
