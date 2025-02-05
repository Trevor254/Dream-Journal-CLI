from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# setting up models

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    dreams = relationship("Dream", back_populates="category", cascade="all, delete")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"

class Dream(Base):
    __tablename__ = "dreams"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="dreams")

    def __repr__(self):
        return f"<Dream(id={self.id}, title='{self.title}', date={self.date})>"

# Database setup
DATABASE_URL = "sqlite:///dream_journal.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def initialize_db():
    Base.metadata.create_all(engine)