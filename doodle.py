from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
# # root.withdraw()
# # file_path = filedialog.askopenfilename()
# # print(file_path)
# #
# # my_img = Image.open("C:\Users\david\OneDrive\שולחן העבודה\Nature.jpg")
# #
# #
# #

root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)
img3 = ImageTk.PhotoImage(Image.open(root.filename))
Label(root, image=img3).grid(row=0, column=0)
root.mainloop()
