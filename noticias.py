import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

URL = "https://www.diariooficial.interior.gob.cl/feed/"

def obtener_noticias():
    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "xml")  # RSS feed

        noticias = []
        items = soup.find_all("item")[:5]  # primeros 5
        for i, item in enumerate(items, start=1):
            titulo = item.title.text
            link = item.link.text
            fecha = item.pubDate.text
            noticias.append({
                "id": i,
                "titulo": titulo,
                "link": link,
                "fecha": fecha
            })

        with open("noticias.json", "w", encoding="utf-8") as f:
            json.dump(noticias, f, ensure_ascii=False, indent=4)

        print("✅ Noticias actualizadas en noticias.json")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    obtener_noticias()
