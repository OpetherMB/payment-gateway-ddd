from application.dtos.PaymentRequest import PaymentRequest
from application.services.gen_id import generate_unique_payment_id
from domain.entities.payment_transaction import PaymentTransaction
from domain.value_objects.amount import Amount
from domain.value_objects.card_details import CardDetails
from infrastructure.adapters.bank_adapter import IBankAdapter
from infrastructure.repositories.interface import IRepository


class PaymentProcessingService:
    def __init__(self, repo: IRepository, acquirerBank: IBankAdapter) -> None:
        self.repo = repo
        self.acquirerBank = acquirerBank

    def process_payment(self, paymentDto: PaymentRequest):
        # map dto to entities and value objects
        amount = Amount(paymentDto.amount, paymentDto.currency)
        card_details = CardDetails(
            paymentDto.card_number,
            paymentDto.expiry_month,
            paymentDto.expiry_year,
            paymentDto.cvv,
        )

        payment_transaction = PaymentTransaction(
            transaction_id=generate_unique_payment_id(paymentDto),
            card_details=card_details,
            amount=amount,
            status="pending",
        )

        response = self.acquirerBank.process_payment(paymentDto)

        # update entitiy status
        payment_transaction.status = (
            "authorized" if response.get("authorized") else "declined"
        )

        # save repo
        self.repo.save_payment(payment_transaction.transaction_id, payment_transaction)

        return payment_transaction
