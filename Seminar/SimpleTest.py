from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    # def on_start(self):
    #     # Log in at the start if authentication is required
    #     response = self.client.post("/api/login", json={"username": "testuser", "password": "password"})
    #     self.token = response.json().get("token")
    #     self.headers = {"Authorization": f"Bearer {self.token}"}
    
    @task
    def to_home(self):
        self.client.get("/")
        
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)  
    host = "https://www.calculator.net//"  