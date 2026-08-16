from models.opportunity import Opportunity
from models.search_result import SearchResult

class OpportunityService:
    def extract(self,results: list[SearchResult]) -> list[Opportunity]:
        opportunities = []
        for result in results:
            opportunity = Opportunity(
                
                title=result.title,
                location="unknown",
                description=result.snippet,
            
                source=result.url,
                opportunity_type="unknown",
                status="active",
                contact=""
            )
            opportunities.append(opportunity)


        return opportunities
      