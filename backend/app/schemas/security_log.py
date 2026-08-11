from datetime import datetime

from pydantic import BaseModel, Field


class SecurityLogCreate(BaseModel):
    source: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    source_ip: str = Field(
        ...,
        min_length=1,
        max_length=45
    )

    event_type: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    username: str | None = Field(
        default=None,
        max_length=100
    )

    message: str = Field(
        ...,
        min_length=1
    )

    severity: str = Field(
        default="INFO",
        max_length=20
    )


class SecurityLogResponse(BaseModel):
    id: int
    timestamp: datetime
    source: str
    source_ip: str
    event_type: str
    username: str | None
    message: str
    severity: str

    model_config = {
        "from_attributes": True
    }