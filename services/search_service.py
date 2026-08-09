from tavily import TavilyClient
from config.settings import settings
from models.search_result import SearchResult

class SearchService:
    def __init__(self):
        self.client = TavilyClient(api_key=settings.TAVILY_API_KEY)
        

    def search(self, query:str)-> list[SearchResult]:
        if not query.strip():
            return []
        response = self.client.search(query) 
        
        results = []
        for item in response['results']:
            search_result = SearchResult(
                title=item.get("title", ""),
                url=item.get("url", ""),
                snippet=item.get("content", "")
            )

            
            results.append(search_result)
        return  results
    
