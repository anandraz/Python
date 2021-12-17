import requests

url = "https://currency23.p.rapidapi.com/exchange"

querystring = {"base":"USD","to":"EUR","int":"1"}

headers = {
    'x-rapidapi-host': "currency23.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)