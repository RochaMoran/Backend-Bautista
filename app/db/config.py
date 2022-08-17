from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgres://byokrxlvfnrfew:e066a110181fed06ec1635e5f10018d253f972381ce3456dd4c0690539dd8cda@ec2-3-234-131-8.compute-1.amazonaws.com:5432/d8p49d4qns46p4'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
