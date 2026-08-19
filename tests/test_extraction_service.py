from models.search_result import SearchResult
from services.extraction_service import ExtractionService


result = SearchResult(
    title="Google AI Scholarship",
    url="https://example.com/scholarship",
    snippet=(
        "Google is offering a scholarship for Indian students "
        "interested in artificial intelligence. The scholarship "
        "supports students pursuing AI-related studies."
    )
)

service = ExtractionService()

extracted = service.extract(result)

print(extracted)