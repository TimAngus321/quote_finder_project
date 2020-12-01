from django.http import HttpResponse
from django.shortcuts import render 
import requests


def home(request):
    url = "https://favqs.com/api/qotd"
    # headers = {
    # 'api-key': "27cc44a2c5c8a6ad64b012d7e4b3ed03",
    # }
    response = requests.request("GET", url,)
    print(response.text)
    quotes = {}
    quotes['quote'] = response.json()['quote']['body']
    quotes['author'] = response.json()['quote']['author']
    return render(request, "home.html", quotes) 
    # return render(request, "home.html", quotes)  

def favouriteQuotes(request):
    return HttpResponse("favouriteQuotes")
    
    
    
# url = 'https://quotes.rest/qod?category=management'
#     api_token = "X-TheySaidSo-Api-Secret"
#     headers = {'content-type': 'application/json',
# 	    'X-TheySaidSo-Api-Secret': format(api_token)}

#     response = requests.get(url, headers=headers)
#     #print(response)
#     quotes=response.json()['contents']['quotes'][0]
#     print(quotes)
#     return render(request, "home.html"), {
#         'quote': quotes['quote']
#     }
# 
# 
# response = requests.get('http://freegeoip.net/json/')
# geodata = response.json()
# return render(request, 'home.html', {
#     'ip': geodata['ip'],
#     'country': geodata['country_name']
# })  
# 

# How to do variables 
# quotes = {}
# quotes['Variable'] = 'I am a variable'