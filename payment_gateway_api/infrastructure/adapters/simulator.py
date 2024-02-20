from application.dtos.PaymentRequest import PaymentRequest
from infrastructure.adapters.bank_adapter import IBankAdapter
import requests
from application.exceptions.exception_adapter import BankException


class AcquirerBAnkSimulator(IBankAdapter):
    def process_payment(self, PaymentRequest: PaymentRequest):
        req = PaymentRequest.dict(exclude={"expiry_month", "expiry_year"})

        response = requests.post(
            "http://bank_simulator:8080/payments",
            json=req,
        )
        print(response.status_code)
        if response.status_code != 200:
            raise BankException(
                f" Failed to process payment with status {response.status_code}"
            )

        return response.json()
