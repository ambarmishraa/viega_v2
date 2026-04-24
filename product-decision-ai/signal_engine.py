import random
from datetime import datetime, timedelta

COMPANIES = ["Rehau", "Geberit", "Uponor", "AquaSystems", "Watts Water"]

DOMAINS = [
    "heating_cooling",
    "piping_systems",
    "pre_wall_technology",
    "industrial_piping"
]

SIGNAL_TYPES = [
    "price_change",
    "feature_launch",
    "sustainability_initiative",
    "tech_partnership"
]


def generate_signals(n=10):
    signals = []

    for _ in range(n):
        company = random.choice(COMPANIES)
        domain = random.choice(DOMAINS)
        signal_type = random.choice(SIGNAL_TYPES)

        impact_score = round(random.uniform(0.4, 0.95), 2)

        description_map = {
            "price_change": f"Adjusted pricing strategy for {domain} products",
            "feature_launch": f"Launched new {domain} system improving efficiency",
            "sustainability_initiative": f"Introduced eco-friendly materials in {domain}",
            "tech_partnership": f"Partnered with university for next-gen {domain} solutions"
        }

        signals.append({
            "company": company,
            "signal_type": signal_type,
            "domain": domain,
            "description": description_map[signal_type],
            "impact_score": impact_score,
            "timestamp": str(datetime.now() - timedelta(days=random.randint(1, 30))),
            "source_type": "synthetic"
        })

    return signals