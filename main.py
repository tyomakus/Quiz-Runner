import tkinter as tk
from tkinter import Menu, filedialog
from PIL import ImageTk, Image
from textwrap import wrap
#from playsound import playsound
from threading import Thread
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
        self.question_num = 0
        self.questions = []
        self.questions_txt = []
        self.result_counter = 0
        self.mainmenu = Menu(self)
        self.config(menu = self.mainmenu)
        self.mainmenu.add_command(label='Открыть опрос из файла', command = self.open_file)
        self.open_file_flag = 0
        self.music_click_flag = 0
        self.music_num = 0
        self.txtlbl = tk.Label()
        self.result_label_str = ""
        

    def open_file(self):
        self.open_file_flag = 1
        self.filepath = tk.filedialog.askopenfilename()
        if self.filepath != "":
            with open(self.filepath, "r", encoding="utf-8") as file:
                # Читаем каждую строку файла и разбиваем ее на вопрос и ответ
                for line in file.readlines():
                    question_txt, answer_txt = line.strip().split(";- ")
            # Добавляем вопрос и ответ в список вопросов
                    self.questions_txt.append([question_txt, answer_txt])
                self.txtlbl = tk.Label(text = ("Вводите вопросы в формате:\n Вопрос;- Ответ\n Знак разделения ';- '\n Пример:\n Какое имя у самого популярного кота в мире YouTube?;- Мару \n Кто написал роман 1984?;- Джордж Оруэлл "), font = (12), bg= "#85d2c8")
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
        self.txtlbl.pack_forget()
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
                                    
        
    #self.resizable(width=True, height=True)
    def create_widgets(self):
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

        if self.open_file_flag == 1:
            self.question_entry.pack_forget()
            self.answer_entry.pack_forget()
            self.add_question_button.pack_forget()
            self.question_label.pack_forget()
            self.answer_label.pack_forget()
        self.mainmenu.destroy()

    def result_count(self):
        result_label = tk.Label(self, text = self.result_label_str, bg= "#85d2c8")
        result_label.pack()#expand=True)
    #Считаем общий балл

        if self.open_file_flag == 0:
            result_count_label = tk.Label(self, text = ("Общий балл: " + str(self.result_counter) + "/" + str(len(self.questions))), font=(20), bg= "#85d2c8")
        else:
              result_count_label = tk.Label(self, text = ("Общий балл: " + str(self.result_counter) + "/" + str(len(self.questions_txt)-1)), font=(20), bg= "#85d2c8")
        result_count_label.pack(side=tk.BOTTOM)
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
        
    def line_switch(self,question):
        self.update()
        char_width = 0
        width_question = self.question_label.winfo_width()
        if width_question > 200:
            char_width = width_question / len(question)
            wrapped_text = '\n'.join(wrap(question, int(200 / char_width)))
            self.question_label.config(text = wrapped_text)
        return width_question


    def submit_answer(self):
        # Получаем ответ на вопрос
        answer = self.answer_entry.get()
        # Обрабатываем ответ на вопрос
        # Здесь можно сохранять ответы в базу данных или файл
        if self.open_file_flag == 0:
            question = self.questions[self.question_index]
            is_correct = answer.lower() == question['answer'].lower()
        else:
            question = self.questions_txt[self.question_num-1][0]
            is_correct = (answer.lower() == str(self.questions_txt[self.question_num-1][1]).lower())
        
        if is_correct:
            self.result_counter += 1
        else:
            self.result_counter -= 1
        self.show_result(is_correct)
        
        # Очищаем поле для ввода ответа
        self.answer_entry.delete(0, tk.END)

        # Переключаемся на следующий вопрос (если есть)
        if self.open_file_flag == 0:
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
        if self.open_file_flag == 1:
            self.question_num += 1
            if self.question_num < (len(self.questions_txt)):
                question = self.questions_txt[self.question_num-1][0]
                self.title_label.config(text="Опрос")
                self.question_label.config(text=question)
                self.line_switch(question)
            else:
                self.title_label.config(text="Опрос завершен", font=(14))
                self.answer_entry.pack_forget()
                self.answer_label.pack_forget()
                self.question_label.pack_forget()
                self.submit_button.pack_forget()
                self.result_count()

        
    def submit_quiz(self):

            #Добавляем кнопку ответа
        self.submit_button.pack()
        
        if self.open_file_flag == 0:
        # Очищаем поля для ввода вопроса и ответа
                self.question_entry.pack_forget()
                self.question_entry.delete(0, tk.END)
                self.answer_entry.delete(0, tk.END)
            #Выводим вопрос
                question = self.questions[self.question_index]
                self.question_label.config(text=question['question'])
                #Удаляем лишние кнопочки
                self.add_question_button.pack_forget()
                self.submit_quiz_button.destroy()
                
        if self.open_file_flag == 1:
                self.answer_entry.delete(0, tk.END)
                self.question_label.pack()
                question = self.questions_txt[self.question_num][0]
                self.question_label.config(text=(question))
                self.question_num += 1
                self.submit_quiz_button.destroy()
                self.answer_entry.pack()



    def show_result(self, is_correct):
        # Создаем метку для вывода результата
        if self.open_file_flag == False:
            question = self.questions[self.question_index]
            self.question_num_text = (str(self.question_index+1) + ". Вопрос: " + str(question['question'])+ " Ответ: " + str(question['answer']))
            
                
        if self.open_file_flag:
            question = self.questions_txt[self.question_num-1][0]
            answer = self.questions_txt[self.question_num-1][1]
            self.question_num_text = ((str(int(self.question_num))) + ". Вопрос: " + str(question)+ " Ответ: " + str(answer))
        if is_correct:
            result_text = self.question_num_text + ". " + "Верно!"
            
        else:
            result_text = self.question_num_text + ". " "Неверно!"
        self.result_label_str = self.result_label_str + '\n' + result_text
        print(self.result_label_str)
        #result_label = tk.Label(self, text = self.result_label_str, bg= "#85d2c8")
        #result_label.pack()#expand=True)
        self.update()
        # char_width = 0
        # width_question_num_text = result_label.winfo_width()
        # height_question_num_text = result_label.winfo_height()

        # if width_question_num_text > 200:
        #     char_width = width_question_num_text / len(self.question_num_text)
        #     wrapped_text = '\n'.join(wrap(self.question_num_text, int(200 / char_width)))
        #     wrapped_text = wrapped_text +  ". Верно!" if is_correct else wrapped_text + ". Неверно!"
        #     result_label.config(text = wrapped_text)
        # if height_question_num_text <= 21:
        #     if self.open_file_flag == False:
        #         #if self.question_index > 8:
        #         char_height = height_question_num_text 
        #         wrapp_text = (self.question_num_text)
        #         font_size = int(((len(self.questions)*char_height))%10)
        #         result_label.config(font = ("Arial", font_size))
        #         print(str(font_size) + " -------- Font size")
        #         print(str(len(self.questions)) + "-------- Len questions")
        #         print(str(char_height) + " -------- Char height")
        #         print(str(self.question_index) + " -------- Question_index")
        #         print(str(height_question_num_text) + " -------- Height_question_num_text")
        #         print("----------------------------------------------------------------")
        #         self.update()
        #     if self.open_file_flag:
        #         char_height = height_question_num_text 
        #         wrapp_text = (self.question_num_text)
        #         font_size = int(((len(self.questions_txt)*char_height))%char_height)
        #         result_label.config(font = ("Arial", font_size))
        #         print(str(font_size) + " -------- Font size")
        #         print(str(len(self.questions_txt)) + "-------- Len questions")
        #         print(str(char_height) + " -------- Char height")
        #         #print(str(self.question_index) + " -------- Question_index")
        #         print(str(height_question_num_text) + " -------- Height_question_num_text")
        #         print("----------------------------------------------------------------")
        #         self.update()
        # self.update()

if __name__ == '__main__':
    app = SurveyApplication()
    app.mainloop()