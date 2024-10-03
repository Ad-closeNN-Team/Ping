import requests
import time
from bs4 import BeautifulSoup
url = "https://profile-counter.glitch.me/WForst_Breeze/count.svg"
a = 0
while a <= 30000:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    numbers = ''.join([tspan.get_text() for tspan in soup.find_all('tspan')])
    if response.status_code == 200:
        print(f"[{a}] GET {numbers} OK: "+str(response.status_code))
        a = a + 1
        time.sleep(0.5)
    else:
        print("Error: "+str(response.status_code))
