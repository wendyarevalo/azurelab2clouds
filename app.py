from flask import Flask
import math
import json

app = Flask(__name__)


@app.route('/numericalintegralservice/<lower_str>/<upper_str>')
def get_numerical_integration(lower_str, upper_str):
    upper = float(upper_str)
    lower = float(lower_str)
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

    return json.dumps(json_integrals), 200
