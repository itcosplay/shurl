import requests


# url = 'http://127.0.0.1:8000/create'
url = 'http://127.0.0.1:8000/create_coustom'

data = {
  "url": "https://hd.kinopoisk.ru/",
  "coustom_url": "my-kinopoisk"
}

# data = {
#   "url": "https://www.performance-lab.ru/blog/luchshie-instrumenty-dlya-nagruzochnogo-testirovaniya"
# }

response = requests.post(url, data=data)
response.raise_for_status()

print(response.text)
# {"short_url": "127.0.0.1:8000/b2kK"}


# redirect_url = Link.objects.filter (
#         Q(short_url=short_url) | Q(coustom_url=short_url)
#     )[0].url