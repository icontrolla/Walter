from tkinter import *
from PIL import ImageTk

SignUpPage = Tk()
SignUpPage.geometry("939x521")
SignUpPage.title("SIGNUPPAGE")
SignUpPage.configure(bg="white")

def on_enter():
    if username.get() == "username":
        username.delete(0, END)




bgImage = ImageTk.PhotoImage(file='login_bg.png')
bgLabel=Label(SignUpPage, image=bgImage)
bgLabel.place(x=0, y=0)

heading=Label(SignUpPage, text='USER SIGN UP', font=("organo", 20,), bg="#FBFEFF", fg='#3085AB')
heading.place(x=620, y=70)


username = Entry(SignUpPage, borderwidth=0, font=("arial", 15,), bg="#FBFEFF", fg='black')
username.place(x=610, y=140)
username.insert(0, f"Insert Name")
username.configure(state=DISABLED)


Name = Entry(SignUpPage, borderwidth=0, font=("arial", 15,), bg="#FBFEFF", fg='black')
Name.place(x=610, y=200)
Name.insert(0, f"Insert Username")
Name.configure(state=DISABLED)

Depatment = Entry(SignUpPage, borderwidth=0, font=("arial", 15,), bg="#FBFEFF", fg='black')
Depatment.place(x=610, y=260)
Depatment.insert(0, f"Department")
Depatment.configure(state=DISABLED)

NumPlates = Entry(SignUpPage,border=4, borderwidth=0, font=("arial", 15,), bg="#FBFEFF", fg='black')
NumPlates.place(x=610, y=320)
NumPlates.insert(0, f"Account type")
NumPlates.configure(state=DISABLED)

password1 = Entry(SignUpPage,border=4, borderwidth=0, font=("arial", 15,), bg="#FBFEFF", fg='black')
password1.place(x=610, y=380)
password1.insert(0, f"Insert Password")
password1.configure(state=DISABLED)

password2 = Entry(SignUpPage,border=4, borderwidth=0, font=("arial", 15,), bg="#FBFEFF", fg='black')
password2.place(x=610, y=430)
password2.insert(0, f"Confirm Password")
password2.configure(state=DISABLED)


def on_click(event):
    username.configure(state=NORMAL)
    username.delete(0, END)


username.bind("<Button-1>", on_click)

Frame(SignUpPage, width=230, height=2, bg='#3085AB').place(x=610, y=170)
Frame(SignUpPage, width=230,height=2, bg='#3085AB').place(x=610, y=230)
Frame(SignUpPage, width=230,height=2, bg='#3085AB').place(x=610, y=290)
Frame(SignUpPage, width=230,height=2, bg='#3085AB').place(x=610, y=350)
Frame(SignUpPage, width=230,height=2, bg='#3085AB').place(x=610, y=410)
Frame(SignUpPage, width=230,height=2, bg='#3085AB').place(x=610, y=455)





def on_click(event):
    password1.configure(state=NORMAL)
    password1.delete(0, END)


password1.bind("<Button-1>", on_click)

def on_click(event):
    password2.configure(state=NORMAL)
    password2.delete(0, END)


password2.bind("<Button-1>", on_click)

def on_click(event):
    Name.configure(state=NORMAL)
    Name.delete(0, END)


Name.bind("<Button-1>", on_click)

def on_click(event):
    Depatment.configure(state=NORMAL)
    Depatment.delete(0, END)

Depatment.bind("<Button-1>", on_click)


def on_click(event):
    NumPlates.configure(state=NORMAL)
    NumPlates.delete(0, END)

()
NumPlates.bind("<Button-1>", on_click)


button=Button(SignUpPage,text="Sign Up", font=("game of squids",14), bg="#669AB8",bd=0)
button.place(x=660, y=460)

SignUpPage.mainloop()
