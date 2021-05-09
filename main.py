# IMPORTANT MODULES
import requests
import os
from colorama import Fore
from win32com.client import Dispatch


# Here we will add our copyright
os.system("title "+"Top Daily BBC NEWS")
print(Fore.CYAN+"""           
   _     _.     _     _.     _     _   
  (c).-.(c)    (c).-.(c)    (c).-.(c)  
   / ._. \      / ._. \      / ._. \   
 __\( Y )/__  __\( Y )/__  __\( Y )/__ 
(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)
   || A ||      || I ||      || T ||   
 _.' `-' '._  _.' `-' '._  _.' `-' '._ 
(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)
 `-'     `-'  `-'     `-'  `-'     `-' 
"""+Fore.LIGHTGREEN_EX)


api_key = '809cf9fa5828485aa033f4f1543e796f'

url = f'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apikey={api_key}'

get_news = requests.get(url).json()

# print(get_news)

articles = get_news['articles']
# print(articles)

res = []

for art in articles:
    title = res.append('- Title:'+art['title'])
    des = res.append('- Description: '+art['description'])
    source_link = res.append('- Source: '+art['url'])
    imgs = res.append('- Images: '+art['urlToImage'])
    # print(art)
    res.append('------------------------------------------')

# print(res)

for i in range(len(res)):
    print(res[i])

# Let's make simple bot to speak these news for us!
# speak = Dispatch('SAPI.spvoice')
# speak.Speak(res)

# Make program more reusable
input(Fore.RED+ "\n[*] Hit Any Key To Close.."+ Fore.RESET)