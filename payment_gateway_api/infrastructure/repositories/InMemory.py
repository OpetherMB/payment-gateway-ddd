from re import I
from domain.entities.payment_transaction import PaymentTransaction

from infrastructure.repositories.interface import IRepository


class InMemoryRepo(IRepository):
    def __init__(self) -> None:
        self.store = {}

    def get_payment_by_id(payment_id: str):
        return super().get_payment_by_id()

    def save_payment(payment_id: str, payment_transation: PaymentTransaction):
        return super().save_payment(payment_transation)
