import unittest
from main import SurveyApplication

class TestMain(unittest.TestCase):
    def setUp(self):
        self.SurveyApplication = SurveyApplication()
    #def test_open_file(self):
        #filepath_test = SurveyApplication.filepath
        #self.assertNotEqual(filepath_test, "")
    def test_geometry(self):
        geom = SurveyApplication.geometry
        self.assertNotEqual(geom, "500x500")
    def width_test(self):
        width =  SurveyApplication.line_switch(width_question)
        self.assertTrue(width <= 500)
    def result_test(self):
        result =  SurveyApplication.result_counter
        self.assertEqual(result, 0)

    # Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()