from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class Opportunity(BaseModel):
    id : UUID
    title : str
    place : str
    role : str
    description : str
    created_at : datetime
    source : str
    opportunity_type : str
    status : str
    contact : str




    