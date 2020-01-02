"""
 all the imported libraries/API for this project:
"""
import os
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image, ImageOps
from data_base import *
import tkinter as tk
import PyPDF2
import base64
import docx2txt

class GUI(object):
    def __init__(self):
        # setting the root
        root = self.root = tk.Tk()
        root.title('Test')
        root.geometry('310x85')

        # make Esc exit the program
        root.bind('<Escape>', lambda e: root.destroy())

        # create a menu bar with an Exit command
        menu_bar = Menu(root)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=root.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menu_bar)

        Label(self.root, text=" UserName: ").grid(row=0, column=0, sticky=W)
        Label(self.root, text=" Password: ").grid(row=1, column=0, sticky=W)

        # creating 2 text boxes to insert the user's information to the system, with the "Text" method:
        self.username_field = Entry(self.root, width=35)
        self.username_field.grid(row=0, column=1)
        self.password_field = Entry(self.root, show="•", width=35)
        self.password_field.grid(row=1, column=1)

        # creating "Accept" button:
        Button(self.root, text='Accept', command=self.login_verify).grid(row=4, column=1, padx=10, pady=10)

    def sub_subject_check(self, key):
        if key == 0:
            if self.combo_course.get() == 'Calculus1':
                # creating a Label for courses:
                Label(self.self_add, text='Sub subject: ').place(x=2, y=70)

                # creating combobox for the sub-subjects:
                self.combo_sub_subject = Combobox(self.self_add)
                self.combo_sub_subject['values'] = ('Integrals', 'Series', 'Derivatives', 'Investigation of functions', 'Limits')
                self.combo_sub_subject.current(0)  # set the selected item
                self.combo_sub_subject.place(x=80, y=70)

            elif self.combo_course.get() == 'Linear algebra':
                # creating a Label for courses:
                Label(self.self_add, text='Sub subject: ').place(x=2, y=70)

                # creating combobox for the sub-subjects:
                self.combo_sub_subject = Combobox(self.self_add)
                self.combo_sub_subject['values'] = ('Spans', 'Matrices', 'Vectors', 'base and 3D', "Determinate")
                self.combo_sub_subject.current(0)  # set the selected item
                self.combo_sub_subject.place(x=80, y=70)

            elif self.combo_course.get() == 'Pre computer science':
                # creating a Label for courses:
                Label(self.self_add, text='Sub subject: ').place(x=2, y=70)

                # creating combobox for the sub-subjects:
                self.combo_sub_subject = Combobox(self.self_add)
                self.combo_sub_subject['values'] = ('Functions', 'Variables', 'Structs', 'Recursions', 'Classes')
                self.combo_sub_subject.current(0)  # set the selected item
                self.combo_sub_subject.place(x=80, y=70)

            elif self.combo_course.get() == 'Architecture':
                # creating a Label for courses:
                Label(self.self_add, text='Sub subject: ').place(x=2, y=70)

                # creating combobox for the sub-subjects:
                self.combo_sub_subject = Combobox(self.self_add)
                self.combo_sub_subject['values'] = ('PLA/PAL', 'Diagrams', 'RTL', 'Logging gates', "RAM")
                self.combo_sub_subject.current(0)  # set the selected item
                self.combo_sub_subject.place(x=80, y=70)

            elif self.combo_course.get() == 'Logic 1':
                # creating a Label for courses:
                Label(self.self_add, text='Sub subject: ').place(x=2, y=70)

                # creating combobox for the sub-subjects:
                self.combo_sub_subject = Combobox(self.self_add)
                self.combo_sub_subject['values'] = ('Predicates', 'Logical expressions', 'Inductions', 'Logic', 'Graphs')
                self.combo_sub_subject.current(0)  # set the selected item
                self.combo_sub_subject.place(x=80, y=70)

        elif key == 1:
            if self.combo_course.get() == 'Calculus1':
                # creating a Label for courses:
                Label(self.student_Lecturer_top, text='   Sub subject: ').place(x=192, y=0)

                # creating combobox for the sub-subjects:
                self.combo_sub_subject = Combobox(self.student_Lecturer_top)
                self.combo_sub_subject['values'] = ('Integrals', 'Series', 'Derivatives', 'Investigation of functions', 'Limits')
                self.combo_sub_subject.current(0)  # set the selected item
                self.combo_sub_subject.place(x=274, y=0)

            elif self.combo_course.get() == 'Linear algebra':
                # creating a Label for courses:
                Label(self.student_Lecturer_top, text='   Sub subject: ').place(x=192, y=0)

                # creating combobox for the sub-subjects:
                self.combo_sub_subject = Combobox(self.student_Lecturer_top)
                self.combo_sub_subject['values'] = ('Spans', 'Matrices', 'Vectors', 'base and 3D', "Determinate")
                self.combo_sub_subject.current(0)  # set the selected item
                self.combo_sub_subject.place(x=274, y=0)

            elif self.combo_course.get() == 'Pre computer science':
                # creating a Label for courses:
                Label(self.student_Lecturer_top, text='   Sub subject: ').place(x=192, y=0)

                # creating combobox for the sub-subjects:
                self.combo_sub_subject = Combobox(self.student_Lecturer_top)
                self.combo_sub_subject['values'] = ('Functions', 'Variables', 'Structs', 'Recursions', 'Classes')
                self.combo_sub_subject.current(0)  # set the selected item
                self.combo_sub_subject.place(x=274, y=0)

            elif self.combo_course.get() == 'Architecture':
                # creating a Label for courses:
                Label(self.student_Lecturer_top, text='   Sub subject: ').place(x=192, y=0)

                # creating combobox for the sub-subjects:
                self.combo_sub_subject = Combobox(self.student_Lecturer_top)
                self.combo_sub_subject['values'] = ('PLA/PAL', 'Diagrams', 'RTL', 'Logging gates', "RAM")
                self.combo_sub_subject.current(0)  # set the selected item
                self.combo_sub_subject.place(x=274, y=0)

            elif self.combo_course.get() == 'Logic 1':
                # creating a Label for courses:
                Label(self.student_Lecturer_top, text='   Sub subject: ').place(x=192, y=0)

                # creating combobox for the sub-subjects:
                self.combo_sub_subject = Combobox(self.student_Lecturer_top)
                self.combo_sub_subject['values'] = ('Predicates', 'Logical expressions', 'Inductions', 'Logic', 'Graphs')
                self.combo_sub_subject.current(0)  # set the selected item
                self.combo_sub_subject.place(x=274, y=0)

    def add_answer(self):
        '''
                Opens the Browse window to upload answers
                :return: Browse window
                '''

        # creating the path to the required file (jpeg/pdf **NOTE**:: *TEXT/docx* IS STILL MISSING )
        self.self_add.answerFile = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Jpeg files", "*.Jpeg"), ("Pdf files", "*.Pdf"),  ("Jpg files", "*.Jpg"), ("Docx files", "*.Docx")))

        # we need to check the answer's format:
        self.answer_file_format = self.self_add.answerFile.rpartition('.')[-1]

        # print(question_file_format)
        if self.answer_file_format == 'jpeg' or self.answer_file_format == 'jpg':

            size = (350, 350)
            thumb = ImageOps.fit(Image.open(self.self_add.answerFile), size, Image.ANTIALIAS)
            thumb.save(self.self_add.answerFile.format(self.self_add.answerFile[:self.self_add.answerFile.rfind('.')]), "JPEG")

            img = ImageOps.fit(Image.open(self.self_add.answerFile), size, Image.ANTIALIAS)
            self.img_answer = ImageTk.PhotoImage(img)


            with open(self.self_add.answerFile, "rb") as imageFile:

                # saving the image as reference to display it later if needed.
                self.str_img_answer = base64.b64encode(imageFile.read())

        elif self.answer_file_format == 'pdf':
            # if the file is in a PDF format:
            self.pdf_answer = ""
            pdfFileObj = open(self.self_add.answerFile, 'rb')

            # creating a pdf reader object
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

            # printing number of pages in pdf file
            # print(pdfReader.numPages)

            # creating a page object

            for i in range(0, pdfReader.numPages):
                pageObj = pdfReader.getPage(i)

                # extracting text from page
                self.pdf_answer = self.pdf_answer + str(pageObj.extractText())

            # organizing the text which is extracted from the pdf to a: 10 words per line format:
            count = 0
            for i in range(0, len(self.pdf_answer)):
                if self.pdf_answer[i] == ' ':
                    if count < 10:
                        count += 1
                    else:
                        self.pdf_answer = self.pdf_answer[0: i] + "\n" + self.pdf_answer[i:]
                        count = 0

            # print(pdf_question)

            # closing the pdf file object
            pdfFileObj.close()

        elif self.answer_file_format == 'docx':
            text = docx2txt.process(self.self_add.answerFile)
            self.docx_answer = text

            # organizing the text which is extracted from the pdf to a: 10 words per line format:
            count = 0
            for i in range(0, len(self.docx_answer)):
                if self.docx_answer[i] == ' ':
                    if count < 10:
                        count += 1
                    else:
                        self.docx_answer = self.docx_answer[0: i] + "\n" + self.docx_answer[i:]
                        count = 0

        # extracting the name of the file from it's path to display it in fill form
        answerFileName = self.self_add.answerFile.rpartition('/')[-1]
        # print(answerFileName)

        # creating the new text box with the name of the file in it:
        self.self_add.browseText = tk.Text(self.self_add, height=1, width=15)
        self.self_add.browseText.insert(INSERT, answerFileName)
        self.self_add.browseText.place(x=110, y=125)

        self.combo_answers = 'Yes'

    def add_question(self):
        """
        this method can open the dialog through tkinter, to choose an image from the user's pc and upload it to the data base.
        """
        # adding a new top level to our tk - on this level the the fill form will be represented.
        self.self_add = Toplevel(self.student_Lecturer_top)
        self.self_add.geometry('240x340')

        # identifier key

        # default answer is No:
        self.combo_answers = 'No'
        key = 0

        # opening the dialog to choose the path to the wanted question
        self.self_add.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Jpeg files", "*.Jpeg"), ("Pdf files", "*.Pdf"), ("Jpg files", "*.Jpg"), ("Docx files", "*.Docx")))

        # we need to check the question's format:
        self.question_file_format = self.self_add.filename.rpartition('.')[-1]
        #print(question_file_format)

        if self.question_file_format == 'jpeg' or self.question_file_format == 'jpg':

            size = (350, 350)
            thumb = ImageOps.fit(Image.open(self.self_add.filename), size, Image.ANTIALIAS)
            thumb.save(self.self_add.filename.format(self.self_add.filename[:self.self_add.filename.rfind('.')]), "JPEG")

            img = ImageOps.fit(Image.open(self.self_add.filename), size, Image.ANTIALIAS)
            self.img_question = ImageTk.PhotoImage(img)

            with open(self.self_add.filename, "rb") as imageFile:
                self.str_img_question = base64.b64encode(imageFile.read())

            # imgdata = base64.b64decode(self.str_img_question)

            # filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
            # with open(filename, 'wb') as f:
            #     f.write(imgdata)

            # opening the image for tkinter.
            # size = (300, 300)
            # img = ImageOps.fit(Image.open(self.self_add.filename), size, Image.ANTIALIAS)
            # self.img_question = ImageTk.PhotoImage(img)
            # self.question_display = Label(self.student_Lecturer_top, image=self.img_question)
            # self.questions_display = self.img_question
            # self.question_display.place(x=260, y=100)
        elif self.question_file_format == 'pdf':
            #if the file is in a PDF format:
            self.pdf_question = ""
            pdfFileObj = open(self.self_add.filename, 'rb')

            # creating a pdf reader object
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

            # printing number of pages in pdf file
            # print(pdfReader.numPages)

            # creating a page object

            for i in range(0, pdfReader.numPages):
                pageObj = pdfReader.getPage(i)

                # extracting text from page
                self.pdf_question = self.pdf_question + str(pageObj.extractText())

            # organizing the text which is extracted from the pdf to a: 10 words per line format:
            count = 0
            for i in range(0, len(self.pdf_question)):
                if self.pdf_question[i] == ' ':
                    if count < 15:
                        count += 1
                    else:
                        self.pdf_question = self.pdf_question[0: i] + "\n" + self.pdf_question[i:]
                        count = 0

            # print(pdf_question)

            # closing the pdf file object
            pdfFileObj.close()

        elif self.question_file_format == 'docx':
            text = docx2txt.process(self.self_add.filename)
            self.docx_question = text
            # organizing the text which is extracted from the pdf to a: 10 words per line format:
            count = 0
            for i in range(0, len(self.docx_question)):
                if self.docx_question[i] == ' ':
                    if count < 10:
                        count += 1
                    else:
                        self.docx_question = self.docx_question[0: i] + "\n" + self.docx_question[i:]
                        count = 0

        # /////////////////////////////////// #
        # ------ creating the fill form :     #
        # /////////////////////////////////// #

        Label(self.self_add, text='Fill form:').place(x=80, y=0)

        # creating a Label for courses:
        Label(self.self_add, text='Course: ').place(x=2, y=40)

        # creating combobox for the courses:
        self.combo_course = Combobox(self.self_add, width=14)
        self.combo_course['values'] = ('Calculus1', 'Linear algebra', 'Pre computer science', 'Architecture', "Logic 1")
        self.combo_course.current(0)  # set the selected item
        self.combo_course.place(x=80, y=40)

        # creating a button for courses:
        if self.combo_course.get() == None:
            Button(self.self_add, text='Apply', width=4, state=DISABLED).place(x=192, y=35)
        else:
            Button(self.self_add, text='Apply', width=4, command=lambda: self.sub_subject_check(key)).place(x=192, y=35)

        # creating a Label for courses:
        Label(self.self_add, text='Sub subject: ').place(x=2, y=70)

        # creating combobox for the sub-subjects:
        self.combo_sub_subject = Combobox(self.self_add)
        self.combo_sub_subject['values'] = ('not yet')
        self.combo_sub_subject.current(0)  # set the selected item
        self.combo_sub_subject.place(x=80, y=70)

        # creating a Label for Difficulty:
        Label(self.self_add, text='Difficulty: ').place(x=2, y=100)

        # creating combobox for the difficulty:
        self.combo_difficulty = Combobox(self.self_add)
        self.combo_difficulty['values'] = ('Easy', 'Moderate', 'Hard')
        self.combo_difficulty.current(0)  # set the selected item
        self.combo_difficulty.place(x=80, y=100)

        # creating a Label and a Button for Answers:
        Label(self.self_add, text='Answers: ').place(x=2, y=130)
        self.self_add.browseButton = Button(self.self_add, command=self.add_answer, text='...', width=2, height=1).place(x=80, y=125)
        self.self_add.browseText = tk.Text(self.self_add, height=1, width=15, state="disabled").place(x=110, y=125)

        # creating a Label for Years:
        Label(self.self_add, text='Year:').place(x=2, y=160)

        # creating spinbox for the Years:
        var = IntVar()
        var.set(2019)
        self.spin_years = Spinbox(self.self_add, from_=1995, to=2020, width=21, textvariable=var)
        self.spin_years.place(x=80, y=160)

        # creating Label for the semester:
        Label(self.self_add, text='Semester:').place(x=2, y=190)

        # creating a combobox for the Semester:
        self.combo_semester = Combobox(self.self_add)
        self.combo_semester['values'] = ('A', 'B', 'Summer')
        self.combo_semester.current(0)  # set the selected item
        self.combo_semester.place(x=80, y=190)

        # creating a Label for Format:
        Label(self.self_add, text='Format:').place(x=2, y=220)

        # creating a combobox for Format:
        self.combo_format = Combobox(self.self_add)
        self.combo_format['values'] = ('Docx', 'Pdf', 'Jpeg')
        self.combo_format.current(0)  # set the selected item
        self.combo_format.place(x=80, y=220)

        # creating Label for the Exam/Quiz:
        Label(self.self_add, text='From:').place(x=2, y=250)

        # creating a combobox for the Exam/Quiz:
        self.combo_from = Combobox(self.self_add)
        self.combo_from['values'] = ('Exam', 'Quiz')
        self.combo_from.current(0)  # set the selected item
        self.combo_from.place(x=80, y=250)

        # crating an Accept button:
        Button(self.self_add, text='Accept', command=self.add_question_to_db, width=20).place(x=40, y=290)

    def add_question_to_db(self):
        """
        this method can add a question/question+ answer to the data base.
        """

        # adding the question/question + answer, with all it's information:
        if self.question_file_format == 'jpeg' or self.question_file_format == 'jpg':
            if self.answer_file_format == 'pdf':
                questions = [self.str_img_question, self.pdf_answer, self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get(), self.answer_file_format]
                print(self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get())

                # in order to add a question to our file, we need to open it as a string, and evaluate it to it's former meaning

                with open('questions.txt', mode='r') as file:
                    eval_list = file.read()

                    # evaluating the content of the file to it's former meanings
                    eval_list = eval(eval_list)

                    # after the evaluation, if the list is empty, we want to append it with our question's information
                    if not eval_list:
                        eval_list.append([0, questions])

                    # if the question isn't empty, append the question, with the right number of question
                    else:
                        eval_list.append([len(eval_list), questions])

                # now after the appending, we want to represent the list as a string, and put it into the file:
                with open('questions.txt', mode='w') as file:
                    file.write(repr(eval_list))


            elif self.answer_file_format == 'jpeg' or self.answer_file_format == 'jpg':
                questions = [self.str_img_question, self.str_img_answer, self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get(), self.answer_file_format]
                print(self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(),  self.combo_semester.get(), self.combo_format.get())

                # in order to add a question to our file, we need to open it as a string, and evaluate it to it's former meaning

                with open('questions.txt', mode='r') as file:
                    eval_list = file.read()
                    self.self_add.destroy()


                    # evaluating the content of the file to it's former meanings
                    eval_list = eval(eval_list)

                    # after the evaluation, if the list is empty, we want to append it with our question's information
                    if not eval_list:
                        eval_list.append([0, questions])

                    # if the question isn't empty, append the question, with the right number of question
                    else:
                        eval_list.append([len(eval_list), questions])

                # now after the appending, we want to represent the list as a string, and put it into the file:
                with open('questions.txt', mode='w') as file:
                    file.write(repr(eval_list))

            elif self.answer_file_format == 'docx':
                questions = [self.str_img_question, self.docx_answer, self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get(), self.answer_file_format]
                print(self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get())

                # in order to add a question to our file, we need to open it as a string, and evaluate it to it's former meaning

                with open('questions.txt', mode='r') as file:
                    eval_list = file.read()
                    self.self_add.destroy()

                    # evaluating the content of the file to it's former meanings
                    eval_list = eval(eval_list)

                    # after the evaluation, if the list is empty, we want to append it with our question's information
                    if not eval_list:
                        eval_list.append([0, questions])

                    # if the question isn't empty, append the question, with the right number of question
                    else:
                        eval_list.append([len(eval_list), questions])

                # now after the appending, we want to represent the list as a string, and put it into the file:
                with open('questions.txt', mode='w') as file:
                    file.write(repr(eval_list))

        elif self.question_file_format == 'pdf':
            if self.answer_file_format == 'pdf':
                questions = [self.pdf_question, self.pdf_answer, self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get(), self.answer_file_format]
                print(self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get())

                # in order to add a question to our file, we need to open it as a string, and evaluate it to it's former meaning

                with open('questions.txt', mode='r') as file:
                    eval_list = file.read()

                    # evaluating the content of the file to it's former meanings
                    eval_list = eval(eval_list)

                    # after the evaluation, if the list is empty, we want to append it with our question's information
                    if not eval_list:
                        eval_list.append([0, questions])

                    # if the question isn't empty, append the question, with the right number of question
                    else:
                        eval_list.append([len(eval_list), questions])

                # now after the appending, we want to represent the list as a string, and put it into the file:
                with open('questions.txt', mode='w') as file:
                    file.write(repr(eval_list))
            elif self.answer_file_format == 'jpeg' or self.answer_file_format == 'jpg':
                questions = [self.pdf_question, self.str_img_answer, self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(),  self.combo_semester.get(), self.combo_format.get(), self.answer_file_format]
                print(self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(),  self.combo_semester.get(), self.combo_format.get())

                # in order to add a question to our file, we need to open it as a string, and evaluate it to it's former meaning

                with open('questions.txt', mode='r') as file:
                    eval_list = file.read()

                    # evaluating the content of the file to it's former meanings
                    eval_list = eval(eval_list)

                    # after the evaluation, if the list is empty, we want to append it with our question's information
                    if not eval_list:
                        eval_list.append([0, questions])

                    # if the question isn't empty, append the question, with the right number of question
                    else:
                        eval_list.append([len(eval_list), questions])

                # now after the appending, we want to represent the list as a string, and put it into the file:
                with open('questions.txt', mode='w') as file:
                    file.write(repr(eval_list))

            elif self.answer_file_format == 'docx':
                questions = [self.pdf_question, self.docx_answer, self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get(), self.answer_file_format]
                print(self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get())

                # in order to add a question to our file, we need to open it as a string, and evaluate it to it's former meaning

                with open('questions.txt', mode='r') as file:
                    eval_list = file.read()
                    self.self_add.destroy()

                    # evaluating the content of the file to it's former meanings
                    eval_list = eval(eval_list)

                    # after the evaluation, if the list is empty, we want to append it with our question's information
                    if not eval_list:
                        eval_list.append([0, questions])

                    # if the question isn't empty, append the question, with the right number of question
                    else:
                        eval_list.append([len(eval_list), questions])

                # now after the appending, we want to represent the list as a string, and put it into the file:
                with open('questions.txt', mode='w') as file:
                    file.write(repr(eval_list))

        elif self.question_file_format == 'docx':
            if self.answer_file_format == 'pdf':
                questions = [self.docx_question, self.pdf_answer, self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get(), self.answer_file_format]
                print(self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get())

                # in order to add a question to our file, we need to open it as a string, and evaluate it to it's former meaning

                with open('questions.txt', mode='r') as file:
                    eval_list = file.read()

                    # evaluating the content of the file to it's former meanings
                    eval_list = eval(eval_list)

                    # after the evaluation, if the list is empty, we want to append it with our question's information
                    if not eval_list:
                        eval_list.append([0, questions])

                    # if the question isn't empty, append the question, with the right number of question
                    else:
                        eval_list.append([len(eval_list), questions])

                # now after the appending, we want to represent the list as a string, and put it into the file:
                with open('questions.txt', mode='w') as file:
                    file.write(repr(eval_list))
            elif self.answer_file_format == 'jpeg' or self.answer_file_format == 'jpg':
                questions = [self.docx_question, self.str_img_answer, self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get(), self.answer_file_format]
                print(self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get())

                # in order to add a question to our file, we need to open it as a string, and evaluate it to it's former meaning

                with open('questions.txt', mode='r') as file:
                    eval_list = file.read()

                    # evaluating the content of the file to it's former meanings
                    eval_list = eval(eval_list)

                    # after the evaluation, if the list is empty, we want to append it with our question's information
                    if not eval_list:
                        eval_list.append([0, questions])

                    # if the question isn't empty, append the question, with the right number of question
                    else:
                        eval_list.append([len(eval_list), questions])

                # now after the appending, we want to represent the list as a string, and put it into the file:
                with open('questions.txt', mode='w') as file:
                    file.write(repr(eval_list))

            elif self.answer_file_format == 'docx':
                questions = [self.docx_question, self.docx_answer, self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get(), self.answer_file_format]
                print(self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get())

                # in order to add a question to our file, we need to open it as a string, and evaluate it to it's former meaning

                with open('questions.txt', mode='r') as file:
                    eval_list = file.read()
                    self.self_add.destroy()

                    # evaluating the content of the file to it's former meanings
                    eval_list = eval(eval_list)

                    # after the evaluation, if the list is empty, we want to append it with our question's information
                    if not eval_list:
                        eval_list.append([0, questions])

                    # if the question isn't empty, append the question, with the right number of question
                    else:
                        eval_list.append([len(eval_list), questions])

                # now after the appending, we want to represent the list as a string, and put it into the file:
                with open('questions.txt', mode='w') as file:
                    file.write(repr(eval_list))

    def crop_question(self):
        """
        this method does the following:
        1. open the open source tool to crop the selected question from the test/quiz.
        2. crop the right place in the image
        3. save it into a folder that is inside the user's pc.
        """
        # this os call should open the open source code, so the user could crop a question.
        os.startfile("C:\\Users\\david\\PycharmProjects\\Pe_fundementals_reworked\\Open source\\new_os_crop.py")

    def display(self, key):

        self.student_Lecturer_top = Toplevel(self.root)

        """
                here should be displayed all the options the students has:
                1. choose a course.
                2. choose a sub-subject for this course.
                3. choose the difficulty for the displayed questions.
                4. choose to display only questions with an answer.
                5. choose a test from specific year
                6. choose a semester
                6. choose a semester
                7. test/quiz
                8. period A/B
                9. format of the question



                here should be displayed all the options the students has:

                1. choose a course.
                2. choose a sub-subject for this course.
                3. choose the difficulty for the displayed questions.
                4. choose to display only questions with an answer.
                5. choose a test from specific year
                6. choose a semester
                7. test/quiz
                8. period A/B
                9. format of the question
                10. add a question to the data base.

        """
        # creating the defining the new layer.
        self.student_Lecturer_top.geometry('840x430')

        # identifier key:
        key1 = 1

        # creating a Label for courses:
        Label(self.student_Lecturer_top, text='Course: ').grid(row=0, column=0)

        # creating combobox for the courses:
        self.combo_course = Combobox(self.student_Lecturer_top, width=14)
        self.combo_course['values'] = ('Calculus1', 'Linear algebra', 'Pre computer science', 'Architecture', "Logic 1")
        self.combo_course.current(0)  # set the selected item
        self.combo_course.grid(row=0, column=1, sticky='W')

        # creating a button for courses: (example)
        if self.combo_course.get() == None:
            Button(self.student_Lecturer_top, text='...', width=3, state=DISABLED).place(x=161, y=0)
        else:
            Button(self.student_Lecturer_top, text='...', width=3, command=lambda: self.sub_subject_check(key1)).place(x=161, y=0)

        # creating a Label for courses:
        Label(self.student_Lecturer_top, text='   Sub subject: ').place(x=192, y=0)

        # creating combobox for the sub-subjects:
        self.combo_sub_subject = Combobox(self.student_Lecturer_top)
        self.combo_sub_subject['values'] = ('not yet', 'not yet', 'not yet', 'not yet', "not yet")
        self.combo_sub_subject.current(0)  # set the selected item
        self.combo_sub_subject.place(x=274, y=0)

        # creating a Label for Difficulty:
        Label(self.student_Lecturer_top, text='  Difficulty: ').place(x=417, y=0)

        # creating combobox for the difficulty:
        self.combo_difficulty = Combobox(self.student_Lecturer_top)
        self.combo_difficulty['values'] = ('Easy', 'Moderate', 'Hard')
        self.combo_difficulty.current(0)  # set the selected item
        self.combo_difficulty.place(x=483, y=0)

        # creating a Label for Answers:
        Label(self.student_Lecturer_top, text='  Answers: ').place(x=626, y=0)

        # creating combobox for the Answers:
        self.combo_answers = Combobox(self.student_Lecturer_top)
        self.combo_answers['values'] = ('Yes', 'No')
        self.combo_answers.current(0)  # set the selected item
        self.combo_answers.place(x=688, y=0)

        # creating a Label for Years:
        Label(self.student_Lecturer_top, text='Year:').place(x=1, y=22)

        if key == 'L' or key == 'C':
            # creating an Add button for the lecturer:
            Button(self.student_Lecturer_top, text='add', width=4, command=self.add_question).place(x=5, y=50)

            # creating a delete question for the lecturer:
            Button(self.student_Lecturer_top, text='delete', width=4, state=DISABLED).place(x=45, y=50)

            # creating a crop question for the lecturer:
            Button(self.student_Lecturer_top, text='crop', width=4, command=self.crop_question).place(x=85, y=50)

        # creating spinbox for the Years:
        var = IntVar()
        var.set(2019)
        self.spin_years = Spinbox(self.student_Lecturer_top, from_=1995, to=2020, width=6, textvariable=var)
        self.spin_years.place(x=49, y=22, width=144)

        # creating Label for the semester:
        Label(self.student_Lecturer_top, text='Semester:').place(x=201, y=22)

        # creating a combobox for the Semester:
        self.combo_semester = Combobox(self.student_Lecturer_top)
        self.combo_semester['values'] = ('A', 'B', 'Summer')
        self.combo_semester.current(0)  # set the selected item
        self.combo_semester.place(x=274, y=22)

        # creating a Label for Format:
        Label(self.student_Lecturer_top, text='Format:').place(x=423, y=22)

        # creating a combobox for Format:
        self.combo_format = Combobox(self.student_Lecturer_top)
        self.combo_format['values'] = ('Docx', 'Pdf', 'Jpeg')
        self.combo_format.current(0)  # set the selected item
        self.combo_format.place(x=483, y=22)

        # creating Label for the Exam/Quiz:
        Label(self.student_Lecturer_top, text='From:').place(x=632, y=22)

        # creating a combobox for the Exam/Quiz:
        self.combo_from = Combobox(self.student_Lecturer_top)
        self.combo_from['values'] = ('Exam', 'Quiz')
        self.combo_from.current(0)  # set the selected item
        self.combo_from.place(x=688, y=22)

        # crating an Accept button:
        Button(self.student_Lecturer_top, text='Accept', command=self.question_match, width=20).place(x=334, y=50)

        # creating forward/backward button for image display:
        self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, state=DISABLED).place(x=488, y=50)
        self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, state=DISABLED).place(x=285, y=50)

    def delete_question(self, index):

        with open('questions.txt', mode='r') as file:
            eval_list = file.read()

            # evaluating the content of the file to it's former meanings
            eval_list = eval(eval_list)


        for i in range(0,len(eval_list)):
            if self.questions_matches[index][0] in eval_list[i]:
                for j in range(i+1, len(eval_list)):
                    eval_list[j][0] -= 1
                eval_list.pop(i)


        # now after the appending, we want to represent the list as a string, and put it into the file:
        with open('questions.txt', mode='w') as file:
            file.write(repr(eval_list))

        messagebox.showinfo('Notice!', 'Question has been deleted.')

    def display_answer(self, index):
        """
        this method can display the answer for the displayed question if the answer is exits
        """

        # opening a new layer to display the answer
        self.answer_display = Toplevel(self.student_Lecturer_top)

        # we need to ask if the answer is in a pdf format or not, because the syntax is different for each state
        if self.questions_matches[index][3] == 'Jpeg':

            imgdata = base64.b64decode(self.questions_matches[index][1])
            filename = 'some_image_answer.jpg'
            with open(filename, 'wb') as f:
                f.write(imgdata)

            self.img_answer = ImageTk.PhotoImage(Image.open(filename))


            self.my_label = Label(self.answer_display, image=self.img_answer)
            self.my_label.image = self.img_answer
            self.my_label.pack()

        elif self.questions_matches[index][3] == 'Pdf':
            self.my_label = Label(self.answer_display, bg='white', text=self.questions_matches[index][1])
            self.my_label.pack()

        elif self.questions_matches[index][3] == 'Docx':
            self.my_label = Label(self.answer_display, bg='white', text=self.questions_matches[index][1])
            self.my_label.pack()

    def forward(self, index):
        """
        this method is handling the logic behind the forward button
        """



        self.my_label.destroy()

        if self.questions_matches[index][2] == 'Jpeg':
            imgdata = base64.b64decode(self.questions_matches[index][0])
            filename = 'some_image_answer.jpg'
            with open(filename, 'wb') as f:
                f.write(imgdata)

            self.img_question = ImageTk.PhotoImage(Image.open(filename))

            self.my_label = tk.Label(self.student_Lecturer_top, image=self.img_question)
            self.my_label.image = self.img_question

            # The Pack geometry manager packs widgets in rows or columns.
            self.my_label.place(x=260, y=100)

            # creating another button to display the answer:
            if self.questions_matches[index][1] != '':
                Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(index)).place(x=126, y=50)
                Button(self.student_Lecturer_top, text='delete', width=4, command=lambda:self.delete_question(index)).place(x=45, y=50)

            else:
                # creating forward/backward button for image display:
                Button(self.student_Lecturer_top, text='Answer', state=DISABLED).place(x=126, y=50)

            if index < (len(self.questions_matches)-1):
                self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, command=lambda: self.forward(index+1)).place(x=488, y=50)
                self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, command=lambda: self.back(index-1)).place(x=285, y=50)
                Button(self.student_Lecturer_top, text='delete', width=4, command=lambda:self.delete_question(index)).place(x=45, y=50)

            else:
                self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, state=DISABLED).place(x=488, y=50)
                self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, command=lambda: self.back(index - 1)).place(x=285, y=50)
                Button(self.student_Lecturer_top, text='delete', width=4, command=lambda:self.delete_question(index)).place(x=45, y=50)

        else:
            self.my_label = tk.Label(self.student_Lecturer_top, bg='white', text=self.questions_matches[index][0])
            self.my_label.place(x=260, y=100)
            Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(index)).place(x=45, y=50)

            # creating another button to display the answer:
            if self.questions_matches[index][1] != '':
                Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(index)).place(x=126, y=50)
                Button(self.student_Lecturer_top, text='delete', width=4, command=lambda:self.delete_question(index)).place(x=45, y=50)

            else:
                # creating forward/backward button for image display:
                Button(self.student_Lecturer_top, text='Answer', state=DISABLED).place(x=126, y=50)
                Button(self.student_Lecturer_top, text='delete', width=4, command=lambda:self.delete_question(index)).place(x=45, y=50)

            if len(self.questions_matches)-1 > index:
                self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, command=lambda: self.forward(index+1)).place(x=488, y=50)
                self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, command=lambda :self.back(index-1)).place(x=285, y=50)
                Button(self.student_Lecturer_top, text='delete', width=4, command=lambda:self.delete_question(index)).place(x=45, y=50)

            else:
                self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, state=DISABLED).place(x=488, y=50)
                self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, command=lambda: self.back(index - 1)).place(x=285, y=50)
                Button(self.student_Lecturer_top, text='delete', width=4, command=lambda:self.delete_question(index)).place(x=45, y=50)

        self.my_label.place(x=260, y=100)

    def back(self, index):
        """
        this method handling the logic behind the back button
        """
        self.my_label.destroy()

        if self.questions_matches[index][2] == 'Jpeg':
            imgdata = base64.b64decode(self.questions_matches[index][0])
            filename = 'some_image_answer.jpg'
            with open(filename, 'wb') as f:
                f.write(imgdata)

            self.img_question = ImageTk.PhotoImage(Image.open(filename))

            self.my_label = tk.Label(self.student_Lecturer_top, image=self.img_question)
            self.my_label.image = self.img_question

            # The Pack geometry manager packs widgets in rows or columns.
            self.my_label.place(x=260, y=100)

            # creating another button to display the answer:
            if self.questions_matches[index][1] != '':
                Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(index)).place(x=126, y=50)

            else:
                # creating forward/backward button for image display:
                Button(self.student_Lecturer_top, text='Answer', state=DISABLED).place(x=126, y=50)

            if index == 0:
                self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, command=lambda: self.forward(index + 1)).place(x=488, y=50)
                self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, state=DISABLED).place(x=285, y=50)

            else:
                self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, command=lambda: self.forward(index + 1)).place(x=488, y=50)
                self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, command=lambda: self.back(index - 1)).place(x=285, y=50)

        else:
            self.my_label = tk.Label(self.student_Lecturer_top, bg='white', text=self.questions_matches[index][0])
            self.my_label.place(x=260, y=100)

            # creating another button to display the answer:
            if self.questions_matches[index][1] != '':
                Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(index)).place(x=126, y=50)

            else:
                # creating forward/backward button for image display:
                Button(self.student_Lecturer_top, text='Answer', state=DISABLED).place(x=126, y=50)

            if index == 0:
                self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, command=lambda: self.forward(index + 1)).place(x=488, y=50)
                self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, state=DISABLED).place(x=285, y=50)

            else:
                self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, command=lambda: self.forward(index + 1)).place(x=488, y=50)
                self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, command=lambda: self.back(index - 1)).place(x=285, y=50)

        self.my_label.place(x=260, y=100)


    def question_match(self):
            """
            this method can find a match from the search bar, and return the matches to the bar
            """

            # my_questions for the data base , temp2 for the users input
            self.questions_matches = []
            my_questions = []
            flag = False
            i = 0

            with open('questions.txt', mode='r') as file:
                my_questions = file.read()
                my_questions = eval(my_questions)

            for i in range(0, len(my_questions)):
                # we need to convert the year to a string to compare it later
                my_questions[i][1][4] = str(my_questions[i][1][4])

            # putting all the user inputs into temp2
            temp2 = [self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers.get(), self.combo_from.get(), self.combo_semester.get(), self.combo_format.get()]

            # checking if the inputs and the outsputs are correct:
            print(f"from combo: {temp2}")

            for data in my_questions:
                print(f"from data base: {data[1][2:]}")

            # checking if there is a match between my_questions and temp2
            for i in range(0, len(my_questions)):
                if my_questions[i][1][2:10] == temp2:  # temp 1 - data base , temp2 - user input
                    if self.combo_format.get() == 'Pdf': # האם המשתמש ביקש שהשאלה תיהיה בPDF
                        if self.combo_answers.get() == 'Yes': # האם המשתמש ביקש שלשאלה יהיה פתרון
                            if my_questions[i][1][10] == 'pdf':
                                self.questions_matches.append([my_questions[i][1][0], my_questions[i][1][1], 'Pdf', 'Pdf'])
                            elif my_questions[i][1][10] == 'jpeg':
                                self.questions_matches.append([my_questions[i][1][0], my_questions[i][1][1], 'Pdf', 'Jpeg'])
                            elif my_questions[i][1][10] == 'docx':
                                self.questions_matches.append([my_questions[i][1][0], my_questions[i][1][1], 'Pdf', 'Docx'])

                        else: # אם המשתמש ביקש שלשאלה לא יהיה פיתרון
                            self.questions_matches.append([my_questions[i][1][0], '', 'Pdf', 'No'])

                    elif self.combo_format.get() == 'Docx': # האם המשתמש ביקש שהשאלה תיהיה jpg/jpeg
                        if self.combo_answers.get() == 'Yes': # האם המשתמש ביקש שלשאלה יהיה פתרון
                            if my_questions[i][1][10] == 'pdf':
                                self.questions_matches.append([my_questions[i][1][0], my_questions[i][1][1], 'Docx', 'Pdf'])
                            elif my_questions[i][1][10] == 'jpeg':
                                self.questions_matches.append([my_questions[i][1][0], my_questions[i][1][1], 'Docx', 'Jpeg'])
                            elif my_questions[i][1][10] == 'docx':
                                self.questions_matches.append([my_questions[i][1][0], my_questions[i][1][1], 'Docx', 'Docx'])
                        else:
                            self.questions_matches.append([my_questions[i][1][0], '', 'Docx', 'No'])

                    elif self.combo_format.get() == 'Jpeg':  # האם המשתמש ביקש שהשאלה תיהיה jpg/jpeg
                        if self.combo_answers.get() == 'Yes':  # האם המשתמש ביקש שלשאלה יהיה פתרון
                            if my_questions[i][1][10] == 'pdf':
                                self.questions_matches.append([my_questions[i][1][0], my_questions[i][1][1], 'Jpeg', 'Pdf'])
                            elif my_questions[i][1][10] == 'jpeg':
                                self.questions_matches.append([my_questions[i][1][0], my_questions[i][1][1], 'Jpeg', 'Jpeg'])
                            elif my_questions[i][1][10] == 'docx':
                                self.questions_matches.append([my_questions[i][1][0], my_questions[i][1][1], 'Jpeg', 'Docx'])
                        else:
                            self.questions_matches.append([my_questions[i][1][0], '', 'Jpeg', 'No'])

                    flag = True

            if flag == True:
                self.image_display()

            elif flag == False:
                self.error_message()

    def error_message(self):
        """
        this method is giving an alet if there is no match between the user's input and database.
        """
        error_window = Toplevel(self.student_Lecturer_top)
        Label(error_window, text='Cannot find a match').pack()

    def image_display(self):

        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        if self.questions_matches[0][2] == 'Jpeg':

            imgdata = base64.b64decode(self.questions_matches[0][0])
            filename = 'some_image.jpg'
            with open(filename, 'wb') as f:
                 f.write(imgdata)

            self.img_question = ImageTk.PhotoImage(Image.open(filename))

            self.my_label = tk.Label(self.student_Lecturer_top, image=self.img_question)
            self.my_label.image = self.img_question

            self.my_label.place(x=260, y=100)

            # creating another button to display the answer:
            if len(self.questions_matches) == 1:
                self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, state=DISABLED).place(x=488, y=50)
                self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, state=DISABLED).place(x=285, y=50)
                Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)

                if self.questions_matches[0][1] != '':
                    Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(0)).place(x=126, y=50)
                    Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)


                else:
                    Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(0)).place(x=126, y=50)
                    Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)



            elif len(self.questions_matches) > 1:
                # creating forward/backward button for image display:
                self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, command=lambda: self.forward(1)).place(x=488, y=50)
                self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, command=self.back, state=DISABLED).place(x=285, y=50)
                Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)


                if self.questions_matches[0][1] != '':
                    Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(0)).place(x=126, y=50)
                    Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)


                else:
                    Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(0)).place(x=126, y=50)
                    Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)


        elif self.questions_matches[0][2] == 'Pdf':
            self.my_label = tk.Label(self.student_Lecturer_top, bg='white', text=self.questions_matches[0][0])
            self.my_label.place(x=260, y=100)

            if len(self.questions_matches) == 1:
                self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, state=DISABLED).place(x=488, y=50)
                self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, state=DISABLED).place(x=285, y=50)
                Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)

                if self.questions_matches[0][1] != '':
                    Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(0)).place(x=126, y=50)
                    Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)


                else:
                    Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(0)).place(x=126, y=50)
                    Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)



            elif len(self.questions_matches) > 1:
                # creating forward/backward button for image display:
                self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, command=lambda: self.forward(1)).place(x=488, y=50)
                self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, command=self.back, state=DISABLED).place(x=285, y=50)
                Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)

                if self.questions_matches[0][1] != '':
                    Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(0)).place(x=126, y=50)
                    Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)


                else:
                    Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(0)).place(x=126, y=50)
                    Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)

        elif self.questions_matches[0][2] == 'Docx':
            self.my_label = tk.Label(self.student_Lecturer_top, bg='white', text=self.questions_matches[0][0])
            self.my_label.place(x=260, y=100)

            if len(self.questions_matches) == 1:
                self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, state=DISABLED).place(x=488, y=50)
                self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, state=DISABLED).place(x=285, y=50)
                Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)

                if self.questions_matches[0][1] != '':
                    Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(0)).place(x=126, y=50)
                    Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)


                else:
                    Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(0)).place(x=126, y=50)
                    Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)



            elif len(self.questions_matches) > 1:
                # creating forward/backward button for image display:
                self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, command=lambda: self.forward(1)).place(x=488, y=50)
                self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, command=self.back, state=DISABLED).place(x=285, y=50)
                Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)

                if self.questions_matches[0][1] != '':
                    Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(0)).place(x=126, y=50)
                    Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)


                else:
                    Button(self.student_Lecturer_top, text='Answer', command=lambda: self.display_answer(0)).place(x=126, y=50)
                    Button(self.student_Lecturer_top, text='delete', width=4, command=lambda: self.delete_question(0)).place(x=45, y=50)


    def create(self, key):
        """
        This method is navigating the system to open the right window via User's validation login/password:
        * if the user is a student - it should navigate him to the student's bar.
        * if the user is a Lecturer - it should navigate him to the Lecturer's bar.
        * if the user is a Coordinator - it should navigate him to the Coordinator's bar.
        """
        # creating a common TopLevel layer for all kind of users, but with different kind of classification the window
        # will present a different bar.
        self.new_root = Toplevel(self.root)

        # creating the navigation with the user's classification.
        # creating the navigation with the user's classification.
        if key == 'S' or key == 'L':
            # gui for Students and Lecturers - with disabled Lecturer button, because, if you press on lecturer button.
            # it should open the Lecturer management bar for the Coordinator
            Button(self.new_root, text='Questions', command=lambda: self.display(key)).grid(row=1, column=1, padx=10, pady=10)
            Button(self.new_root, text='Lecturers', state=DISABLED).grid(row=1, column=2, padx=10, pady=10)

        else:
            # it's the key =='C' case: which is open dor the Coordinator, he have access to question and Lecturer.
            Button(self.new_root, text='Questions', command=lambda: self.display(key)).grid(row=1, column=1, padx=10, pady=10)
            Button(self.new_root, text='Lecturers', command=self.management).grid(row=1, column=2, padx=10, pady=10)

    def management(self):
        self.management_top = Toplevel(self.new_root)
        self.management_top.geometry('250x230')
        Label(self.management_top, text='Choose one of the following options:', bg='white').place(x=30, y=2)
        Label(self.management_top, text='Operation:').place(x=2, y=35)
        self.combo_pick = Combobox(self.management_top, width=14)
        self.combo_pick['values'] = ['Add', 'Remove', 'Update']
        self.combo_pick.current(0)
        self.combo_pick.place(x=70, y=35)
        Button(self.management_top, width=7, text='...', command=lambda: self.pick_reflect(self.combo_pick.get())).place(x=185, y=30)

        self.combo_reflect = Combobox(self.management_top, width=14, state=DISABLED)
        self.combo_reflect['values'] = ['Add', 'Remove', 'Update']
        self.combo_reflect.current(0)
        self.combo_reflect.place(x=70, y=65)

    def pick_reflect(self, key):
        if key == 'Add':
            Label(self.management_top, text='on:').place(x=2, y=65)
            self.combo_reflect = Combobox(self.management_top, width=14)
            self.combo_reflect['values'] = ['Coordinator', 'Lecturer', 'Student']
            self.combo_reflect.current(0)
            self.combo_reflect.place(x=70, y=65)
            Button(self.management_top, width=7, text='...', command=self.pick_add).place(x=185, y=60)

        if key == 'Remove':
            Label(self.management_top, text='on:').place(x=2, y=65)
            self.combo_reflect = Combobox(self.management_top, width=14)
            self.combo_reflect['values'] = ['Coordinator', 'Lecturer', 'Student']
            self.combo_reflect.current(0)
            self.combo_reflect.place(x=70, y=65)
            Button(self.management_top, width=7, text='...', command=self.pick_remove).place(x=185, y=60)


        if key == 'Update':
            Label(self.management_top, text='on:').place(x=2, y=65)
            self.combo_reflect = Combobox(self.management_top, width=14)
            self.combo_reflect['values'] = ['Student', 'Lecturer', 'Coordinator']
            self.combo_reflect.current(0)
            self.combo_reflect.place(x=70, y=65)
            Button(self.management_top, width=7, text='...', command=self.pick_update).place(x=185, y=60)


    def pick_add(self):
        Label(self.management_top, text='Username:').place(x=3, y=95)
        self.entry_username= Entry(self.management_top, width=28)
        self.entry_username.place(x=70, y=95)
        Label(self.management_top, text='Password:').place(x=3, y=125)
        self.entry_pass = Entry(self.management_top, width=28)
        self.entry_pass.place(x=70, y=125)
        Button(self.management_top, width=12, text='Add', command=self.valid).place(x=85, y=165)


    def add(self, log, pas):
        if self.combo_reflect.get() == 'Student':
            users_data[log] = [pas, 'S']

        if self.combo_reflect.get() == 'Lecturer':
            users_data[log] = [pas, 'L']

        if self.combo_reflect.get() == 'Coordinator':
            users_data[log] = [pas, 'C']

        print(users_data)

        with open('users.txt', mode='r') as file:
            my_users = file.read()

            my_users = eval(my_users)

        my_users.update(users_data)


        with open('users.txt', mode='w') as file:
            file.write(repr([my_users]))


    def remove(self):

        with open('users.txt', mode='r') as file:
            my_users = file.read()
            my_users = dict(eval(my_users))


        if self.entry_username.get() in my_users.keys():
           my_users.pop(self.entry_username.get())

           with open('users.txt', mode='w') as file:
               file.write(repr(my_users))

        else:
            messagebox.showinfo("Error!", f"{self.entry_username.get()} doesn't exist in the system")
        print(users_data)

    def update(self, log, pas):

        with open('users.txt', mode='r') as file:
            my_users = file.read()
            my_users = dict(eval(my_users))

        my_users[log] = my_users.pop(self.combo_choose.get())
        my_users[log][0] = pas
        print(my_users)

        with open('users.txt', mode='w') as file:
            file.write(repr(my_users))


    def pick_remove(self):
        Label(self.management_top, text='Username:').place(x=3, y=95)
        self.entry_username = Entry(self.management_top, width=28)
        self.entry_username.place(x=70, y=95)
        Button(self.management_top, width=12, text='Remove', command=self.remove).place(x=85, y=135)

    def pick_update(self):
        self.loginList=[]
        with open('users.txt', mode='r') as file:
            my_users = file.read()
            my_users = dict(eval(my_users))

        Label(self.management_top, text='Account:').place(x=3, y=95)

        if self.combo_reflect.get() == 'Student':
            for i in my_users:
                if my_users[i][1] == 'S':
                    self.loginList.append(i)
        if self.combo_reflect.get() == 'Lecturer':
            for i in my_users:
                if my_users[i][1] == 'L':
                    self.loginList.append(i)
        if self.combo_reflect.get() == 'Coordinator':
            for i in my_users:
                if my_users[i][1] == 'C':
                    self.loginList.append(i)

        self.combo_choose = Combobox(self.management_top, values=sorted(self.loginList), width=14)
        self.combo_choose.current(0)
        self.combo_choose.place(x=70, y=95)

        Button(self.management_top, width=7, text='Update', command=self.blala).place(x=185, y=90)

    def valid(self):
        log = self.entry_username.get()
        pas = self.entry_pass.get()
        result = True
        flag_us = True
        flag_pas = True
        good = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'


        with open('users.txt', mode='r') as file:
            my_users = file.read()
            my_users = dict(eval(my_users))

        if log in my_users.keys():
            messagebox.showinfo("Error!", "Username already exists!")
            result = False


        for i in range(0, len(log)):
            if log[i] not in good:
                flag_us = False
                result = False

                break

        for i in range(0, len(pas)):
            if pas[i] not in good:
                flag_pas = False
                result = False
                break

        if flag_us == False:
                messagebox.showinfo("Error!", "Invalid username!")
        if flag_pas == False:
                messagebox.showinfo("Error!", "Invalid password!")

        if result == True:
            self.add(log, pas)

    def blala(self):
        Label(self.management_top, text='New username:').place(x=3, y=125)
        self.entry_new_username = Entry(self.management_top, width=22)
        self.entry_new_username.place(x=100, y=125)
        Label(self.management_top, text='New password:').place(x=3, y=155)
        self.entry_new_pass = Entry(self.management_top, width=22)
        self.entry_new_pass.place(x=100, y=155)
        Button(self.management_top, width=12, text='Apply', command=self.update_valid).place(x=75, y=185)

    def update_valid(self):
        result = True
        flag_us = True
        flag_pas = True
        good = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
        log = self.entry_new_username.get()
        pas = self.entry_new_pass.get()
        for i in range(0, len(log)):
            if log[i] not in good:
                flag_us = False
                result = False
                break
        for i in range(0, len(pas)):
            if pas[i] not in good:
                flag_pas = False
                result = False
                break

        if flag_us == False:
                messagebox.showinfo("Error!", "Invalid username!")

        if flag_pas == False:
                messagebox.showinfo("Error!", "Invalid password!")

        if result == True:
            with open('users.txt', mode='r') as file:
                my_users = file.read()
                my_users = dict(eval(my_users))

                if log in my_users.keys():
                    messagebox.showinfo("Error!", "Username already exists!")
                    return
                else:
                    self.update(self.entry_new_username.get(), self.entry_new_pass.get())


    def login_verify(self):
        """
        this method is in charge of compering the user name which is writen in the Entry to the key in the data base.
        if there is a match - the method will compere the password from the user to the password in the data base.
        if there is no match - the program will present an alert to the user, otherwise, it will open the appropriate
        page.
        """

        k = users_data.keys()  # verification of username in dictionary
        for names in k:
            if names == self.username_field.get():
                if users_data[names][0] != self.password_field.get():  # verification of password
                    messagebox.showinfo("Error", "Invalid Password!")
                else:
                    if users_data[names][1] == 'S':
                        self.create('S')
                        # open student
                    if users_data[names][1] == 'L':
                        self.create('L')
                        # open lecturer
                    if users_data[names][1] == 'C':
                        self.create('C')
                        # open coordinator


gui = GUI()
gui.root.mainloop()
