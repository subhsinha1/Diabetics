from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Check Diabetics")
window.geometry('700x700')

window.configure(background = "pink")
a = Label(window ,text = "Pregnancies",).grid(row = 0,column = 0)
b = Label(window ,text = "Glucose").grid(row = 1,column = 0)
c = Label(window ,text = "BloodPressure").grid(row = 2,column = 0)
d = Label(window ,text = "SkinThickness").grid(row = 3,column = 0)
e = Label(window ,text = "Insulin").grid(row = 4,column = 0)
f = Label(window ,text = "BMI").grid(row = 5,column = 0)
g = Label(window ,text = "DiabetesPedigreeFunction").grid(row = 6,column = 0)
h = Label(window ,text = "Age").grid(row = 7,column = 0)

a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1)
e1 = Entry(window).grid(row = 4,column = 1)
f1 = Entry(window).grid(row = 5,column = 1)
g1 = Entry(window).grid(row = 6,column = 1)
h1 = Entry(window).grid(row = 7,column = 1)
def clicked():
   res = "Welcome to " + txt.get()
   lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=8,column=0)
window.mainloop()