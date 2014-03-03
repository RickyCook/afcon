from afcon.settings import DB_CONNECTION
from sqlalchemy import create_engine

engine = create_engine(DB_CONNECTION)