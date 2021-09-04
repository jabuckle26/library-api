import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData


load_dotenv()
db_url = f"mysql+pymysql://{os.getenv('DBUSER')}@{os.getenv('DBHOSTNAME')}/{os.getenv('DBNAME')}"
engine = create_engine(db_url)
meta = MetaData()
meta.create_all(engine)
conn = engine.connect()
