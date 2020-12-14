import sqlalchemy as sa
import creation
from functions import funcs

#print(sa.text(funcs))

engine = sa.create_engine("postgresql://postgres:123@localhost:5432/trains", echo=True)
con = engine.connect()
con.execute(creation.creat)
con.execute("SELECT public.create_database()")

engine = sa.create_engine("postgresql://postgres:123@localhost:5432/lab", echo=True)
con = engine.connect()
con.execute(sa.text(funcs))
