from app.models import BankAccount
from app.database import SessionLocal,engine,Base
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
load_dotenv()
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

class AccountCreate(BaseModel):
    Name: str  
    phone: int


BankAccount.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# db: Session = Depends(get_db)


app=FastAPI(title="Welcome to Harshad Mehta Banks",
    description="API for banking operations",
    version="1.0.0")

@app.get("/")
def read_root():
    # print("Welcome to Harshad Mehta Banks")
    return {"message": "Welcome to Harshad Mehta Banks"}

@app.post("/create_account/")
def create_account(bank:AccountCreate, db: Session = Depends(get_db)):
    import random

    # Generate a 15-digit account number
    account_id = random.randint(1, 9)
    for _ in range(14):
        account_id = account_id * 10 + random.randint(0, 9)

    # Generate a 4-digit PIN
    pin = random.randint(1, 9)
    for _ in range(3):
        pin = pin * 10 + random.randint(0, 9)

    new_account = BankAccount(
        Name=bank.Name,
        account_id=account_id,
        pin=pin,
        phone=bank.phone,
        balance=0)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    
    return {
        "message": "Account created successfully.Thank you for choosing Harshad Mehta Banks. Please keep your Account Number and PIN safe.",
        "account_details": {
            "Name": bank.Name,
            "Phone Number": bank.phone,
            "Account Number": account_id,
            "PIN": pin
        }
    }
    
@app.post("/deposit_money/")
def money_deposit(balance:int,pin:int,db: Session = Depends(get_db)):
    account = db.query(BankAccount).filter(BankAccount.pin == pin).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found Create a Bank Account.")
    
    account.balance += balance
    db.commit()
    db.refresh(account)
    
    return {"message": f"₹{balance} has been successfully deposited.", "new_balance": account.balance}


@app.post("/withdraw_money/")
def money_withdraw(amount:int,pin:int,db: Session = Depends(get_db)):
    account = db.query(BankAccount).filter(BankAccount.pin == pin).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found Create a Bank Account.")
    
    if amount > account.balance:
        raise HTTPException(status_code=400, detail="Insufficient funds.")
    
    account.balance -= amount
    db.commit()
    db.refresh(account)
    
    return {"message": f"₹{amount} has been successfully withdrawn.", "new_balance": account.balance}


@app.put("/change_pin/")
def change_pin(account_id: int, phone: int, new_pin: int, db: Session = Depends(get_db)):
    account = db.query(BankAccount).filter(BankAccount.account_id == account_id and BankAccount.phone == phone).first()
    # account = db.query(BankAccount).filter(BankAccount.phone == phone).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found Create a Bank Account.")

    account.pin = new_pin
    db.commit()
    db.refresh(account)
    

    return {"message": "PIN changed successfully"}

@app.delete("/delete_account/")
def delete_account(account_id: int,pin:int, db: Session = Depends(get_db)):
    account = db.query(BankAccount).filter(BankAccount.account_id == account_id and BankAccount.pin == pin).first()

    if account.balance != 0:
        raise HTTPException(status_code=400, detail="Please withdraw all the money before deleting the account.")
    if not account:
        raise HTTPException(status_code=404, detail="Account not found Create a Bank Account.")

    db.delete(account)
    db.commit()

    return {"message": "Account deleted successfully Thank you for choosing Harshad Mehta Banks. We hope to see you again."}