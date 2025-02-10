from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define a test model
class TestModel(Base):
    __tablename__ = "test_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # String should support Unicode

# Connect to database
engine = create_engine("sqlite:///test.db", echo=True)  # Ensure debug mode (echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Insert Bangla text
bangla_text = "বাংলা নাম"  # Unicode Bangla text
new_entry = TestModel(name=bangla_text)
session.add(new_entry)
session.commit()

# Fetch and print
retrieved = session.query(TestModel).first()
print("Stored Name:", retrieved.name)  # Expected Output: বাংলা নাম
