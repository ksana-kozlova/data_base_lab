import sqlalchemy as sa
from creation import creat
from functions import funcs
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import pandas as pd


class Buttons:
    
    main_root = None
    con = None
    engine = None
    child = None
    child2 = None
    btn_names_main = ["Create DB", "Drop DB", "Clear all tables", "Trains", "Drivers", "Lines"]
    btn_names = ["Show table", "Clear Table", "Add row", "Delete Table", "Search", "Update"]
    def __init__(self, _root):

        self.main_root = _root
        self.main_root.title("Sign in")
        self.main_root.geometry("500x250")
        lbl = Label(root, text="Database Trains")
        lbl.config(font=("Arial Bold", 22))
        lbl.place(x=150, y=10)
        btn_create = Button(_root, text="Create DB", width=15, bg='blue', fg='white', activebackground='yellow', activeforeground='green',
                            command=self.create_db)
        btn_create.place(x=50, y=120)
        btn_drop = Button(_root, text="Drop DB", width=15, bg='blue', fg='white', activebackground='yellow', activeforeground='green',
                            command=self.drop_db)
        btn_drop.place(x=200, y=120)
        btn_clear = Button(_root, text="Clear tables", width=15, bg='blue', fg='white', activebackground='yellow', activeforeground='green',
                            command=self.clear_all_tables)
        btn_clear.place(x=350, y=120)
        btn_trains = Button(_root, text="Trains", width=15, bg='blue', fg='white', activebackground='yellow', activeforeground='green',
                            command=self.trains_table)
        btn_trains.place(x=50, y=215)
        btn_drivers = Button(_root, text="Drivers", width=15, bg='blue', fg='white', activebackground='yellow', activeforeground='green',
                            command=self.drivers_table)
        btn_drivers.place(x=200, y=215)
        '''btn_lines = Button(_root, text="Lines", width=15, bg='blue', fg='white', activebackground='yellow', activeforeground='green',
                            command=self.sublines_table)
        btn_lines.place(x=350, y=215)'''
        self.main_root.mainloop()

    def create_db(self):
        self.engine = sa.create_engine("postgresql://postgres:123@localhost:5432/postgres", echo=True)
        self.con = self.engine.connect()
        self.con.execute(creat)
        self.con.execute("SELECT create_database()")

        self.engine = sa.create_engine("postgresql://postgres:123@localhost:5432/subway", echo=True)
        self.con = self.engine.connect()
        self.con.execute(sa.text(funcs))
        mb.showinfo(title="Significant", message="Databse created successfully!")


    def drop_db(self):
        self.engine = sa.create_engine("postgresql://postgres:123@localhost:5432/postgres", echo=True)
        self.con = self.engine.connect()
        self.con.execute("SELECT drop_database()")


    def clear_all_tables(self): 
        self.con.execute("SELECT clear_trains()")
        self.con.execute("SELECT clear_drivers()")
        self.con.execute("SELECT clear_lines()")


    def exit(self):
        self.main_root.quit()

    def make_buttons(self, label, len):
        lbl = Label(self.child, text=label)
        lbl.config(font=("Arial Bold", 22))
        lbl.place(x=150, y=10)
        btns = list()
        x_cur = 50
        y_cur = 120
        for i in range(1, len+1):
            btn = Button(self.child, text=self.btn_names[i-1], width=15)
            btn.config(bg='blue', fg='white', activebackground='yellow', activeforeground='green')
            btn.place(x=x_cur, y=y_cur)
            btns.append(btn)
            if i % 3 == 0:
                y_cur += 95
                x_cur -= 300
            else:
                x_cur += 150
        return btns
        
    def trains_table(self):
        self.child = Toplevel(self.main_root)
        self.child.title('Table Trains Controller')
        self.child.geometry("500x250")
        
        btns = self.make_buttons("Table Trains", 5)
        btns[0].config(command=self.show_all_trains)
        btns[1].config(command=self.clear_trains_table)
        btns[2].config(command=self.add_new_train)
        #btns[3].config(command=)
        #btns[4].config(command=)
        
        
    
    def drivers_table(self):
        self.child = Toplevel(self.main_root)
        self.child.title('Table Trains Controller')
        self.child.geometry("500x250")
        
        btns = self.make_buttons("Table Drivers", 6)
        btns[0].config(command=self.show_all_trains)
        btns[1].config(command=self.clear_trains_table)
        btns[2].config(command=self.add_new_train)
        #btns[3].config(command=)
        #btns[4].config(command=)
    
    # def sublines_table(self):

    #trains

   #def show_all_trains(self):
   #     self.child2 = Toplevel(self.main_root)
   #     self.child2.title("Table Trains")
   #     res = pd.DataFrame(self.con.execute("SELECT * from show_trains()"))
   #     print(res)

    def show_all_trains(self):
        self.child2 = Toplevel(self.main_root)
        self.child2.title("lksdjfsoje")
        columns = ('train_id', 'title', 'line_id', 'driver_id')
        headings = ('train_id', 'title', 'line_id', 'driver_id')
        self.tree = ttk.Treeview(self.child2, column=columns, height=18, show='headings')
        widths = [100, 100, 100, 100]
        for i in range(len(columns)):
            self.tree.column(columns[i], width=widths[i], anchor=CENTER)
            self.tree.heading(columns[i], text=headings[i])
        res = pd.DataFrame(self.con.execute("SELECT * from show_trains()"))
        [self.tree.insert('', 'end', values=row) for ind, row in res.iterrows()]

    def clear_trains_table(self):
        self.con.execute("SELECT clear_trains()")
        mb.showinfo(title="Significant", message="Table trains cleared successfully!")

    def btn_add_train(self, _id, _title, _line, _driver):
        self.con.execute(f"SELECT add_train({_id}, '{_title}', {_line}, {_driver})")
        
    def add_new_train(self):
        self.child2 = Toplevel(self.child)
        self.child2.title("Add new Train")
        self.child2.geometry("250x250")
        
        lbl_id = Label(self.child2, text="ID: ")
        lbl_id.grid(row=0, column=0)
        lbl_title = Label(self.child2, text="Title: ")
        lbl_title.grid(row=1, column=0)
        lbl_line = Label(self.child2, text="Line: ")
        lbl_line.grid(row=2, column=0)
        lbl_driver = Label(self.child2, text="Driver: ")
        lbl_driver.grid(row=3, column=0)

        entry_id = Entry(self.child2, width=15)
        entry_id.grid(row=0, column=1)
        entry_title = Entry(self.child2, width=15)
        entry_title.grid(row=1, column=1)
        entry_line = Entry(self.child2, width=15)
        entry_line.grid(row=2, column=1)
        entry_driver = Entry(self.child2, width=15)
        entry_driver.grid(row=3, column=1)
        
        btn = Button(self.child2, text="Add row",
                    command=lambda: self.btn_add_train(entry_id.get(), entry_title.get(), entry_line.get(), entry_driver.get()))
        btn.config(bg='blue', fg='white', activebackground='yellow', activeforeground='green')
        btn.grid(row=4, column=1)

    def btn_delete_train(self, _title):
        self.con.execute(f"SELECT delete_trains_by_title('{_title}')")

    def delete_one_train(self, _title):
        self.child2 = Toplevel(self.child)
        self.child2.title("Delete Train")
        self.child2.geometry("250x250")
        lbl = Label(self.child2, text="Deletion")
        lbl.grid(row=0)

        lbl_title = Label(self.child2, text="Title: ")
        lbl_title.grid(row=1, column=0)

        entry_title = Entry(self.child2, width=15)
        entry_title.grid(row=1, column=1)

        btn = Button(self.child2, text="Delete row",
                    command=lambda: self.btn_delete_train(entry_title.get()))
        btn.config(bg='blue', fg='white', activebackground='yellow', activeforeground='green')
        btn.grid(row=2, column=1)
        

    def find_trains_by_title(self, _title):
        self.con.execute(f"SELECT find_trains('{_title}')")


    '''#don't touch pls
    def update_one_train(self, _oldtitle, _oldline, _title, _line, _driver, _age)
        self.con.execute(f"SELECT update_train('{_oldtitle}', '{_oldline}', '{_title}', '{_line}', '{_driver}', {_age})")
    '''

    #drivers

    def show_all_drivers(self):
        self.con.execute("SELECT * from show_drivers()")


    def clear_drivers_table(self):
        self.con.execute("SELECT clear_drivers()")
        mb.showinfo(title="Significant", message="Table Drivers cleared successfully!")
 
    def btn_add_driver(self, _id, _name, _age, _exp):
        self.con.execute(f"SELECT add_driver({_id}, '{_name}', {_age}, {_exp})")

    def add_new_driver(self, _id, _name, _age, _exp):
        self.child2 = Toplevel(self.child)
        self.child2.title("Add new Driver")
        self.child2.geometry("250x250")
        
        lbl_id = Label(self.child2, text="ID: ")
        lbl_id.grid(row=0, column=0)
        lbl_name = Label(self.child2, text="Surname: ")
        lbl_name.grid(row=1, column=0)
        lbl_age = Label(self.child2, text="Age: ")
        lbl_age.grid(row=2, column=0)
        lbl_exp = Label(self.child2, text="Experience: ")
        lbl_exp.grid(row=3, column=0)

        entry_id = Entry(self.child2, width=15)
        entry_id.grid(row=0, column=1)
        entry_name = Entry(self.child2, width=15)
        entry_name.grid(row=1, column=1)
        entry_age = Entry(self.child2, width=15)
        entry_age.grid(row=2, column=1)
        entry_exp = Entry(self.child2, width=15)
        entry_exp.grid(row=3, column=1)
        
        btn = Button(self.child2, text="Add row",
                    command=lambda: self.btn_add_driver(entry_id.get(), entry_name.get(), entry_age.get(), entry_exp.get()))
        btn.config(bg='blue', fg='white', activebackground='yellow', activeforeground='green')
        btn.grid(row=4, column=1)

    def btn_delete_driver(self, _sname, _age):
        self.con.execute(f"SELECT delete_driver('{_sname}', {_age})")

    def delete_one_driver(self, _sname, _age):
        self.child2 = Toplevel(self.child)
        self.child2.title("Delete Driver")
        self.child2.geometry("250x250")
        lbl = Label(self.child2, text="Deletion")
        lbl.grid(row=0)

        lbl_name = Label(self.child2, text="Surname: ")
        lbl_name.grid(row=1, column=0)
        lbl_age = Label(self.child2, text="Age: ")
        lbl_age.grid(row=2, column=0)

        entry_title = Entry(self.child2, width=15)
        entry_title.grid(row=1, column=1)
        entry_age = Entry(self.child2, width=15)
        entry_age.grid(row=2, column=1)

        btn = Button(self.child2, text="Delete row",
                    command=lambda: self.btn_delete_driver(entry_name.get(), entry_age.get()))
        btn.config(bg='blue', fg='white', activebackground='yellow', activeforeground='green')
        btn.grid(row=3, column=1)


    def find_drivers_by_name(self, _sname):
        self.con.execute(f"SELECT find_drivers('{_sname}')")


    def update_one_driver(self, _oldname, _oldage, _sname, _age, _exp):
        self.con.execute(f"SELECT update_driver('{_oldname}', {_oldage}, '{_sname}', {_age}, {_exp})")


    #sublines

    def show_all_lines(self):
        self.con.execute("SELECT * from show_lines()")

    def clear_lines_table(self):
        self.con.execute("SELECT clear_lines()")


    def add_new_line(self, _id, _title, _trains):
        self.con.execute(f"SELECT add_line({_id}, '{_title}', {_trains})")


    def delete_one_line(self, _title):
        self.con.execute(f"SELECT delete_lines_by_title('{_title}')")


    def find_lines_by_title(self, _title):
        self.con.execute(f"SELECT find_lines('{_title}')")


    def update_one_line_title(self, _oldtitle, _title):
        self.con.execute(f"SELECT update_line_title('{_oldtitle}', '{_title}')")






if __name__ == '__main__':
    root = Tk()
    db = Buttons(root)
    #db.create_db()
    #db.add_new_line(1, "my", 0)
    #db.show_all_lines()
