from domain.value_objects.amount import Amount
from domain.value_objects.card_details import CardDetails


class PaymentTransaction:
    def __init__(
        self,
        transaction_id: str,
        card_details: CardDetails,
        amount: Amount,
        status: str,
    ) -> None:
        self.transaction_id = transaction_id
        self.card_details = card_details
        self.amount = amount
        self.status = status

        def _is_valid(self) -> bool:
            # business logic validation
            return True
