from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class Opportunity(BaseModel):
    id : UUID | None = None
    title : str
    location : str
    description : str
    created_at : datetime | None = None
    source : str
    opportunity_type : str
    status : str
    contact : str




    