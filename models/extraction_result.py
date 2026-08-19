from pydantic import BaseModel

class ExtractionResult(BaseModel):
    title: str
    location: str | None = None
    description: str
    opportunity_type: str | None = None