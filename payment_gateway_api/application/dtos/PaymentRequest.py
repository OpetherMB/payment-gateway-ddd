from datetime import date
from enum import Enum
from pydantic import BaseModel, constr, Field, validator


class Currency(str, Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"


class PaymentRequest(BaseModel):
    card_number: constr(regex=r"^\d{14,19}$")
    expiry_month: int = Field(..., ge=1, le=12)
    expiry_year: int
    currency: Currency
    amount: int
    cvv: constr(regex=r"^\d{3,4}$")

    @validator("expiry_year")
    def validation_year(cls, v):
        if date.today().year > v:
            raise ValueError("Error year must in future !")
        return v

    @property
    def expiry_date(self):
        return f"{self.expiry_month}/{self.expiry_year}"
