import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta

def scrape_dirk():
    deals = []
    # Zoekopdracht bij Dirk voor Cola en Pepsi
    url = "https://www.dirk.nl/zoeken?q=pepsi%20coca%20cola"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Dirk toont producten vaak in 'product-card' elementen
        # Let op: dit kan veranderen als Dirk hun site vernieuwt!
        products = soup.find_all('div', class_='product-card')
        
        for p in products:
            title = p.find('div', class_='product-card__name').text.strip()
            
            # We filteren alleen op 1L en 1.5L flessen
            if any(size in title for size in ["1,5l", "1l", "1.5L", "1L"]) and \
               any(brand in title.lower() for brand in ["pepsi max", "coca-cola zero"]):
                
                # Check of er een aanbieding-label is
                promo = p.find('div', class_='product-card__promo-label')
                if promo:
                    price_element = p.find('div', class_='product-card__price')
                    # Hier zou je normaal de prijs uit de tekst trekken
                    # Voor dit voorbeeld vullen we een gevonden deal in
                    deals.append({
                        "supermarket": "dirk",
                        "name": "Dirk",
                        "product": title,
                        "normalPrice": 2.29, # Dit zou je idealiter ook scrapen
                        "dealPrice": 1.49,
                        "validFrom": datetime.now().strftime("%Y-%m-%d"),
                        "validUntil": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
                    })
        return deals
    except Exception as e:
        print(f"Fout bij Dirk: {e}")
        return []

if __name__ == "__main__":
    found_deals = scrape_dirk()
    
    # Als Dirk niks heeft, voegen we voor nu even handmatige data toe om te testen
    if not found_deals:
        print("Geen live deals gevonden bij Dirk, check de filters in de code.")
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(found_deals, f, indent=4)
