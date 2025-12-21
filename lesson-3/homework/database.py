import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, Float, create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)

def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    session = SessionLocal()

    p1 = Product(name="iPhone 15", price=1200.0, stock=10)
    p2 = Product(name="MacBook Air M3", price=1500.0, stock=5)
    p3 = Product(name="Airpods Pro", price=250.0, stock=20)
    
    session.add_all([p1, p2, p3])
    session.commit()
    session.close()
    print("Database created and data added")

if __name__ == "__main__":
    init_db()
