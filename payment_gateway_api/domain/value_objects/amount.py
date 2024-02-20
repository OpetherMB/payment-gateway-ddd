from application.dtos.PaymentRequest import Currency


class Amount:
    def __init__(self, amount: int, currency: Currency) -> None:
        self.value = amount
        self.currency = currency
