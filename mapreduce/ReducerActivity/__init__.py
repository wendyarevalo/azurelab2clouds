# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import azure.functions as func

def main(shuffledData):
    reduced_results = []

    for key, values in shuffledData.items():
        total_count = sum(values)
        reduced_results.append((key, total_count))

    return reduced_results
