import requests

url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

querystring = {"text":"great value in its price range!"}

headers = {
	"X-RapidAPI-Key": "07b1d0f1efmsh96130b6ca0a3fbdp17946cjsn9c1f9a89c7f2",
	"X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())