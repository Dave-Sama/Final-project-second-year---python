from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk



# user_data represent the login and password of the users in the system
users_data = {'a': ['a', 'S'], 'b': ['b', 'L'], 'c': ['c', 'C']}

# questions represent the questions that are stored in the database of the system
# each question are stored into a dictionary with the following format:
# {key:" specific ID of the question " : values: "list of:"[ 'Question itself', 'Course', 'Sub-subject',
# , 'Difficulty', 'Year', 'Has an answer', 'From exam/quiz', 'Semester', 'Format']}
questions = {1: ['hello', 'Calculus1', 'Integrals', 'Easy', 2019, 'Yes', 'Exam', 'A', 'Docx'], 2: ['moto', 'Calculus2', 'banana', 'hard', 2020, 'No', 'Quiz', 'A', 'Pdf']}
