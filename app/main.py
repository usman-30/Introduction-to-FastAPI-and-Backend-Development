
from typing import Any

from fastapi import FastAPI, HTTPException
from scalar_fastapi import get_scalar_api_reference

app = FastAPI(title="Shipment API")

# Sample shipment data
shipment = {
    1: {
        "content": "Laptop",
        "weight": 5,
        "status": "in transit"
    },
    2: {
        "content": "Mobile",
        "weight": 2,
        "status": "delivered"
    },
    3: {
        "content": "Wooden box",
        "weight": 10,
        "status": "in transit"
    }
}


# Query parameter
@app.get("/shipment")
def get_shipment(id: int | None = None) -> dict[str, Any]:

    # If no ID is provided, select the latest shipment
    if id is None:
        id = max(shipment.keys())

    # Check whether shipment exists
    if id not in shipment:
        return {"Detail":"Shipment not found"}
    
    return shipment[id]
            
        

    


# Scalar API documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_doc():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Shipment API Documentation"
    )
