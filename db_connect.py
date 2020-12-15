import sqlalchemy as sa
from creation import creat
from functions import funcs


class Buttons:
    
    main_root = None
    con = None
    engine = None
    child = None
    child2 = None

    def __init__(self):

        self.main_root = _root


    def create_db(self):
        engine = sa.create_engine("postgresql://postgres:postgres@localhost:5432/postgres", echo=True)
        con = engine.connect()
        #con.execute(creat)
        con.execute("SELECT create_database()")

        self.engine = sa.create_engine("postgresql://postgres:postgres@localhost:5432/subway", echo=True)
        self.con = engine.connect()
        #self.con.execute(sa.text(funcs))


    def drop_db(self):
        self.con.execute("SELECT drop_database()")


    def clear_all_tables(self): 
        self.con.execute("SELECT clear_trains()")
        self.con.execute("SELECT clear_drivers()")
        self.con.execute("SELECT clear_lines()")


    def exit(self):
        self.main_root.quit()


    # def trains_table(self):

    # def drivers_table(self):
    
    # def sublines_table(self):

    #trains

    def show_all_trains(self):
        self.con.execute("SELECT show_trains()")


    def clear_trains_table(self):
        self.con.execute("SELECT clear_trains()")


    def add_new_train(self, _id, _title, _line, _driver):
        self.con.execute(f"SELECT add_train({_id}, '{_title}', {_line}, {_driver})")


    def delete_one_train(self, _title):
        self.con.execute(f"SELECT delete_trains_by_title('{_title}')")


    def find_trains_by_title(self, _title):
        self.con.execute(f"SELECT find_trains('{_title}')")


    def update_one_train(self, _oldtitle, _oldline, _title, _line, _driver, _age)
        self.con.execute(f"SELECT update_train('{_oldtitle}', '{_oldline}', '{_title}', '{_line}', '{_driver}', {_age})")


    #drivers

    def show_all_drivers(self):
        self.con.execute("SELECT show_drivers()")


    def clear_drivers_table(self):
        self.con.execute("SELECT clear_drivers()")


    def add_new_driver(self, _id, _name, _age, _exp):
        self.con.execute(f"SELECT add_driver({_id}, '{_name}', {_age}, {_exp})")


    def delete_one_driver(self, _sname, _age):
        self.con.execute(f"SELECT delete_driver('{_sname}', {_age})")


    def find_drivers_by_name(self, _sname):
        self.con.execute(f"SELECT find_drivers('{_sname}')")


    def update_one_driver(self, _oldname, _oldage, _sname, _age, _exp)
        self.con.execute(f"SELECT update_driver('{_oldname}', {_oldage}, '{_sname}', {_age}, {_exp})")


    #sublines

    def show_all_lines(self):
        self.con.execute("SELECT show_lines()")

    def clear_lines_table(self):
        self.con.execute("SELECT clear_lines()")


    def add_new_line(self, _id, _title, _trains):
        self.con.execute(f"SELECT add_line({_id}, '{_title}', {_trains})")


    def delete_one_line(self, _title):
        self.con.execute(f"SELECT delete_lines_by_title('{_title}')")


    def find_lines_by_title(self, _title):
        self.con.execute(f"SELECT find_lines('{_title}')")


    def update_one_line_title(self, _oldtitle, _title)
        self.con.execute(f"SELECT update_line_title('{_oldtitle}', '{_title}')")






if __name__ == '__main__':
    db = Buttons()
    db.create_db()
    db.add_new_line(1, "my", 0)
    #db.show_all_lines()
