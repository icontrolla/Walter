from tkinter import *
from tkinter import ttk
from tkinter import messagebox


win = Tk()
win.geometry("939x521")
win.title("LOGIN PAGE")
win.configure(bg="white")



def login():
    username = usernames.get()
    password = passwords.get()


    if username == "Admin" and password == "Password":
        messagebox.showinfo("Automen Mechanics Service", "Login successful")
        win.destroy()
        import sample

    else:
        messagebox.askretrycancel("Automen Mechanics Service", "Login Unsuccessful. Please Click Retry")






bgImage = PhotoImage(file='login_bg.png')
bgLabel=Label(win, image=bgImage)
bgLabel.place(x=0, y=0)

heading=Label(win, text='USER LOGIN', font=("organo", 20,), bg="#FBFEFF", fg='#3085AB')
heading.place(x=630, y=80)


usernames = Entry(win, borderwidth=0, font=("arial", 15,), bg="#FBFEFF", fg='black')
usernames.place(x=610, y=140)
usernames.insert(0, f"  Username")
usernames.configure(state=DISABLED)
usernames.place(x=610, y=140)


passwords = Entry(win,border=4, borderwidth=0, font=("arial", 15), bg="#FBFEFF", fg='black')
passwords.insert(0, f"  Password")
passwords.configure(state=DISABLED)
passwords.place(x=610, y=200)



Frame(win, width=230, height=2, bg='#3085AB').place(x=610, y=170)
Frame(win, width=230, height=2, bg='#3085AB').place(x=610, y=230)


def on_click(event):
    usernames.configure(state=NORMAL)
    usernames.delete(0, END)


usernames.bind("<Button-1>", on_click)


def on_click(event):
    passwords.configure(state=NORMAL)
    passwords.delete(0, END)


passwords.bind("<Button-1>", on_click)


button = Button(win, borderwidth=0, text="login",font=("organo",14),width=19, bg="#0092D1",fg="white",
                command=lambda: login())
button.place(x=595, y=290)




forgotPassword=Button(win, text="forgot password?", bg="white", bd=0, fg="#89D0F7",
                      font=("comic sans ui", 11), activebackground="white")
forgotPassword.place(x=710, y=240)

orLabel=Label(win, text="-----------OR-------------", bg="white",font=("organo",16))
orLabel.place(x=640, y=340)

button=Button(win,text="Sign Up", font=("game of squids", 11),
              bd=0,bg="#89D0F7", width=10)
button.place(x=710, y=380)

win.mainloop()
