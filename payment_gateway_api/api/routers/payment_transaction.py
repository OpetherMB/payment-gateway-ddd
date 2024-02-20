from fastapi import APIRouter, Depends, HTTPException, status
from application.dependecies import get_payment_service
from application.dtos.PaymentRequest import PaymentRequest

from application.dtos.PaymentResponse import PaymentResponse
from application.services.payment_processing import (
    PaymentProcessingService,
)


payment_router = APIRouter()


@payment_router.post("/payment", response_model=PaymentResponse)
def process_payment(
    paymentRequest: PaymentRequest,
    payment_service: PaymentProcessingService = Depends(get_payment_service),
):
    try:
        transaction_result = payment_service.process_payment(paymentDto=paymentRequest)
        payment_response = PaymentResponse.from_domain(transaction_result)
        return payment_response

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"REJECTED {e}"
        )
