import hashlib
import uuid
from application.dtos.PaymentRequest import PaymentRequest


def generate_unique_payment_id(payment_data: PaymentRequest) -> str:
    unique_str = f"{uuid.uuid4()}-{payment_data.amount}-{payment_data.card_number}-{payment_data.currency}"
    hashed_id = hashlib.sha256((unique_str.encode())).hexdigest()
    return hashed_id
