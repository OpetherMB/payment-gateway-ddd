from abc import ABC, abstractmethod

from domain.entities.payment_transaction import PaymentTransaction


class IRepository(ABC):
    @abstractmethod
    def save_payment(payment_id: str, payment_transation: PaymentTransaction):
        pass

    @abstractmethod
    def get_payment_by_id(payment_id: str):
        pass
