from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class BankAccount(Base):
    __tablename__ = "bank_account"
    id: int = Column(Integer, primary_key=True, index=True)
    Name: str = Column(String, index=True)
    account_id: str = Column(Integer, nullable=False)
    pin: int = Column(Integer, nullable=False)
    phone: int = Column(Integer, nullable=False)
    balance: int = Column(Integer, nullable=False)
    