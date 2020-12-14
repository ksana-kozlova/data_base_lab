from tkinter import *
from tkinter import messagebox as mb
import sqlalchemy as sa
import creation
from functions import funcs

password = "123"

'''def btn1_com():
    engine = sa.create_engine("postgresql://postgres:123@localhost:5432/trains", echo=True)
    con = engine.connect()
    con.execute(creation.creat)
    con.execute("SELECT public.create_database()")

    engine = sa.create_engine("postgresql://postgres:123@localhost:5432/lab", echo=True)
    con = engine.connect()
    con.execute(sa.text(funcs))'''

def btn2_com():
    btn_root = Toplevel(root)
    btn_root.title('Clearing table')
    

def btn3_com():
    print("3")

def btn4_com():
    print("3")

def btn5_com():
    print("3")

def btn6_com():
    print("3")

def btn7_com():
    print("3")

def btn8_com():
    print("3")

def btn9_com():
    print("3")

def btn10_com():
    print("3")

def btn11_com():
    print("3")

def btn12_com():
    root.quit()

root = Tk()
root.title("Sign in")
root.geometry("500x500")

lbl = Label(root, text="Database Trains")
lbl.config(font=("Arial Bold", 22))
lbl.place(x=150, y=10)


#======BUTTONS======
btn_names = ["Create DB", "Drop DB", "Clear Table", "Clear all Tables", "Add new Train", "Add new Driver", "Add new SubLine", 
            "Search in Table", "Update Data", "Delete Data", "Delete particular row", "Exit"]

x_cur = 50
y_cur = 120
for i in range(1, 13):
    btn_com = "btn" + str(i) + "_com"
    btn = Button(root, text=btn_names[i-1], command=locals().get(btn_com), width=15)
    btn.config(bg='blue', fg='white', activebackground='yellow', activeforeground='green')
    btn.place(x=x_cur, y=y_cur)
    if i % 3 == 0:
        y_cur += 95
        x_cur -= 300
    else:
        x_cur += 150


#entry = Entry(root, width=12)
#entry.grid(column=0, row=1)


root.mainloop()
