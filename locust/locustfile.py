from locust import HttpUser, TaskSet, task, between
import random

class APICalls(TaskSet):
    @task()
    def getpost(self):
        self.client.get("/")

    @task()
    def postpost(self):
        self.client.post("/predict",json={"CHAS":{"0":0},"RM":{"0":6.575},"TAX":{"0":296.0},"PTRATIO":{"0":15.3},"B":{"0":396.9},"LSTAT":{"0":4.98}})

class APIUser(HttpUser):
    tasks = [APICalls]
    wait_time = between(5, 10) # seconds
