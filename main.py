import tkinter as tk

class QuizRunnerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Quizrunner")

        # создание области для ввода вопросов
        self.question_frame = tk.Frame(master)
        self.question_frame.pack(side="left")

        self.question_label = tk.Label(self.question_frame, text="Enter a question:")
        self.question_label.pack()

        self.question_text = tk.Text(self.question_frame, height=10, width=50)
        self.question_text.pack()

        self.question_submit_button = tk.Button(self.question_frame, text="Submit Question", command=self.submit_question)
        self.question_submit_button.pack()

        # создание области для ответов
        self.answer_frame = tk.Frame(master)
        self.answer_frame.pack(side="right")

        self.answer_label = tk.Label(self.answer_frame, text="Answer:")
        self.answer_label.pack()

        self.answer_text = tk.Text(self.answer_frame, height=10, width=50)
        self.answer_text.pack()

        self.submit_answer_button = tk.Button(self.answer_frame, text="Submit Answer", command=self.submit_answer)
        self.submit_answer_button.pack()

        self.question_list = []

    def submit_question(self):
        question = self.question_text.get("1.0", "end-1c")
        self.question_list.append(question)
        self.question_text.delete("1.0", "end")

    def submit_answer(self):
        answer = self.answer_text.get("1.0", "end-1c")
        question = self.question_list.pop(0)
        # отправить ответ на вопрос на другую сторону приложения
        self.answer_text.delete("1.0", "end")
        if self.question_list:
            next_question = self.question_list[0]
            self.question_label.config(text=next_question)

root = tk.Tk()
my_gui = QuizRunnerGUI(root)
root.mainloop()