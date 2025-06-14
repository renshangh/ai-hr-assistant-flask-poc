import logging
import azure.functions as func
import json

from shared.langchain_logic import get_hr_answer  # Make sure this import matches your function

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid JSON.",
            status_code=400
        )

    question = req_body.get('question')
    if not question:
        return func.HttpResponse(
            "Please pass a question in the request body.",
            status_code=400
        )

    # Use your AI logic
    try:
        answer = get_hr_answer(question)

        return func.HttpResponse(
            json.dumps({"answer": answer}),
            mimetype="application/json"
    )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"answer": "Sorry, there was an error."}),
            mimetype="application/json",
            status_code=500
        )