from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Certificate(Base):
    __tablename__ = 'certificates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column("certificate_name", String, nullable=False)
    course = Column(String, nullable=False)
    date_issued = Column(Date, nullable=False)
    pdf_path = Column(String, nullable=False)


DATABASE_URL = "mysql+pymysql://user:password@db/certs_db"  
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
