import azure.functions as func
import logging
import math
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    upper = req.params.get('upper')
    lower = req.params.get('lower')
    if not upper or not lower:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            upper = req_body.get('upper')
            lower = req_body.get('lower')

    N_intervals = [10, 100, 1000, 10000, 100000, 1000000]
    N_integrals = "{}"
    json_integrals = json.loads(N_integrals)
    for N in N_intervals:
        subinterval_width = (upper - lower) / N
        integral = 0.0

        for i in range(N):
            rectangle = lower + i * subinterval_width
            integral += abs(math.sin(rectangle)) * subinterval_width

        n_integral = {N: f'{integral:.10f}'}
        json_integrals.update(n_integral)
    
    return func.HttpResponse(
            json.dumps(json_integrals),
            status_code=200
        )