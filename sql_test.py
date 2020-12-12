import sqlalchemy as sa
import pandas as pd

engine = sa.create_engine("postgresql://postgres:123@localhost:5432/trains", echo=True)
con = engine.connect()
con.execute("SELECT public.create_database()")

engine = sa.create_engine("postgresql://postgres:123@localhost:5432/lab", echo=True)