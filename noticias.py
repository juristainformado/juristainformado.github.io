import requests
import json
from datetime import datetime

# URL de ejemplo del Diario Oficial (ajustaremos si cambia la fuente real)
URL = "https://www.diariooficial.interior.gob.cl/feed/"

def obtener_noticias():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        # Guardamos el feed como JSON simplificado
        noticias = []
        for i, item in enumerate(response.text.split("<item>")[1:6], start=1):  
            titulo = item.split("<title>")[1].split("</title>")[0]
            link = item.split("<link>")[1].split("</link>")[0]

            noticias.append({
                "id": i,
                "titulo": titulo.strip(),
                "link": link.strip(),
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

        with open("noticias.json", "w", encoding="utf-8") as f:
            json.dump(noticias, f, ensure_ascii=False, indent=4)

        print("✅ Noticias actualizadas en noticias.json")

    except Exception as e:
        print("❌ Error obteniendo noticias:", e)

if __name__ == "__main__":
    obtener_noticias()
