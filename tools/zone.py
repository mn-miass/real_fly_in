from pydantic import BaseModel, Field, model_validator


class Zone(BaseModel):
    max_drones : int = Field(default=1)
    name: str
    start_hub: bool = Field(default=False)
    end_hub: bool = Field(default=False)
    color: str | None = Field(default=None)
    zone: str = Field(default="Normal")
    cordinate_x: int
    coordinate_y: int
