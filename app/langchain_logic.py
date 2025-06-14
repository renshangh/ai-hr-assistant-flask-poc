import os
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import AnalyzeTextOptions
from azure.core.credentials import AzureKeyCredential as CSKeyCredential
from embeddings import retrieve_relevant_docs

load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
AZURE_CONTENT_SAFETY_ENDPOINT = os.getenv("AZURE_CONTENT_SAFETY_ENDPOINT")
AZURE_CONTENT_SAFETY_KEY = os.getenv("AZURE_CONTENT_SAFETY_KEY")

llm = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    deployment_name=AZURE_OPENAI_DEPLOYMENT,
    api_key=AZURE_OPENAI_KEY,
    openai_api_version="2024-02-15-preview"
)

cs_client = ContentSafetyClient(
    endpoint=AZURE_CONTENT_SAFETY_ENDPOINT,
    credential=CSKeyCredential(AZURE_CONTENT_SAFETY_KEY)
)

def get_hr_answer(question):
    retrieved_docs = retrieve_relevant_docs(question, k=3)
    context = "\n".join(retrieved_docs)

    prompt = f"""
    You are an HR assistant. Answer the following question based on these HR policies:

    {context}

    Question: {question}
    """

    response = llm.invoke(prompt)
    answer = response.content

    options = AnalyzeTextOptions(
        text=answer,
        categories=["Hate", "Violence", "SelfHarm", "Sexual"]
    )
    safety = cs_client.analyze_text(options)


    # Check if any category has a severity of 3 or higher
    for category in safety.categories_analysis:
        print(f"Category: {category.category}, Severity: {category.severity}") 

    for category in safety.categories_analysis:
        if category.severity >= 3:
            answer = "[Content flagged for safety review.]"
            break

    return answer
