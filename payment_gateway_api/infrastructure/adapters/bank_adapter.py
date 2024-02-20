from abc import ABC, abstractmethod
from application.dtos.PaymentRequest import PaymentRequest


class IBankAdapter(ABC):
    @abstractmethod
    def process_payment(self, PaymentRequest: PaymentRequest):
        ...
