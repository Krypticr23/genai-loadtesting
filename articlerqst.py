import requests

topic = input("Enter the topic or instruction for the article:\n")

res = requests.post("http://localhost:8000/chat", json={"topic": topic})
print("\n--- FULL RESPONSE ---\n")
print(res.json())
