import unittest
import wnpims

api = wnpims.API()

class TestWNPimsCurrVal(unittest.TestCase):
    """Note that you need to be sure that the server is online or else the test will give false results!"""
    def test_get_curr_val(self):
        # todo: test if server is online
        self.assertEqual(api.get_curr_val("PLV-SB-001_850").shape, (1,9))
        self.assertEqual(api.get_curr_val("PLV-SB-001_XXX"), None)

if __name__=="__main__":
    unittest.main()
