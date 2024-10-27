from locust import HttpUser, task, between, SequentialTaskSet, TaskSet
from locust import events
from locust.argument_parser import LocustArgumentParser
import random

# Base user class
class BaseUserTaskSets:    
    def __init__(self):
        self.session_token = None
        self.sample_products = ['66c686be4eed0f819e8263d0', '66c696848f776d05af999758', '66c696ac8f776d05af99975d',
                                '66c696cc8f776d05af999762', '66c696e88f776d05af999767', '66e8fe7098151479f020e793',
                                '66e8fe2798151479f020e789']
        self.sample_categories = ['66e59c721534fd85e21a96ee', '66e59f8fc0203e8389198bf8', '66e59fa1c0203e8389198bfb',
                                  '66e59fb2c0203e8389198bfe', '66e59fccc0203e8389198c01']
    
    def get_headers(self):
        return {"Authorization": f"Bearer {self.session_token}"} if self.session_token else {}

    def log_in(self, credentials):
        if not self.session_token:
            try:
                response = self.client.post("/auth/login", json=credentials)
                response_data = response.json()
                if response.status_code == 200 and "accessToken" in response_data.get("data", {}):
                    self.session_token = response_data["data"]["accessToken"]
                    print("Logged in successfully as user")
                else:
                    print(f"Login failed: {response_data}")
                    self.interrupt()
            except Exception as e:
                print(f"Login error: {e}")
                self.interrupt()
   
   
        
# Sequential tasks for clients     
class SequentialClientTaskSet(SequentialTaskSet, BaseUserTaskSets):
    def __init__(self, parent):
        SequentialTaskSet.__init__(self, parent)
        BaseUserTaskSets.__init__(self)

    def on_start(self):
        self.log_in({"username": "client", "password": "20122003"})
        
    #Simulate a process of buying a product
    @task
    def add_to_cart(self):
        
        return
    
    @task
    def add_to_cart(self):
        #do sth
        return
            
# All tasks for clients
class ClientTaskSet(TaskSet, BaseUserTaskSets):
    def __init__(self, parent):
        TaskSet.__init__(self, parent)
        BaseUserTaskSets.__init__(self)

    tasks = {SequentialClientTaskSet: 5}  # Nested sequential tasks, with weight = 5
    
    def on_start(self):
        self.log_in({"username": "client", "password": "20122003"})
    
    @task(20)
    def get_all_categories(self):
        try:
            response = self.client.get("/category")
            if response.status_code != 200:
                print(f"Failed to get categories: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Error retrieving categories: {e}")
    
    @task(10)
    def get_all_products(self):
        try:
            response = self.client.get("/product?page=1&limit=15")
            if response.status_code != 200:
                print(f"Failed to get products: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Error retrieving products: {e}")
            
    @task(10)
    def search_products(self):
        keywords = ['quần', 'áo', 'giày', 'nón', 'trẻ em']
        searchKey = random.choice(keywords)
        try:
            response = self.client.get(f"/product?page=1&limit=15&search={searchKey}")
            if response.status_code != 200:
                print(f"Failed to search product: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Error search products: {e}")

    @task(15)
    def get_product_detail(self):        
        product_id = random.choice(self.sample_products)
        try:
            response = self.client.get(f"/product/{product_id}")
            if response.status_code != 200:
                print(f"Failed to get product {product_id}: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Error retrieving product detail: {e}")

    @task(10)
    def get_category(self):
        cat_id = random.choice(self.sample_categories)
        try:
            response = self.client.get(f"/category/{cat_id}")
            if response.status_code != 200:
                print(f"Failed to get category {cat_id}: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Error retrieving category: {e}")
        
    @task(20)
    def get_products_by_category(self):
        cat_id = random.choice(self.sample_categories)
        try:
            response = self.client.get(f"/product/category/{cat_id}?page=1&limit=10")
            if response.status_code != 200:
                print(f"Failed to get products for category {cat_id}: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Error retrieving products by category: {e}")
        
    @task(10)
    def get_products_filter(self):
        cat_id = random.choice(self.sample_categories)
        try:
            response = self.client.get(f"/product/category/{cat_id}?minPrice=30000&maxPrice=200000&order=asc")
            if response.status_code != 200:
                print(f"Failed to get filtered products for category {cat_id}: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Error retrieving filtered products: {e}")
            
    @task(5)
    def get_cart(self):
        try:
            response = self.client.get(f"/cart/fetch", headers=self.get_headers())
            print(response.json())
            if response.status_code != 200:
                print(f"Failed to get cart: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Error retrieving cart: {e}")
            
        
class AdminTaskSet(TaskSet, BaseUserTaskSets):    
    def __init__(self, parent):
        TaskSet.__init__(self, parent)
        BaseUserTaskSets.__init__(self)
    
    #On application start
    def on_start(self):
        BaseUserTaskSets.log_in({"username": "Admin", "password": "20122003"})
    
    @task
    def to_home(self):
        header = {"Authorization": f"Bearer {self.session_token}"} if self.session_token else {}
        self.client.get("/", headers=header)
        
class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  
    host = "https://olivia-fashion-studio.onrender.com/api"  
    
    def __init__(self, parent):
        super().__init__(parent)
        # Get role from command-line argument
        self.role = self.environment.parsed_options.role

    
    def on_start(self):
        self.tasks = [AdminTaskSet] if self.role == "admin" else [ClientTaskSet]
        
@events.init_command_line_parser.add_listener
def _(parser: LocustArgumentParser):
    parser.add_argument("--role", type=str, default="user", help="Specify role: 'user' or 'admin'")