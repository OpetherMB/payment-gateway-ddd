from fastapi import Depends
from application.services.payment_processing import (
    PaymentProcessingService,
)
from infrastructure.adapters.bank_adapter import IBankAdapter
from infrastructure.adapters.simulator import AcquirerBAnkSimulator
from infrastructure.repositories.InMemory import InMemoryRepo
from infrastructure.repositories.interface import IRepository


def get_repository() -> IRepository:
    return InMemoryRepo()


def get_bank_acquirer() -> IBankAdapter:
    return AcquirerBAnkSimulator()


def get_payment_service(
    repo: IRepository = Depends(get_repository),
    bank_acquirer: IBankAdapter = Depends(get_bank_acquirer),
) -> PaymentProcessingService:
    return PaymentProcessingService(repo, bank_acquirer)
