
from typing import Any

from fastapi import FastAPI,status, HTTPException
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
    #Add HttpException for 404 error
    if id not in shipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id is not found in the shipment data"
        )
    
    return shipment[id]

#post method to add shipment data
@app.post("/shipment")
def add_shipment(weight:float,data:dict[str,str]) -> dict[str, Any]:
    content = data.get("content")

    if weight >25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Weight exceeds the maximum allowed limit of 25"
            
        )


    new_id = max(shipment.keys()) + 1 
    shipment[new_id]={
        "content":content,
        "weight":weight,
        "status":"placed"
    }

    return {"id": new_id}

@app.get("/shipment/{field}")
def get_shipment_field(field:str,id:int)-> dict[str,Any]:
    return{
        field:shipment[id][field]
    }
#Update shipment detail using PUT Method
@app.put("/shipment")
def update_shipment(id:int,content:str,weight:float,status:str) -> dict[str,Any]:
    shipment[id]={
         "content":content,
         "weight":weight,
         "status":status
     }
    return shipment[id]

# Update Exiting values
@app.patch("/shipment")
def path_shipment(id:int,
                  body:dict[str,Any]
                 # content:str | None=None,
                 # weight:str | None=None ,
                 # status:str | None=None
                 )-> dict[str,Any]:
    shipments=shipment[id]

    #if content:
    #    shipments[content]=content
    #if status:
    #    shipments[status]=status
    #if weight:
    #    shipments[weight]=weight
    shipments.update(body)
    shipment[id]=shipments
    return shipments

# Delete Items using pop method
@app.delete("/shipment")
def delete_shipment(id:int)-> dict[str,str]:
    shipment.pop(id)
    return {"Detail":f"shipment with id {id} is deleted!"}

# Scalar API documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_doc():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Shipment API Documentation"
    )
