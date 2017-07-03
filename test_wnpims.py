import unittest
import wnpims

api = wnpims.API()

class TestWNPims(unittest.TestCase):
    def test_get_curr_val(self):
        api.get_curr_val("PLV-SB-001_850")

if __name__=="__main__":
    unittest.main()
