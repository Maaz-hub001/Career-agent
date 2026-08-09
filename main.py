
# from agent.scholarship_agent import ScholarshipAgent

# def main():
#     agent=ScholarshipAgent()
#     agent.run()

# if __name__ == "__main__":
#     main()

from services.search_service import SearchService

search_service = SearchService()

#results = search_service.search("AI scholarships for Indian students")
queries = ["AI scholarships for Indian students",
           "AI jobs in Germany",
            "machine learning internships in India",
            ]
for query in queries:
    print(f"\nQUERY: {query}")
    results = search_service.search("")
    for result in results:
        print(result.title)
        print(result.url)
        print(result.snippet)
        print("-"*80)
    
