import json
import logging
import re

import azure.functions as func


TITLES_MAPPING = {
    "Köchling-Wehner2020_Article_DiscriminatedByAnAlgorithmASys.pdf": (
        "Discriminated by an algorithm: a systematic review "
        "of discrimination and fairness by algorithmic decision making "
        "in the context of HR recruitment and HR "
        "development"
    ),
    "Liang-Lin2021_Article_MachineLearningForDigitalTry-o.pdf": (
        "Machine learning for digital try-on: Challenges and progress"
    ),
    "s13173-013-0117-7.pdf": "A systematic review on keystroke dynamics",
    "s13640-018-0373-8.pdf": (
        "Augmented reality virtual glasses try-on " "technology based on iOS platform"
    ),
    "s13640-020-00545-z.pdf": "A classification method for social information of sellers on social network",
    "s13673-018-0135-8.pdf": "QER: a new feature selection method for sentiment analysis",
    "s13673-019-0177-6.pdf": "Mobile marketing recommendation method based on user location feedback",
    "s40064-015-1515-4.pdf": "Multi technique amalgamation for enhanced information identification with content based image data",
    "s40294-016-0016-9.pdf": "Sentiment analysis and the complex natural language",
    "s40467-015-0033-9.pdf": "Extraction methods for uncertain inference rules by ant colony optimization",
    "s40493-015-0015-3.pdf": "Reusable components for online reputation systems",
    "s40493-015-0019-z.pdf": "Toward a testbed for evaluating computational trust models: experiments and analysis",
    "s40537-018-0141-8.pdf": "Privacy preservation techniques in big data analytics: a survey",
    "s40537-019-0184-5.pdf": "Mining aspects of customer's review on the social network",
    "s40537-019-0210-7.pdf": "Big data stream analysis: a systematic literature review",
    "s40537-019-0258-4.pdf": "Context-aware rule learning from smartphone data: survey, challenges and future directions",
    "s40537-020-00292-y.pdf": "Improving prediction with enhanced Distributed Memory-based Resilient Dataset Filter",
    "s40708-015-0017-z.pdf": "Local regression transfer learning with applications to users' psychological characteristics prediction",
    "s40708-020-00109-x.pdf": "Technological advancements and opportunities in Neuromarketing: a systematic review",
    "s41109-020-00330-x.pdf": "Detecting problematic transactions in a consumer-to-consumer e-commerce network",
}


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    try:
        req_body = req.get_json()

        output_values = []
        for value in req_body["values"]:
            record_id = value["recordId"]
            title = TITLES_MAPPING[value["data"]["metadata_storage_name"]]

            output_values.append(
                {
                    "recordId": record_id,
                    "data": {"articleName": title},
                    "errors": None,
                    "warnings": None,
                }
            )

        return func.HttpResponse(
            json.dumps({"values": output_values}),
            headers={"Content-Type": "application/json"},
        )
    except:
        return func.HttpResponse(
            json.dumps({"error": "Bad request"}),
            status_code=400,
            headers={"Content-Type": "application/json"},
        )
