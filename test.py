import unittest
from main import SurveyApplication

class TestMain(unittest.TestCase):
    def setUp(self):
        self.SurveyApplication = SurveyApplication()
    #Each test method starts with the keyword test_
    def test_open_file(self):
        questions_txt = SurveyApplication.open_file(question_txt)
        self.assertNotEqual(questions_txt, 0)
    # Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()