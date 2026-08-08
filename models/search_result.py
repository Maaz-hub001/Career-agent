from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class SearchResult(BaseModel):
    title: str  
    snippet : str  
    url : str

# results = search_service.search(
#     "AI scholarships for indian students"
# )    


# # id : UUID | None = None
# title : str
# #location : str
# snippet : str
# # created_at : datetime | None = None
# url : str
# # opportunity_type : str
