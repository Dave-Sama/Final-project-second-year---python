"""
 all the imported libraries/API for this project:
"""
import os
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from data_base import *
import tkinter as tk
import PyPDF2



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
        self.self_add.answerFile = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpeg"), ("PDF files", "*.PDF"),  ("jpg files", "*.jpg"), ("all files", "*.*")))

        # we need to check the answer's format:
        self.answer_file_format = self.self_add.answerFile.rpartition('.')[-1]

        # print(question_file_format)
        if self.answer_file_format == 'jpeg' or self.answer_file_format == 'jpg':
            # saving the image as reference to display it later if needed.
            self.img_answer = ImageTk.PhotoImage(Image.open(self.self_add.answerFile))

        else:
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
                self.pdf_answer = self.pdf_question + str(pageObj.extractText())

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

        # extracting the name of the file from it's path to display it in fill form
        answerFileName = self.self_add.answerFile.rpartition('/')[-1]
        # print(answerFileName)

        # creating the new text box with the name of the file in it:
        self.self_add.browseText = tk.Text(self.self_add, height=1, width=15)
        self.self_add.browseText.insert(INSERT, answerFileName)
        self.self_add.browseText.place(x=110, y=125)

        self.combo_answers = 'YES'

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
        self.self_add.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpeg"), ("PDF files", "*.PDF"), ("jpg files", "*.jpg"), ("all files", "*.*")))

        # we need to check the question's format:
        self.question_file_format = self.self_add.filename.rpartition('.')[-1]
        #print(question_file_format)

        if self.question_file_format == 'jpeg' or self.question_file_format == 'jpg':
            # opening the image for tkinter.
            self.img_question = ImageTk.PhotoImage(Image.open(self.self_add.filename))
            # self.question_display = Label(self.student_Lecturer_top, image=self.img_question)
            # self.questions_display = self.img_question
            # self.question_display.place(x=260, y=100)
        else:
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
                    if count < 10:
                        count += 1
                    else:
                        self.pdf_question = self.pdf_question[0: i] + "\n" + self.pdf_question[i:]
                        count = 0

            # print(pdf_question)

            # closing the pdf file object
            pdfFileObj.close()

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
        self.combo_sub_subject['values'] = ('not yet', 'not yet', 'not yet', 'not yet', "not yet")
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
        # creating a start self.key = 0, each time we add an element to the dictionary, we will implement i:
        self.key = 0

        # adding the question/question + answer, with all it's information:
        if self.question_file_format == 'jpeg' or self.question_file_format == 'jpg':
            questions[self.key] = [self.img_question, self.img_answer, self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(),  self.combo_semester.get(), self.combo_format.get()]
        else:
            questions[self.key] = [self.pdf_question, self.pdf_answer, self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get()]

        self.key += 1
        print(questions[0])

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
        print(self.combo_course.get())
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

        if key == 'L':
            # creating an Add button for the lecturer:
            Button(self.student_Lecturer_top, text='add', width=4, command=self.add_question).place(x=5, y=50)

            # creating a delete question for the lecturer:
            Button(self.student_Lecturer_top, text='delete', width=4).place(x=45, y=50)

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
        self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, command=lambda: self.forward(2)).place(x=488, y=50)
        self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, command=self.back, state=DISABLED).place(x=285, y=50)



    def display_answer(self, image_number):
        answer_display = Toplevel(self.student_Lecturer_top)
        self.my_label = Label(answer_display, image=self.questions_matches[image_number - 1][1])
        self.my_label.image = self.questions_matches[image_number - 1][1]
        self.my_label.pack()

    def forward(self, image_number):
        """
        this method is handling the logic behind the forward button
        """
        self.my_label.place_forget()
        self.my_label = Label(self.student_Lecturer_top, image=self.questions_matches[image_number - 1][0])
        self.my_label.image = self.questions_matches[image_number - 1][0]


        if image_number < len(self.questions_matches):
            self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, command=lambda: self.forward(image_number + 1)).place(x=488, y=50)
            self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, command=lambda: self.back(image_number - 1)).place(x=285, y=50)

        else:
            self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, state=DISABLED).place(x=488, y=50)

        self.my_label.place(x=260, y=100)

    def back(self, image_number):
        """
        this method handling the logic behind the back button
        """
        self.my_label.place_forget()
        self.my_label = Label(self.student_Lecturer_top, image=self.questions_matches[image_number - 1])
        self.my_label.image = self.questions_matches[image_number - 1]

        self.button_forward = Button(self.student_Lecturer_top, text='>>', width=5, command=lambda: self.forward(image_number + 1)).place(x=488, y=50)
        self.button_back = Button(self.student_Lecturer_top, text='<<', width=5, command=lambda: self.back(image_number - 1)).place(x=285, y=50)

        if image_number == 1:
            self.button_forward = Button(self.student_Lecturer_top, text='<<', width=5, state=DISABLED).place(x=285, y=50)

        self.my_label.place(x=260, y=100)

    def question_match(self):
        """
        this method can find a match from the search bar, and return the matches to the bar
        """

        # temp1 for the data base , temp2 for the users input
        self.questions_matches = []
        temp1 = []
        flag = False
        i = 0

        # copying the values for each key from the data base:
        for k in questions:
            temp1.append(questions[k])

            # we need to convert the year to a string to compare it later
            temp1[i][4] = str(temp1[i][4])

        # putting all the user inputs into temp2
        temp2 = [self.combo_course.get(), self.combo_sub_subject.get(), self.combo_difficulty.get(), self.spin_years.get(), self.combo_answers, self.combo_from.get(), self.combo_semester.get(), self.combo_format.get()]

        print(f"from combo: {temp2}")
        print(f"from data base: {temp1[2:]}")

        # checking if there is a match between temp1, and temp2
        for i in range(0, len(temp1)):
            if temp1[i][2:] == temp2:
                if self.combo_format.get() == 'PDF':
                    if self.combo_answers == 'YES':
                        self.questions_matches.append([self.pdf_question, self.pdf_answer])
                    else:
                        self.questions_matches.append([self.pdf_question, 'no answer'])
                else:
                    if self.combo_answers == 'YES':
                        self.questions_matches.append([self.img_question, self.img_answer])
                    else:
                        self.questions_matches.append([self.img_question, 'no answer'])
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
        # path = "banana.jpeg"
        # img = ImageTk.PhotoImage(Image.open(path))
        # path1 = "leopard.jpeg"
        # img1 = ImageTk.PhotoImage(Image.open(path1))
        #
        # path2 = "panda.jpeg"
        # img2 = ImageTk.PhotoImage(Image.open(path2))
        #
        # path3 = "pug.jpeg"
        # img3 = ImageTk.PhotoImage(Image.open(path3))
        #
        # self.questions_matches.append(img)
        # self.questions_matches.append(img1)
        # self.questions_matches.append(img2)
        # self.questions_matches.append(img3)

        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        self.my_label = tk.Label(self.student_Lecturer_top, image=self.questions_matches[0][0])
        self.my_label.image = self.questions_matches[0][0]
        # The Pack geometry manager packs widgets in rows or columns.
        self.my_label.place(x=260, y=100)

        # creating another button to display the answer:
        if self.questions_matches[0][1] != 'no answer':
            Button(text='Answer', command=lambda: self.display_answer(image_number - 1)).place(x=500, y=50)

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
            Button(self.new_root, text='Questions').grid(row=1, column=1, padx=10, pady=10)
            Button(self.new_root, text='Lecturers').grid(row=1, column=2, padx=10, pady=10)

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
