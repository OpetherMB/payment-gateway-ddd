from typing import Dict
from fastapi import FastAPI
from api.routers.payment_transaction import payment_router
from api.exceptionHandler import bank_exception_handler
from application.exceptions.exception_adapter import BankException

app = FastAPI()

app.include_router(payment_router)

app.add_exception_handler(BankException, bank_exception_handler)


@app.get("/")
async def ping() -> Dict[str, str]:
    return {"app": "payment-gateway-api"}
