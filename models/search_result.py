from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class SearchResult(BaseModel):
    title: str  
    snippet : str  
    url : str