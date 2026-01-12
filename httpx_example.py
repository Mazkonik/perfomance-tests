import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.json())
print(response.status_code)

data = {
    "name": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos")

print(response.json())
print(response.status_code)

headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.json())
print(response.status_code)

params = {"user_id": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.json())
print(response.status_code)
print(response.request.url, response.request.url.query)

files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)

print(response.json())
print(response.status_code)

client = httpx.Client(
    headers = {"Authorization": "Bearer my_secret_token"},
    base_url = "https://jsonplaceholder.typicode.com",
)
response1 = client.get("/todos/1")
response2 = client.get("/todos/2")

print(response1.json(), response2.json())
print(response1.request.headers)


try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout as e:
    print("Запрос превысил лимит времени")