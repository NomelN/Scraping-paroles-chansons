import requests
from pprint import pprint
from bs4 import BeautifulSoup


def extract_lyrics(url):
    r = requests.get(url)
    if r.status_code != 200:
        print("La page impossible à récupérer ")
        return []
    
    soup = BeautifulSoup(r.content, "html.parser")
    lyrics = soup.find("div", class_="YYrds")
    pprint(lyrics)

    if not lyrics:
        return extract_lyrics(url)


def get_all_urls():
    lien_de_pages = []
    numero_page = 1

    while True:
        r = requests.get(f"https://genius.com/api/artists/29743/songs?page={numero_page}&sort=popularity")

        if r.status_code == 200:
            response = r.json().get("response", {})
            page_suivante = response.get("next_page")

            songs = response.get("songs")

            for song in songs:
                url = song.get("url")
                if "".join(url).startswith("https://genius.com/Patrick-bruel"):
                    lien_de_pages.append(url)
            numero_page += 1
            
            if not page_suivante:
                print("page suivante indisponible")
                break 
    return lien_de_pages

mes_pages = get_all_urls()
#pprint(mes_pages)
extract_lyrics("https://genius.com/Patrick-bruel-quest-ce-quon-fait-lyrics")

#print(len(mes_pages))