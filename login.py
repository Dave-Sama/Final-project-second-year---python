
# all the imported libraries/API for this project
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from data_base import *

class GUI(object):
    def __init__(self):
        # setting the root
        root = self.root = Tk()
        root.title('Test')
        root.geometry('310x85')

    # make the top right close button minimize (iconify) the main window
        root.protocol("WM_DELETE_WINDOW", root.iconify)

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

    def display(self, key):

        self.student_top = Toplevel(self.root)
        if key == 'S':
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
                    """
            # creating the defining the new layer.
            self.student_top.geometry('825x400')

            # creating a Label for courses:
            Label(self.student_top, text='Course: ').grid(row=0, column=0)

            # creating combobox for the courses:
            combo_course = Combobox(self.student_top)
            combo_course['values'] = ('Calculus1', 'Linear algebra', 'Pre computer science', 'Architecture', "Logic 1")
            combo_course.current(0)  # set the selected item
            combo_course.grid(row=0, column=1, sticky='W')

            # creating a Label for courses:
            Label(self.student_top, text='   Sub subject: ').grid(row=0, column=3)

            # creating combobox for the sub-subjects:
            combo_sub_subject = Combobox(self.student_top)
            combo_sub_subject['values'] = ('not yet', 'not yet', 'not yet', 'not yet', "not yet")
            combo_sub_subject.current(0)  # set the selected item
            combo_sub_subject.grid(row=0, column=4)

            # creating a Label for Difficulty:
            Label(self.student_top, text='  Difficulty: ').grid(row=0, column=6)

            # creating combobox for the difficulty:
            combo_difficulty = Combobox(self.student_top)
            combo_difficulty['values'] = ('Easy', 'Moderate', 'Hard')
            combo_difficulty.current(0)  # set the selected item
            combo_difficulty.grid(row=0, column=7, sticky='W')

            # creating a Label for Answers:
            Label(self.student_top, text='  Answers: ').grid(row=0, column=9)

            # creating combobox for the Answers:
            combo_answers = Combobox(self.student_top)
            combo_answers['values'] = ('Yes', 'No')
            combo_answers.current(0)  # set the selected item
            combo_answers.grid(row=0, column=10, sticky='W')

            # creating a Label for Years:
            Label(self.student_top, text='Year:').grid(row=1, column=0)

            # creating spinbox for the Years:
            var = IntVar()
            var.set(2019)
            spin_years = Spinbox(self.student_top, from_=1995, to=2020, width=6, textvariable=var)
            spin_years.place(x=47, y=22, width=143)

            # creating Label for the semester:
            Label(self.student_top, text='Semester:').place(x=199, y=22)

            # creating a combobox for the Semester:
            combo_semester = Combobox(self.student_top)
            combo_semester['values'] = ('A', 'B', 'Summer')
            combo_semester.current(0)  # set the selected item
            combo_semester.place(x=270, y=22)

            # creating a Label for Format:
            Label(self.student_top, text='Format:').place(x=419, y=22)

            # creating a combobox for Format:
            combo_format = Combobox(self.student_top)
            combo_format['values'] = ('docx', 'pdf', 'jpeg')
            combo_format.current(0)  # set the selected item
            combo_format.place(x=477, y=22)

            # crating an Accept button:
            Button(self.student_top, text='Accept', command=self.login_verify, width = 20).place(x=679, y=22)

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
        k = users_data.keys() # verification of username in dictionary
        for names in k:
            if names == self.username_field.get():
                if users_data[names][0] != self.password_field.get(): # verification of password
                    messagebox.showinfo("Error", "Invalid Password!")
                else:
                    if users_data[names][1] == 'S':
                        self.create('S')
                        #open student
                    if users_data[names][1] == 'L':
                        self.create('L')
                        #open lecturer
                    if users_data[names][1] == 'C':
                        self.create('C')
                        #open coordinator






gui = GUI()
gui.root.mainloop()



