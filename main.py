
# from agent.scholarship_agent import ScholarshipAgent

# def main():
#     agent=ScholarshipAgent()
#     agent.run()

# if __name__ == "__main__":
#     main()

from services.opportunity_service import OpportunityService

from services.search_service import SearchService

search_service = SearchService()
opportunity_service = OpportunityService()

#results = search_service.search("AI scholarships for Indian students")
queries = ["AI scholarships for Indian students",
           "AI jobs in Germany",
            "machine learning internships in India",
            ]
for query in queries:
    print(f"\nQUERY: {query}")
    results = search_service.search(query)
    opportunity_service = OpportunityService()
    opportunities = opportunity_service.extract(results)
    for opportunity in opportunities:
        print(opportunity)
      
