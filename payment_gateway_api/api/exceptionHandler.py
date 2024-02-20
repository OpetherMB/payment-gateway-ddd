from fastapi import Request, status
from fastapi.responses import JSONResponse

from application.exceptions.exception_adapter import BankException


async def bank_exception_handler(req: Request, exc: BankException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"message": "DECLINED"}
    )


# TODO validation requesthandler 400
