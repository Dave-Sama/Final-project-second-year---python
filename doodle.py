
import os
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from data_base import *
import tkinter as tk

root = Tk()
root.geometry('240x340')
Label(root, text='Fill form:').place(x=80, y=0)

# creating a Label for courses:
Label(root, text='Course: ').place(x=2, y=40)


# creating combobox for the courses:
combo_course = Combobox(root, width=14)
combo_course['values'] = ('Calculus1', 'Linear algebra', 'Pre computer science', 'Architecture', "Logic 1")
combo_course.current(0)  # set the selected item
combo_course.place(x=80, y=40)

# creating a button for courses:

Button(root, text='OK', width=3, state=DISABLED).place(x=192, y=35)

# creating a Label for courses:
Label(root, text='Sub subject: ').place(x=2, y=70)

# creating combobox for the sub-subjects:
root.combo_sub_subject = Combobox(root)
root.combo_sub_subject['values'] = ('not yet', 'not yet', 'not yet', 'not yet', "not yet")
root.combo_sub_subject.current(0)  # set the selected item
root.combo_sub_subject.place(x=80, y=70)

# creating a Label for Difficulty:
Label(root, text='Difficulty: ').place(x=2, y=100)

# creating combobox for the difficulty:
root.combo_difficulty = Combobox(root)
root.combo_difficulty['values'] = ('Easy', 'Moderate', 'Hard')
root.combo_difficulty.current(0)  # set the selected item
root.combo_difficulty.place(x=80, y=100)

# creating a Label for Answers:
Label(root, text='Answers: ').place(x=2, y=130)


# creating combobox for the Answers:
root.combo_answers = Combobox(root, width=14)
root.combo_answers['values'] = ('Yes', 'No')
root.combo_answers.current(0)  # set the selected item
root.combo_answers.place(x=80, y=130)


# creating a button for courses:
Button(root, text='OK', width=3, height=1, state=DISABLED).place(x=192, y=125)

# creating a Label for Years:
Label(root, text='Year:').place(x=2, y=160)

# creating spinbox for the Years:
var = IntVar()
var.set(2019)
root.spin_years = Spinbox(root, from_=1995, to=2020, width=22, textvariable=var)
root.spin_years.place(x=80, y=160)

# creating Label for the semester:
Label(root, text='Semester:').place(x=2, y=190)

# creating a combobox for the Semester:
root.combo_semester = Combobox(root)
root.combo_semester['values'] = ('A', 'B', 'Summer')
root.combo_semester.current(0)  # set the selected item
root.combo_semester.place(x=80, y=190)

# creating a Label for Format:
Label(root, text='Format:').place(x=2, y=220)
# creating a combobox for Format:
root.combo_format = Combobox(root)
root.combo_format['values'] = ('Docx', 'Pdf', 'Jpeg')
root.combo_format.current(0)  # set the selected item
root.combo_format.place(x=80, y=220)

# creating Label for the Exam/Quiz:
Label(root, text='From:').place(x=2, y=250)

# creating a combobox for the Exam/Quiz:
root.combo_from = Combobox(root)
root.combo_from['values'] = ('Exam', 'Quiz')
root.combo_from.current(0)  # set the selected item
root.combo_from.place(x=80, y=250)

# crating an Accept button:
Button(root, text='Accept', width=20,  state=DISABLED).place(x=40, y=290)

root.mainloop()