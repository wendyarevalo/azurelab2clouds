# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import azure.functions as func

def main(inputData):
    mapped_data = []

    words = inputData[1].split()
    for word in words:
        mapped_data.append((word, 1))

    return mapped_data
