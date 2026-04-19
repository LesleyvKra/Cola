// Testdata: Dit is hoe de data eruit zou zien als je een backend of API zou hebben
const mockDeals = [
    {
        supermarket: 'ah',
        name: 'Albert Heijn',
        product: 'Coca-Cola Zero 1.5L (4-pack)',
        normalPrice: 11.56,
        dealPrice: 8.67,
        validFrom: '2026-04-20',
        validUntil: '2026-04-26'
    },
    {
        supermarket: 'jumbo',
        name: 'Jumbo',
        product: 'Pepsi Max 1L',
        normalPrice: 2.15,
        dealPrice: 1.07, // 1+1 gratis simulatie
        validFrom: '2026-04-18',
        validUntil: '2026-04-24'
    },
    {
        supermarket: 'plus',
        name: 'Plus',
        product: 'Coca-Cola Zero 1.5L',
        normalPrice: 2.89,
        dealPrice: 2.00,
        validFrom: '2026-04-19',
        validUntil: '2026-04-25'
    },
    {
        supermarket: 'dirk',
        name: 'Dirk',
        product: 'Pepsi Max 1.5L',
        normalPrice: 2.29,
        dealPrice: 1.49,
        validFrom: '2026-04-15',
        validUntil: '2026-04-21'
    }
];

// Functie om datums mooi te formatteren in het Nederlands
function formatDate(dateString) {
    const options = { day: 'numeric', month: 'short' };
    const date = new Date(dateString);
    return date.toLocaleDateString('nl-NL', options);
}

// Functie om valuta mooi te tonen
function formatCurrency(amount) {
    return '€ ' + amount.toFixed(2).replace('.', ',');
}

// Functie om de deals op het scherm te tekenen
function renderDeals(deals) {
    const container = document.getElementById('deals-container');
    container.innerHTML = ''; // Maak loading tekst leeg

    deals.forEach(deal => {
        const savings = deal.normalPrice - deal.dealPrice;
        
        const card = document.createElement('div');
        card.className = 'deal-card';
        
        card.innerHTML = `
            <div class="deal-header">
                <span class="supermarket ${deal.supermarket}">${deal.name}</span>
                <span class="savings">Bespaar ${formatCurrency(savings)}</span>
            </div>
            <div class="product-name">${deal.product}</div>
            <div class="price-container">
                <div>
                    <span class="current-price">${formatCurrency(deal.dealPrice)}</span>
                    <span class="old-price">${formatCurrency(deal.normalPrice)}</span>
                </div>
            </div>
            <div class="validity">
                🗓️ ${formatDate(deal.validFrom)} t/m ${formatDate(deal.validUntil)}
            </div>
        `;
        
        container.appendChild(card);
    });
}

// Vervang de setTimeout onderaan je app.js door dit:
fetch('./data.json')
    .then(response => response.json())
    .then(data => {
        // Sorteer op grootste besparing
        const sortedDeals = data.sort((a, b) => {
            return (b.normalPrice - b.dealPrice) - (a.normalPrice - a.dealPrice);
        });
        renderDeals(sortedDeals);
    })
    .catch(error => {
        console.error('Kon data niet laden:', error);
        document.getElementById('deals-container').innerHTML = '<p>Geen live data beschikbaar op dit moment.</p>';
    });
