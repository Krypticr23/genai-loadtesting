from locust import HttpUser, task, between
import random
articles = [
    "AI is transforming the way we live and work. It has wide applications in healthcare, education, and more.",
    "The global economy is seeing signs of recovery amid inflation and supply chain shifts.",
    "Climate change is accelerating with rising sea levels and extreme weather events.",
    "Space exploration has resumed with new missions to the moon and Mars.",
    "Quantum computing may revolutionize problem solving in cryptography and medicine."
]

class ChatUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def send_request(self):
        article = random.choice(articles)
        self.client.post("/chat", json={"article": article})