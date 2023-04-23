import tkinter as tk
from tkinter import Menu, filedialog
from PIL import ImageTk, Image
import os

class SurveyApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QuizRunner")
        self.geometry("500x500")
        self.resizable(width=False, height=False)
        self.loadbackground()
        self.title_quiz()
        self.question_index = 0
        self.questions = []
        self.result_counter = 0
        self.mainmenu = Menu(self)
        self.config(menu = self.mainmenu)
        self.mainmenu.add_command(label='Открыть опрос из файла', command = self.open_file)
        self.open_file_flag = 0

    def open_file(self):
        self.open_file_flag = 1
        self.questions_txt = []
        self.filepath = tk.filedialog.askopenfilename()
        if self.filepath != "":
            with open(self.filepath, "r", encoding="utf-8") as file:
                # Читаем каждую строку файла и разбиваем ее на вопрос и ответ
                for line in file.readlines():
                    question_txt, answer_txt = line.strip().split(", ")
            # Добавляем вопрос и ответ в список вопросов
                    self.questions_txt.append([question_txt, answer_txt])
                self.txtlbl = tk.Label(text = str(self.questions_txt))
                self.txtlbl.pack()
    
    def loadbackground(self):
        self.background_img = ImageTk.PhotoImage(Image.open("images/background.jpg"))
        self.background_img_label = tk.Label(self, image = self.background_img)
        self.background_img_label.place(x=0, y=0, relwidth=1, relheight=1) 

    def show_title(self):
        #Имя опросику меняем
        self.title_label["text"] = self.title_entry.get()
        self.title_label.pack()
        #Чистим
        self.title_entry.pack_forget()
        self.submit_title_btn.pack_forget()
        self.title_img_label.pack_forget()
        #Запускаем
        self.create_widgets()


    def title_quiz(self):
        # Создаем метку для заголовка опроса
        self.title_label = tk.Label(self, text= "Введите название опроса:", font = (20), bg= "#85d2c8")
        self.title_label.pack()
        self.title_entry = tk.Entry(self)
        self.title_entry.pack()
        self.submit_title_btn = tk.Button(text="Подтвердить", command=self.show_title,font = (14))
        self.submit_title_btn.pack()
        self.title_picture_add()
    
    def title_picture_add(self):
        self.title_img = ImageTk.PhotoImage(Image.open("images/logo v22.jpg"))
        self.title_img_label = tk.Label(self, image = self.title_img, width=500, height=100)
        self.title_img_label.pack(  side= tk.BOTTOM,
                                    fill=tk.BOTH)
                                    
        
    def create_widgets(self):
        
        #self.resizable(width=True, height=True)

        # Создаем метку для вопроса
        self.question_label = tk.Label(self, text="Вопрос", bg= "#85d2c8")
        self.question_label.pack()

        # Создаем поле для ввода вопроса
        self.question_entry = tk.Entry(self)
        self.question_entry.pack()

        # Создаем метку для ответа
        self.answer_label = tk.Label(self, text="Ответ", bg= "#85d2c8")
        self.answer_label.pack()

        # Создаем поле для ввода ответа
        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack()

        # Создаем кнопку для добавления нового вопроса
        self.add_question_button = tk.Button(self, text="Добавить вопрос", command=self.add_question)
        self.add_question_button.pack()

        # Создаем кнопку для отправки ответа
        self.submit_button = tk.Button(self, text="Отправить", command=self.submit_answer)
        #self.submit_button.pack()

        #Создаем кнопку для подтверждения оконченности создания опроса
        self.submit_quiz_button = tk.Button(self, text = "Подтвердить", command=self.submit_quiz)
        self.submit_quiz_button.pack()

    def result_count(self):
    #Считаем общий балл
        result_count_label = tk.Label(self, text = ("Общий балл: " + str(self.result_counter) + "/" + str(len(self.questions))), font=(20), bg= "#85d2c8")
        result_count_label.pack(side=tk.BOTTOM)

    def add_question(self):
        if self.open_file_flag == 0:
        # Получаем текст вопроса и ответа
            question_text = self.question_entry.get()
            answer_text = self.answer_entry.get()

        # Создаем новый вопрос и добавляем его в список вопросов
            question = {'question': question_text, 'answer': answer_text}
            self.questions.append(question)

        # Очищаем поля для ввода вопроса и ответа
            self.question_entry.delete(0, tk.END)
            self.answer_entry.delete(0, tk.END)
        else:
            question_num = 0
            question_text = self.questions_txt([0], [question_num])
            answer_text = self.questions_txt([1], [question_num])


    def submit_answer(self):
        # Получаем ответ на вопрос
        answer = self.answer_entry.get()
        # Обрабатываем ответ на вопрос
        # Здесь можно сохранять ответы в базу данных или файл
        question = self.questions[self.question_index]
        is_correct = answer.lower() == question['answer'].lower()
        if is_correct:
            self.result_counter += 1
        else:
            self.result_counter -= 1
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
            self.title_label.config(text="Опрос завершен", font=(14))
            self.answer_entry.pack_forget()
            self.answer_label.pack_forget()
            self.question_label.pack_forget()
            self.submit_button.pack_forget()
            self.result_count()

        
    def submit_quiz(self):
        # Очищаем поля для ввода вопроса и ответа
            self.question_entry.delete(0, tk.END)
            self.answer_entry.delete(0, tk.END)
        #Удаляем кнопку
            self.submit_quiz_button.destroy()
        #Добавляем кнопку ответа
            self.submit_button.pack()
        #Выводим вопрос
            question = self.questions[self.question_index]
            self.question_label.config(text=question['question'])
        #Удаляем лишние кнопочки
            self.question_entry.pack_forget()
            self.add_question_button.pack_forget()
            self.submit_quiz_button.destroy()


    def show_result(self, is_correct):
        # Создаем метку для вывода результата
        question = self.questions[self.question_index]
        self.question_num_text = (str(self.question_index+1) + ". Вопрос: " + str(question['question'])+ " Ответ: " + str(question['answer']))
        if is_correct:
            result_text = self.question_num_text + ". " + "Верно!"
            
        else:
            result_text = self.question_num_text + ". " "Неверно!"
        result_label = tk.Label(self, text = result_text, bg= "#85d2c8")
        result_label.pack(expand=True)

if __name__ == '__main__':
    app = SurveyApplication()
    app.mainloop()