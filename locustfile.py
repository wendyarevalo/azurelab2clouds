import time
from locust import HttpUser, task

#locust --headless --host "http://127.0.0.1:5000" -u 1 --run-time 180 --csv=results
class QuickstartUser(HttpUser):
    @task
    def numerical_integration(self):
        #self.client.get("/numericalintegralservice/0/3.14159")
        self.client.get("/api/http_trigger",json={ "lower": 0,"upper":3.14159 })