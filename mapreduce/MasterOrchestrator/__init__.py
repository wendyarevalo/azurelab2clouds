# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    input_data = yield context.call_activity('GetInputDataFn')
    tasks = []
    for line in input_data:
        tasks.append(context.call_activity("MapperActivity", line))

    map_results = yield context.task_all(tasks)
    shuffle_results = yield context.call_activity('ShufflerActivity', map_results)
    tasks = []
    for key,values in shuffle_results.items():
        tasks.append(context.call_activity("ReducerActivity", {key:values}))

    reduce_results = yield context.task_all(tasks)
    return reduce_results

main = df.Orchestrator.create(orchestrator_function)