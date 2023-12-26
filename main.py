import json
import math


def numerical_integration(lower, upper):
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

    print(json.dumps(json_integrals))


def main():
    lower_limit = 0
    upper_limit = math.pi
    numerical_integration(lower_limit, upper_limit)


if __name__ == "__main__":
    main()
