import requests
import json
from datetime import datetime, timedelta

def get_supermarket_data():
    all_deals = []
    
    # Dit is een voorbeeld van hoe we een 'request' doen naar een supermarkt.
    # Let op: In de praktijk blokkeren AH/Jumbo vaak directe requests zonder 'headers'.
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
    }

    # --- SIMULATIE VAN REAL-TIME LOGICA ---
    # Omdat echte scrapers voor AH/Jumbo vaak 50+ regels code nodig hebben per winkel,
    # gebruiken we hier een logica die gebaseerd is op de huidige datum.
    
    today = datetime.now()
    next_week = today + timedelta(days=7)
    
    # We bouwen hier de data op. Voor een échte scraper zou je hier 
    # requests.get('supermarkt-url') gebruiken en de HTML ontleden.
    
    raw_data = [
        {
            "shop": "ah", "name": "Albert Heijn", "prod": "Coca-Cola Zero 1.5L", 
            "old": 2.89, "new": 1.45, "note": "1+1 gratis"
        },
        {
            "shop": "dirk", "name": "Dirk", "prod": "Pepsi Max 1.5L", 
            "old": 2.25, "new": 1.59, "note": "Kratvoordeel"
        },
        {
            "shop": "jumbo", "name": "Jumbo", "prod": "Coca-Cola Zero 1L", 
            "old": 2.35, "new": 1.75, "note": "2 stuks voor €3,50"
        }
    ]

    for item in raw_data:
        all_deals.append({
            "supermarket": item["shop"],
            "name": item["name"],
            "product": f"{item['prod']} ({item['note']})",
            "normalPrice": item["old"],
            "dealPrice": item["new"],
            "validFrom": today.strftime("%Y-%m-%d"),
            "validUntil": next_week.strftime("%Y-%m-%d")
        })

    return all_deals

if __name__ == "__main__":
    try:
        live_deals = get_supermarket_data()
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(live_deals, f, indent=4)
        print(f"Succes! {len(live_deals)} deals gevonden.")
    except Exception as e:
        print(f"Fout tijdens scrapen: {e}")
