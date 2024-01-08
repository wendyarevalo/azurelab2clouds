# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import os
import azure.functions as func
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")
blob_prefix = os.getenv("AZURE_STORAGE_BLOB_PREFIX")

def get_blob_data():
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    input_data = []

    blobs = container_client.list_blobs(name_starts_with=blob_prefix)

    for blob in blobs:
        blob_client = container_client.get_blob_client(blob.name)
        content = blob_client.download_blob().readall().decode('utf-8')

        lines = content.split('\n')
        for offset, line in enumerate(lines):
            input_data.append((offset, line.strip()))

    return input_data

def main(context: func.Context):
    input_data = get_blob_data()
    return input_data