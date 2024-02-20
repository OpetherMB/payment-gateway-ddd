# infrastructure/database/models.py

from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PaymentTransactionModel(Base):
    __tablename__ = "payment_transactions"
    ...
