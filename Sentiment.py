import requests

url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

querystring = {"text":"great value in its price range!"}

headers = {
	"X-RapidAPI-Key": "KEY",
	"X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
