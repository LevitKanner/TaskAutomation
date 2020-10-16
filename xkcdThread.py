"""
xkcdThread.py - Downloads comic images from xkcd.com using multiple threads.
"""

import requests, bs4, threading,os
from pathlib import Path

os.makedirs("ImageDownloads", exist_ok= True)
def download(start, end) :
    for i in range(start, end):
        
        url = f"https://xkcd.com/{i}"
        res = requests.get(url)
        res.raise_for_status()
        
        content = bs4.BeautifulSoup(res.text, "html.parser")
        imgElems = content.select("div[id='comic'] > img")
        
        if len(imgElems) == 0:
            print("Could not find images")
        else:
            imgLink = f"https://xkcd.com{imgElems[0].get('src')}"
            img = requests.get(imgLink)
            img.raise_for_status
            
            with open(Path("ImageDownloads") / os.path.basename(imgLink), "wb") as f:
                f.write(img.content)
                
threads = []
for i in range(0, 140, 10):
    end = i + 9
    start = 1 if i == 0 else i
    
    thread = threading.Thread(target= download, args=[start, end])
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
print("Download complete!")