import threading 
from bs4 import BeautifulSoup
import time
import requests


urls=[
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://en.wikipedia.org/wiki/Generative_artificial_intelligence",
    "https://en.wikipedia.org/wiki/Data_science"
]

def fetch_data(url):
    response=requests.get(url)
    result=BeautifulSoup(response.content,"html.parser")
    print(f"Length of Char is {len(result.text)} in URL:{url}")


start=time.time()

all_threads=[]

for u in urls:
    thread=threading.Thread(target=fetch_data,args=(u,))
    all_threads.append(thread)
    thread.start()

for t in all_threads:
    t.join()

end=time.time()

print(f"Total time taken is: {end-start}")




