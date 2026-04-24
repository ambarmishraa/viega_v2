# data.py

from datetime import datetime, timedelta
import random

def generate_signals():

    companies = ["Rehau", "Geberit", "Uponor", "AquaSystems", "Watts Water"]

    signal_types = [
        "price_change",
        "feature_launch",
        "sustainability_initiative",
        "tech_partnership"
    ]

    domains = [
        "heating_cooling",
        "piping_systems",
        "pre_wall_technology",
        "industrial_piping"
    ]

    signals = []

    for _ in range(12):

        signal = {
            "company": random.choice(companies),
            "signal_type": random.choice(signal_types),
            "domain": random.choice(domains),
            "description": f"Auto generated event in {random.choice(domains)}",
            "impact_score": round(random.uniform(0.4, 0.95), 2),
            "timestamp": str(datetime.now() - timedelta(days=random.randint(0, 10))),
            "source_type": "synthetic"
        }

        signals.append(signal)

    return signals