import os
from sqlalchemy import create_engine, MetaData


db_url = f"mysql+pymysql://{os.getenv('DBUSER')}@{os.getenv('DBHOSTNAME')}/{os.getenv('DBNAME')}"
engine = create_engine(db_url)
meta = MetaData()
conn = engine.connect()
