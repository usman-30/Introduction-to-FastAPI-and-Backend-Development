
from typing import Any

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
app = FastAPI()


@app.get("/shipment/{id}")
def get_shipment(id: int) -> dict[str, Any]:
    return {"id": id, "content": "wooden box", "weight": 10, "status": "in transit"}


@app.get("/scalar")
def get_scalar_doc():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar API")
