import requests

# === CONFIGURARE ===
TOKEN = "AICI_PUI_TOKENUL_TĂU_DE_LA_BOTFATHER"
CHANNEL = "@NumeleCanaluluiTau"  # Exemplu: @canalulpatiseria
PHOTO_URL = "https://upload.wikimedia.org/wikipedia/commons/6/6e/Golde33443.jpg"  # Schimbă cu linkul tău
CAPTION = "Salut! Aceasta este o poză postată automat de bot 📸"

# === TRIMITEREA POZEI ===
url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
payload = {
    "chat_id": CHANNEL,
    "photo": PHOTO_URL,
    "caption": CAPTION
}

response = requests.post(url, data=payload)

# === RĂSPUNS ===
if response.status_code == 200:
    print("✅ Poză trimisă cu succes pe canal!")
else:
    print("❌ Eroare:", response.text)
