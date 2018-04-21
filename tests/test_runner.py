import unittest
import sys
import string

from hypothesis import given
from hypothesis import strategies as st
sys.path.append('/Users/mcbobs/projects/python/python-examples/')

from airport_list import list_airports
from am_pm_to_24hr import time_converter
from enc_dec1 import encr, decr

class TestRunner(unittest.TestCase):

    # @given(s1 = st.sampled_from(['ABC','DEF','GHI']),
    #        s2 = st.sampled_from(['XYZ','HOO']))
    @given(st.text(min_size=3, max_size=3, alphabet=string.ascii_uppercase),
           st.text(min_size=3, max_size=3, alphabet=string.ascii_uppercase))
    def test_airport_lister(self, s1, s2):
        ap = 'This flight goes from {} to {}'.format(s1, s2)
        self.assertEquals(len(list_airports(ap)), 2)

    @given(p1=st.integers(min_value=1, max_value=12),
           p2=st.sampled_from(['AM', 'PM']))
    def test_time_converter(self, p1, p2):
        time_str = str(p1) + p2
        self.assertLessEqual(int(time_converter(time_str)), 24)

    @given(st.text(alphabet=string.ascii_letters))
    def test_enc_dec(self, s):
        self.assertEquals(decr(encr(s)), s)



if __name__ == "__main__":
    unittest.main()
