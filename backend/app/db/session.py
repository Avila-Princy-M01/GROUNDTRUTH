from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 

#Our Docker DB address
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password@localhost:5432/groundtruth'

#the create_engine is the physical cable connecting app to the db
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#session factory creates temporary, safe convos with the db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

