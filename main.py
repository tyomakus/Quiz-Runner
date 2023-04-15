import tkinter as tk

class SurveyApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Опрос")
        self.geometry("500x500")
        self.create_widgets()
        self.question_index = 0
        self.questions = []

    def create_widgets(self):
        # Создаем метку для заголовка опроса
        self.title_label = tk.Label(self, text="Заголовок опроса")
        self.title_label.pack()

        # Создаем метку для вопроса
        self.question_label = tk.Label(self, text="Вопрос")
        self.question_label.pack()

        # Создаем поле для ввода вопроса
        self.question_entry = tk.Entry(self)
        self.question_entry.pack()

        # Создаем метку для ответа
        self.answer_label = tk.Label(self, text="Ответ")
        self.answer_label.pack()

        # Создаем поле для ввода ответа
        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack()

        # Создаем кнопку для добавления нового вопроса
        self.add_question_button = tk.Button(self, text="Добавить вопрос", command=self.add_question)
        self.add_question_button.pack()

        # Создаем кнопку для отправки ответа
        self.submit_button = tk.Button(self, text="Отправить", command=self.submit_answer)
        self.submit_button.pack()

        #Создаем кнопку для подтверждения оконченности создания опроса
        self.submit_quiz_button = tk.Button(self, text = "Подтвердить", command=self.submit_quiz)
        self.submit_quiz_button.pack()

    def add_question(self):
        # Получаем текст вопроса и ответа
        question_text = self.question_entry.get()
        answer_text = self.answer_entry.get()

        # Создаем новый вопрос и добавляем его в список вопросов
        question = {'question': question_text, 'answer': answer_text}
        self.questions.append(question)

        # Очищаем поля для ввода вопроса и ответа
        self.question_entry.delete(0, tk.END)
        self.answer_entry.delete(0, tk.END)

    def submit_answer(self):
        # Получаем ответ на вопрос
        answer = self.answer_entry.get()

        # Обрабатываем ответ на вопрос
        # Здесь можно сохранять ответы в базу данных или файл
        question = self.questions[self.question_index]
        is_correct = answer.lower() == question['answer'].lower()
        self.show_result(is_correct)

        # Очищаем поле для ввода ответа
        self.answer_entry.delete(0, tk.END)

        # Переключаемся на следующий вопрос (если есть)
        self.question_index += 1
        if self.question_index < len(self.questions):
            question = self.questions[self.question_index]
            self.title_label.config(text="Опрос")
            self.question_label.config(text=question['question'])
        else:
            self.title_label.config(text="Опрос завершен")
        
    def submit_quiz(self):
            pass

    def show_result(self, is_correct):
        # Создаем метку для вывода результата
        result_text = "Верно!" if is_correct else "Неверно!"
        result_label = tk.Label(self, text=result_text)
        result_label.pack()

if __name__ == '__main__':
    app = SurveyApplication()
    app.mainloop()