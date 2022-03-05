import requests

url = 'http://127.0.0.1:8000/create'

data = {
  "url": "https://www.performance-lab.ru/blog/luchshie-instrumenty-dlya-nagruzochnogo-testirovaniya"
}

response = requests.post(url, data=data)
response.raise_for_status()

print(response.text)
# {"short_url": "127.0.0.1:8000/b2kK"}