import json

def main():
    # Dit is de data die de app gaat inladen
    deals = [
        {
            "supermarket": "ah",
            "name": "Albert Heijn",
            "product": "Coca-Cola Zero 1.5L (1+1 gratis)",
            "normalPrice": 5.70,
            "dealPrice": 2.85,
            "validFrom": "2026-04-15",
            "validUntil": "2026-04-21"
        },
        {
            "supermarket": "dirk",
            "name": "Dirk",
            "product": "Pepsi Max 1.5L",
            "normalPrice": 2.29,
            "dealPrice": 1.49,
            "validFrom": "2026-04-15",
            "validUntil": "2026-04-21"
        },
        {
            "supermarket": "jumbo",
            "name": "Jumbo",
            "product": "Coca-Cola Zero 1L",
            "normalPrice": 2.39,
            "dealPrice": 1.50,
            "validFrom": "2026-04-19",
            "validUntil": "2026-04-26"
        }
    ]
    
    # Dit maakt het bestandje 'data.json' aan waar de app naar zoekt
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(deals, f, indent=4)
    print("Bestand data.json is succesvol aangemaakt!")

if __name__ == "__main__":
    main()
