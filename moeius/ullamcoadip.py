import requests

url = 'https://www.example.com/api/some-endpoint'
headers = {
    'Referer': 'https://www.example.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

print(response.text)
