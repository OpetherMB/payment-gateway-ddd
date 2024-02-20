from locale import currency
from typing import Literal
from pydantic import BaseModel

from application.dtos.PaymentRequest import Currency
from domain.entities.payment_transaction import PaymentTransaction
from domain.value_objects.amount import Amount


class PaymentResponse(BaseModel):
    payment_id: str
    status: Literal["authorized", "declined"]
    last_four_digits: str
    expiry_date: str
    currency: Currency
    amount: int

    @classmethod
    def from_domain(cls, payment_transation: PaymentTransaction):
        return cls(
            payment_id=payment_transation.transaction_id,
            status=payment_transation.status,
            last_four_digits=payment_transation.card_details.card_number[-4:],
            expiry_date=f"{payment_transation.card_details.expiry_month}/{payment_transation.card_details.expiry_year}",
            currency=payment_transation.amount.currency,
            amount=payment_transation.amount.value,
        )
