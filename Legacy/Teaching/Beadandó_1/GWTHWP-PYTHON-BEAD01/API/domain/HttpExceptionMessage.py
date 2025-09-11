from enum import Enum
from fastapi import HTTPException

class HttpExceptionMessage(Enum):
    BASKET = "Nem található ilyen kosár"
    ITEM = "Nem található ilyen termék"
    VALUE = "Valamit félre ütöttél"

    def raise_exception(self):
        raise HTTPException(status_code=404, detail=self.value)