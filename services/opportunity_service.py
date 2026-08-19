from models.opportunity import Opportunity
from models.search_result import SearchResult
from models.extraction_result import ExtractionResult
class OpportunityService:
    def extract(self,results: list[SearchResult],
        extracted_results : list[ExtractionResult],) -> list[Opportunity]:
        opportunities = []
        for result, extracted in zip(results, extracted_results):
           opportunity = Opportunity(

           title=extracted.title,
           location=extracted.location,
           description=extracted.description,

           source=result.url,
           opportunity_type=extracted.opportunity_type,
           status="active",
           contact=""
    )
        opportunities.append(opportunity)


        return opportunities
      