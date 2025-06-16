import os
from azure.storage.blob import BlobServiceClient
from datetime import datetime
from zoneinfo import ZoneInfo

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME", "logs")

blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(BLOB_CONTAINER_NAME)

def log_question_to_blob(question):
    timestamp = datetime.now(ZoneInfo("America/Chicago")).isoformat()

    log_entry = f"{timestamp} Question: {question}\n---\n"

    blob_name = "questions.txt"
    blob_client = container_client.get_blob_client(blob_name)

    try:
        existing_data = blob_client.download_blob().readall().decode("utf-8")
    except:
        existing_data = ""

    updated_data = existing_data + log_entry
    blob_client.upload_blob(updated_data, overwrite=True)
