from pydantic import BaseModel,Field
from random import randint
def random_destination():
    default=randint(11000,11999)
    


class Shipment(BaseModel):
    content:str=Field(max_length=40)
    weight:float=Field(description="Weight in shipment in Kilogram(KG)",le=25,ge=1)
    destination:int | None = Field(default_factory=random_destination,)
