# import tkinter as tk

# class QuizRunner:
#     def __init__(self, master):
#         self.master = master
#         master.title("QuizRunner")

#         # create and place widgets
#         self.question_label = tk.Label(master, text="Question:")
#         self.question_label.grid(row=0, column=0)

#         self.question_entry = tk.Entry(master)
#         self.question_entry.grid(row=0, column=1)

#         self.answer_label = tk.Label(master, text="Answer:")
#         self.answer_label.grid(row=1, column=0)

#         self.answer_entry = tk.Entry(master)
#         self.answer_entry.grid(row=1, column=1)

#         self.add_button = tk.Button(master, text="Add", command=self.add_question)
#         self.add_button.grid(row=2, column=0)

#         self.start_button = tk.Button(master, text="Start", command=self.start_quiz)
#         self.start_button.grid(row=2, column=1)

#         self.question_listbox = tk.Listbox(master)
#         self.question_listbox.grid(row=3, column=0, columnspan=2)

#     def add_question(self):
#         question = self.question_entry.get()
#         answer = self.answer_entry.get()
#         self.question_listbox.insert(tk.END, f"{question} - {answer}")
#         self.question_entry.delete(0, tk.END)
#         self.answer_entry.delete(0, tk.END)

#     def start_quiz(self):
#     # Hide the question input fields and start button
#         self.question_label.grid_remove()
#         self.question_entry.grid_remove()
#         self.answer_label.grid_remove()
#         self.answer_entry.grid_remove()
#         self.add_button.grid_remove()
#         self.start_button.grid_remove()

#         # Display the quiz questions and answer input fields
#         questions = [self.question_listbox.get(idx) for idx in range(self.question_listbox.size())]
#         self.current_question_idx = 0
#         self.num_correct_answers = 0

#         self.quiz_question_label = tk.Label(self.master, text=questions[self.current_question_idx])
#         self.quiz_question_label.grid(row=0, column=0)

#         self.quiz_answer_entry = tk.Entry(self.master)
#         self.quiz_answer_entry.grid(row=1, column=0)

#         self.quiz_submit_button = tk.Button(self.master, text="Submit", command=self.submit_answer)
#         self.quiz_submit_button.grid(row=2, column=0)

#         self.quiz_progress_label = tk.Label(self.master, text=f"{self.current_question_idx + 1}/{len(questions)}")
#         self.quiz_progress_label.grid(row=3, column=0)

#         self.time_remaining_label = tk.Label(self.master, text=f"Time remaining: {self.time_limit} seconds")
#         self.time_remaining_label.grid(row=4, column=0)

#         self.timer = threading.Timer(self.time_limit, self.display_results)
#         self.timer.start()

    # def submit_answer(self):
    #     # Check the user's answer and display the next question
    #     questions = [self.question_listbox.get(idx) for idx in range(self.question_listbox.size())]
    #     current_question = questions[self.current_question_idx]
    #     question, answer = current_question.split(" - ")
    #     user_answer = self.quiz_answer_entry.get().strip().lower()

    #     if user_answer == answer.lower():
    #         self.num_correct_answers += 1

    #     self.quiz_answer_entry.delete(0, tk.END)
    #     self.current_question_idx += 1

    #     if self.current_question_idx < len(questions):
    #         self.quiz_question_label.config(text=questions[self.current_question_idx])
    #         self.quiz_progress_label.config(text=f"{self.current_question_idx + 1}/{len(questions)}")
    #     else:
    #         self.display_results()

    # def display_results(self):
    #     # Display the user's score and reset the quiz
    #     num_questions = self.question_listbox.size()
    #     score = self.num_correct_answers / num_questions * 100
    #     score_message = f"You answered {self.num_correct_answers} out of {num_questions} questions correctly. Your score is {score:.2f}%."
    #     self.quiz_question_label.config(text=score_message)
    #     self.quiz_answer_entry.grid_remove()
    #     self.quiz_submit_button.grid_remove()
    #     self.quiz_progress_label.grid_remove()

    #     self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_quiz)
    #     self.restart_button.grid(row=2, column=0)

    # def restart_quiz(self):
    #     # Reset the quiz to the beginning
    #     self.quiz_question_label.destroy()
    #     self.quiz_answer_entry.destroy()
    #     self.quiz_submit_button.destroy()
    #     self.quiz_progress_label.destroy()
    #     self.restart_button.destroy()
    #     self.question_label.grid()
    #     self.question_entry.grid()
    #     self.answer_label.grid()
    #     self.answer_entry.grid()
    #     self.add_button.grid()
    #     self.start_button.grid()
    #     self.question_listbox.delete(0, tk.END)
    #     self.current_question_idx = 0
    #     self.num_correct_answers = 0

# root = tk.Tk()
# app = QuizRunner(root)
# root.mainloop()

from tkinter import *
import sqlite3

root = Tk()
root.title("Опросы")

question_label = Label(root, text="Введите вопрос:")
question_label.grid(row=0, column=0, padx=10, pady=10)

question_entry = Entry(root, width=50)
question_entry.grid(row=0, column=1, padx=10, pady=10)

answer_label = Label(root, text="Введите верный ответ:")
answer_label.grid(row=1, column=0, padx=10, pady=10)

answer_entry = Entry(root, width=50)
answer_entry.grid(row=1, column=1, padx=10, pady=10)

conn = sqlite3.connect("questions.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)")
conn.commit()

def save_question():
    question = question_entry.get()
    answer = answer_entry.get()

    cursor.execute("INSERT INTO questions (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()

save_button = Button(root, text="Сохранить", command=save_question)
save_button.grid(row=2, column=0, padx=10, pady=10)

def start_quiz():
    questions = []
    answers = []

    cursor.execute("SELECT  FROM questions")
    rows = cursor.fetchall()

    for row in rows:
        question, answer = row
        questions.append(question)
        answers.append(answer)

    quizlabel = Label(root, text="Ответьте на вопросы:")
    quizlabel.grid(row=3, column=0, padx=10, pady=10)

    for i in range(len(questions)):
        questionlabel = Label(root, text=questions[i])
        questionlabel.grid(row=i+4, column=0, padx=10, pady=10)

        answerentry = Entry(root, width=50)
        answerentry.grid(row=i+4, column=1, padx=10, pady=10)

    submitbutton = Button(root, text="Проверить", command=lambda: checkanswers(answers))
    submitbutton.grid(row=len(questions)+5, column=0, padx=10, pady=10)

def checkanswers(answers):
    useranswers = []

    for i in range(len(answers)):
        answer = root.gridslaves(row=i+4, column=1).get()
        useranswers.append(answer)

    correct = 0
    for i in range(len(answers)):
        if useranswers.lower() == answers.lower():
            correct += 1

    result_label = Label(root, text=f"Вы ответили правильно на {correct} из {len(answers)} вопросов.")
    result_label.grid(row=len(answers)+6, column=0, padx=10, pady=10)

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Новый вопрос", command=lambda: root.focus())
file_menu.add_command(label="Начать опрос", command=start_quiz)

root.mainloop()