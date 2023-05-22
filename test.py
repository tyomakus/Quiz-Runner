import unittest
from tkinter import Tk
from unittest.mock import patch
from io import StringIO
from main import SurveyApplication

class SurveyApplicationTests(unittest.TestCase):

    def setUp(self):
        self.app = SurveyApplication()
        self.app.title("QuizRunner")
        self.app.geometry("500x500")

    def test_init(self):
        self.assertEqual(self.app.title(), "QuizRunner")
        self.assertEqual(self.app.geometry(), "500x500")
        self.assertFalse(self.app.resizable())

    def test_open_file(self):
        with patch('tkinter.filedialog.askopenfilename', return_value='sample.txt'):
            self.app.open_file()
            self.assertEqual(self.app.filepath, 'sample.txt')
            self.assertEqual(len(self.app.questions_txt), 2)

    def test_show_title(self):
        self.app.title_entry.insert(0, "Sample Quiz")
        self.app.show_title()
        self.assertEqual(self.app.title_label['text'], "Sample Quiz")
        self.assertFalse(self.app.title_entry.winfo_ismapped())
        self.assertFalse(self.app.submit_title_btn.winfo_ismapped())

    def test_add_question(self):
        self.app.question_entry.insert(0, "What is the capital of France?")
        self.app.answer_entry.insert(0, "Paris")
        self.app.add_question()
        self.assertEqual(len(self.app.questions), 1)
        question = self.app.questions[0]
        self.assertEqual(question['question'], "What is the capital of France?")
        self.assertEqual(question['answer'], "Paris")
        self.assertEqual(self.app.question_entry.get(), "")
        self.assertEqual(self.app.answer_entry.get(), "")

    def test_line_switch(self):
        question = "This is a long question that needs to be wrapped"
        self.app.question_label.configure(text=question)
        width_question = self.app.question_label.winfo_width()
        self.app.line_switch(question)
        new_width_question = self.app.question_label.winfo_width()
        self.assertEqual(new_width_question, width_question)

    def test_submit_answer(self):
        self.app.open_file_flag = 0
        self.app.questions = [{'question': 'Q1', 'answer': 'A1'}, {'question': 'Q2', 'answer': 'A2'}]
        self.app.question_index = 0
        self.app.answer_entry.insert(0, "A1")
        self.app.submit_answer()
        self.assertEqual(self.app.result_counter, 1)
        self.assertEqual(self.app.result_label_str, "1. Вопрос: Q1 Ответ: A1. Верно!")

    def test_submit_quiz(self):
        self.app.open_file_flag = 0
        self.app.questions = [{'question': 'Q1', 'answer': 'A1'}, {'question': 'Q2', 'answer': 'A2'}]
        self.app.submit_quiz_button.invoke()
        self.assertFalse(self.app.question_entry.winfo_ismapped())
        self.assertFalse(self.app.question_label.winfo_ismapped())
        self.assertFalse(self.app.add_question_button.winfo_ismapped())
        self.assertEqual(self.app.title_label['text'], "Опрос")
        self.assertTrue(self.app.submit_button.winfo_ismapped())

    def test_show_result(self):
        self.app.open_file_flag = 0
        self.app.questions = [{'question': 'Q1', 'answer': 'A1'}, {'question': 'Q2', 'answer': 'A2'}]
        self.app.question_index = 0
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.app.show_result(True)
            output = mock_stdout.getvalue().strip()
            expected_output = "1. Вопрос: Q1 Ответ: A1. Верно!"
            self.assertEqual(output, expected_output)

            self.app.show_result(False)
            output = mock_stdout.getvalue().strip()
            expected_output += "\n2. Вопрос: Q1 Ответ: A1. Неверно!"
            self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()