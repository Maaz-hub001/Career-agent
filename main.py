
# from agent.scholarship_agent import ScholarshipAgent

# def main():
#     agent=ScholarshipAgent()
#     agent.run()

# if __name__ == "__main__":
#     main()

from services.opportunity_service import OpportunityService
from services.extraction_service import ExtractionService     
from services.search_service import SearchService

search_service = SearchService()
opportunity_service = OpportunityService()
extraction_service = ExtractionService()
#results = search_service.search("AI scholarships for Indian students")
queries = ["AI scholarships for Indian students",
           "AI jobs in Germany",
            "machine learning internships in India",
            ]


for query in queries:
    print(f"\nQUERY: {query}")

    results = search_service.search(query)

    extracted_results = []

    for result in results:
        print("Extracting with Qwen...")

        extracted = extraction_service.extract(result)

        print(" Extraction complete")

        extracted_results.append(extracted)

    print("\nAI EXTRACTION:")

    for extracted in extracted_results:
        print(extracted)
    opportunities = opportunity_service.extract(
    results,
    extracted_results
)

    print("\nOPPORTUNITIES:")

    for opportunity in opportunities:
       print(opportunity)
