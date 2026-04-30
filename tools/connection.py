from pydantic import BaseModel, Field, model_validator
from .zone import Zone

class connection(BaseModel):
    hub_a: Zone
    hub_b: Zone
    max_link_capacity: int = Field(default=1)