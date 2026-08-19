import ollama

from models.search_result import SearchResult
from models.extraction_result import ExtractionResult


class ExtractionService:

    def extract(self, result: SearchResult) -> ExtractionResult:
        response = ollama.chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Extract structured opportunity information from "
                        "the provided search result. Do not invent information. "
                        "Always return every field required by the schema. "
                        "If location cannot be determined, return null. "
                        "For opportunity_type, choose the most appropriate type "
                        "based only on the provided content."
                        "Keep the title and description concise."

                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Title: {result.title}\n"
                        f"Content: {result.snippet[:4000]}"
                    ),
                },
            ],
            format=ExtractionResult.model_json_schema(),
             options={
                      "temperature": 0,
                     "num_predict": 512,
                     }
        )

        return ExtractionResult.model_validate_json(response.message.content)