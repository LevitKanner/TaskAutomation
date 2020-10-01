"""
DownloadXkcd.py - Downloads all comics from the most recent to back to the very first on Xkcd.com
"""
import requests, bs4, webbrowser
from pathlib import Path
import os

url = "https://xkcd.com/"
# if not Path("comic").exists():
#     Path("comic").mkdir()
os.makedirs("comic", exist_ok=True)
  
while not url.endswith("#"):
    print(f"Downloading: {url}")
    site = requests.get(url)
    site.raise_for_status
    
    content = bs4.BeautifulSoup(site.text, "html.parser")
    images = content.select("div[id='comic'] > img")
    imgSrc = f"https://xkcd.com{images[0].get('src')}"
    print(imgSrc)
    
    # Download image
    print(f"Downloading image - {imgSrc}")
    image = requests.get(imgSrc)
    image.raise_for_status()
    
    #save image to ./xkcd
    with open(Path("comic") / os.path.basename(imgSrc), "wb") as imgFile:
        imgFile.write(image.content)
        
    #Link to previous comic
    prev = content.select("a[rel='prev']")
    url = f"https://xkcd.com{prev[0].get('href')}"
print("Done!")