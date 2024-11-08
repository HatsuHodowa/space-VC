import json
from models.Asset import Asset, AssetType
from models.Liability import Liability
from models.Job import Job
from numpy import random


def generate_earth_level(f):
    return {
        "images" : {
            "stats_tab" : "../View/backgrounds/unicorn space.jpg",
            "assets_tab" : "../View/backgrounds/assets.jpg",
            "liabilities_tab" : "../View/backgrounds/Liabilities.jpg",
            "asset_market_tab" : "../View/backgrounds/markets.jpg",
            "taxes_tab" : "../View/backgrounds/tax.jpg",
            "career_tab" : "../View/backgrounds/careers.jpg",
        },
        "assets": [
            Asset(name="House", value=random.randint(250000, 350000) * f, purchase_price=275000, income=1500, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY, liability=Liability(name="Mortgage", debt_amount=random.randint(150000, 250000), interest_rate=0.04, months_left=36)),
            Asset(name="Car", value=random.randint(15000, 25000) * f, purchase_price=20000, income=0, apr_mean=0.02, apr_std=0.005, asset_type=AssetType.PROPERTY, liability=Liability(name="Car Loan", debt_amount=random.randint(10000, 20000), interest_rate=0.05, months_left=6)),
            Asset(name="Tech Stock", value=random.randint(8000, 12000) * f, purchase_price=10000, income=200, apr_mean=0.08, apr_std=0.2, asset_type=AssetType.SECURITY),
            Asset(name="Government Bond", value=random.randint(4000, 6000) * f, purchase_price=5000, income=100, apr_mean=0.03, apr_std=0.0, asset_type=AssetType.SECURITY),
            Asset(name="Farm Land", value=random.randint(40000, 60000) * f, purchase_price=50000, income=300, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Small Business", value=random.randint(70000, 80000) * f, purchase_price=75000, income=1000, apr_mean=0.06, apr_std=0.02, asset_type=AssetType.BUSINESS),
            Asset(name="Earth Rocket", value=random.randint(450000, 550000) * f, purchase_price=500000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Aerospace Engineer", income=random.randint(60000, 120000))
        ],
        "liabilities": [
            Liability(name="Mortgage", debt_amount=random.randint(150000, 250000), interest_rate=0.04, months_left=18),
            Liability(name="Car Loan", debt_amount=random.randint(10000, 20000), interest_rate=0.05, months_left=6)
        ],
    }

def generate_moon_level(f):
    return {
        "images" : {
            "stats_tab" : "../View/backgrounds/unicorn space.jpg",
            "assets_tab" : "../View/backgrounds/assets.jpg",
            "liabilities_tab" : "../View/backgrounds/Liabilities.jpg",
            "asset_market_tab" : "../View/backgrounds/markets.jpg",
            "taxes_tab" : "../View/backgrounds/tax.jpg",
            "career_tab" : "../View/backgrounds/careers.jpg",
        },
        "assets": [
            Asset(name="Lunar Habitat", value=random.randint(350000, 450000) * f, purchase_price=400000, income=4000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Habitat Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, months_left=36)),
            Asset(name="Moon Mining Rights", value=random.randint(250000, 350000) * f, purchase_price=300000, income=5000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.SECURITY, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, months_left=18)),
            Asset(name="Lunar Solar Array", value=random.randint(120000, 180000) * f, purchase_price=150000, income=2000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Lunar Water Extraction Facility", value=random.randint(220000, 280000) * f, purchase_price=250000, income=3500, apr_mean=0.06, apr_std=0.025, asset_type=AssetType.PROPERTY),
            Asset(name="Lunar Research Lab", value=random.randint(300000, 400000) * f, purchase_price=350000, income=4500, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Moon Rocket", value=random.randint(950000, 1050000) * f, purchase_price=1000000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Lunar Engineer", income=random.randint(80000, 120000)),
            Job(title="Astrogeologist", income=random.randint(70000, 110000)),
            Job(title="Water Processing Technician", income=random.randint(60000, 90000)),
            Job(title="Solar Array Technician", income=random.randint(55000, 85000)),
            Job(title="Lunar Miner", income=random.randint(50000, 80000)),
            Job(title="Habitat Manager", income=random.randint(70000, 100000))
        ],
        "liabilities": [
            Liability(name="Habitat Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, months_left=24),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, months_left=18)
        ]
    }

def generate_venus_level(f):
    return {
        "images" : {
            "stats_tab" : "../View/backgrounds/unicorn space.jpg",
            "assets_tab" : "../View/backgrounds/assets.jpg",
            "liabilities_tab" : "../View/backgrounds/Liabilities.jpg",
            "asset_market_tab" : "../View/backgrounds/markets.jpg",
            "taxes_tab" : "../View/backgrounds/tax.jpg",
            "career_tab" : "../View/backgrounds/careers.jpg",
        },
        "assets": [
            Asset(name="Venus Dome", value=random.randint(350000, 450000) * f, purchase_price=400000, income=4000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Dome Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, months_left=36)),
            Asset(name="Atmosphere Mining Rights", value=random.randint(250000, 350000) * f, purchase_price=300000, income=5000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.SECURITY, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, months_left=18)),
            Asset(name="Solar Energy Array", value=random.randint(120000, 180000) * f, purchase_price=130000, income=2000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Venus Water Extraction Facility", value=random.randint(220000, 280000) * f, purchase_price=250000, income=3500, apr_mean=0.06, apr_std=0.025, asset_type=AssetType.PROPERTY),
            Asset(name="Venus Research Station", value=random.randint(300000, 400000) * f, purchase_price=350000, income=4500, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Venus Rocket", value=random.randint(950000, 1050000) * f, purchase_price=1000000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Atmospheric Processor Engineer", income=random.randint(80000, 120000)),
            Job(title="Astrobiologist", income=random.randint(70000, 110000)),
            Job(title="Solar Energy Specialist", income=random.randint(60000, 100000)),
            Job(title="Mining Operator", income=random.randint(60000, 90000)),
            Job(title="Venus Dome Supervisor", income=random.randint(75000, 110000)),
            Job(title="Water Extraction Technician", income=random.randint(55000, 85000))
        ],
        "liabilities": [
            Liability(name="Dome Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, months_left=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, months_left=18)
        ]
    }

def generate_mars_level(f):
    return {
        "images" : {
            "stats_tab" : "../View/backgrounds/unicorn space.jpg",
            "assets_tab" : "../View/backgrounds/assets.jpg",
            "liabilities_tab" : "../View/backgrounds/Liabilities.jpg",
            "asset_market_tab" : "../View/backgrounds/markets.jpg",
            "taxes_tab" : "../View/backgrounds/tax.jpg",
            "career_tab" : "../View/backgrounds/careers.jpg",
        },
        "assets": [
            Asset(name="Mars Rover", value=random.randint(120000, 180000) * f, purchase_price=150000, income=500, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY, liability=Liability(name="Rover Loan", debt_amount=random.randint(80000, 120000), interest_rate=0.05, months_left=12)),
            Asset(name="Martian Colony Unit", value=random.randint(200000, 300000) * f, purchase_price=250000, income=3000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Colony Unit Mortgage", debt_amount=random.randint(150000, 250000), interest_rate=0.04, months_left=24)),
            Asset(name="Solar Farm", value=random.randint(80000, 120000) * f, purchase_price=90000, income=800, apr_mean=0.05, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Martian Mineral Rights", value=random.randint(100000, 150000) * f, purchase_price=120000, income=1500, apr_mean=0.06, apr_std=0.02, asset_type=AssetType.SECURITY),
            Asset(name="Martian Research Facility", value=random.randint(180000, 220000) * f, purchase_price=200000, income=2500, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Mars Rocket", value=random.randint(750000, 850000) * f, purchase_price=800000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Rover Technician", income=random.randint(65000, 90000)),
            Job(title="Martian Geologist", income=random.randint(70000, 110000)),
            Job(title="Solar Farm Manager", income=random.randint(60000, 95000)),
            Job(title="Mineral Extraction Specialist", income=random.randint(75000, 100000)),
            Job(title="Colony Unit Supervisor", income=random.randint(80000, 120000)),
            Job(title="Mars Research Scientist", income=random.randint(85000, 125000))
        ],
        "liabilities": [
            Liability(name="Rover Loan", debt_amount=random.randint(80000, 120000), interest_rate=0.05, months_left=12),
            Liability(name="Colony Unit Mortgage", debt_amount=random.randint(150000, 250000), interest_rate=0.04, months_left=24)
        ]
    }

def generate_mercury_level(f):
    return {
        "images" : {
            "stats_tab" : "../View/backgrounds/unicorn space.jpg",
            "assets_tab" : "../View/backgrounds/assets.jpg",
            "liabilities_tab" : "../View/backgrounds/Liabilities.jpg",
            "asset_market_tab" : "../View/backgrounds/markets.jpg",
            "taxes_tab" : "../View/backgrounds/tax.jpg",
            "career_tab" : "../View/backgrounds/careers.jpg",
        },
        "assets": [
            Asset(name="Mercury Habitat", value=random.randint(350000, 450000) * f, purchase_price=425000, income=4000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Habitat Mortgage", debt_amount=random.randint(250000, 350000) * f, interest_rate=0.05, months_left=36)),
            Asset(name="Mercury Mining Rights", value=random.randint(250000, 350000) * f, purchase_price=275000, income=5000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.SECURITY, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000) * f, interest_rate=0.06, months_left=18)),
            Asset(name="Mercurial Solar Array", value=random.randint(120000, 180000) * f, purchase_price=140000, income=2000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Mercury Water Extraction Facility", value=random.randint(220000, 280000) * f, purchase_price=240000, income=3500, apr_mean=0.06, apr_std=0.025, asset_type=AssetType.PROPERTY),
            Asset(name="Mercury Research Station", value=random.randint(300000, 400000) * f, purchase_price=350000, income=4500, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Mercury Rocket", value=random.randint(950000, 1050000) * f, purchase_price=975000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Solar Technician", income=random.randint(70000, 110000)),
            Job(title="Mining Engineer", income=random.randint(80000, 120000)),
            Job(title="Atmospheric Scientist", income=random.randint(70000, 100000)),
            Job(title="Water Processing Specialist", income=random.randint(75000, 105000)),
            Job(title="Mercury Habitat Manager", income=random.randint(90000, 130000)),
            Job(title="Geologist", income=random.randint(75000, 115000))
        ],
        "liabilities": [
            Liability(name="Habitat Mortgage", debt_amount=random.randint(250000, 350000) * f, interest_rate=0.05, months_left=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000) * f, interest_rate=0.06, months_left=18)
        ]
    }

def generate_jupiter_level(f):
    return {
        "images" : {
            "stats_tab" : "../View/backgrounds/unicorn space.jpg",
            "assets_tab" : "../View/backgrounds/assets.jpg",
            "liabilities_tab" : "../View/backgrounds/Liabilities.jpg",
            "asset_market_tab" : "../View/backgrounds/markets.jpg",
            "taxes_tab" : "../View/backgrounds/tax.jpg",
            "career_tab" : "../View/backgrounds/careers.jpg",
        },
        "assets": [
            Asset(name="Jupiter Orbital Station", value=random.randint(350000, 450000) *f, purchase_price=440000, income=4000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Station Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, months_left=36)),
            Asset(name="Jovian Mining Rights", value=random.randint(250000, 350000) *f, purchase_price=320000, income=5000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.SECURITY, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, months_left=18)),
            Asset(name="Jupiter Solar Array", value=random.randint(120000, 180000) *f, purchase_price=160000, income=2000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Jupiter Atmospheric Processor", value=random.randint(220000, 280000) *f, purchase_price=260000, income=3500, apr_mean=0.06, apr_std=0.025, asset_type=AssetType.PROPERTY),
            Asset(name="Jupiter Research Lab", value=random.randint(300000, 400000) *f, purchase_price=380000, income=4500, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Jupiter Rocket", value=random.randint(950000, 1050000) *f, purchase_price=1025000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Orbital Engineer", income=random.randint(80000, 130000)),
            Job(title="Atmosphere Processor Technician", income=random.randint(70000, 110000)),
            Job(title="Gas Mining Specialist", income=random.randint(85000, 125000)),
            Job(title="Solar Array Engineer", income=random.randint(75000, 115000)),
            Job(title="Orbital Station Manager", income=random.randint(90000, 140000)),
            Job(title="Research Scientist", income=random.randint(95000, 130000))
        ],
        "liabilities": [
            Liability(name="Station Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, months_left=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, months_left=18)
        ]
    }

def generate_saturn_level(f):
    return {
        "images" : {
            "stats_tab" : "../View/backgrounds/unicorn space.jpg",
            "assets_tab" : "../View/backgrounds/assets.jpg",
            "liabilities_tab" : "../View/backgrounds/Liabilities.jpg",
            "asset_market_tab" : "../View/backgrounds/markets.jpg",
            "taxes_tab" : "../View/backgrounds/tax.jpg",
            "career_tab" : "../View/backgrounds/careers.jpg",
        },
        "assets": [
            Asset(name="Saturn Orbital Station", value=random.randint(350000, 450000) *f, purchase_price=425000, income=4000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Station Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, months_left=36)),
            Asset(name="Titan Mining Rights", value=random.randint(250000, 350000) *f, purchase_price=300000, income=5000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.SECURITY, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, months_left=18)),
            Asset(name="Saturn Solar Array", value=random.randint(120000, 180000)*f, purchase_price=135000, income=2000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Saturn Water Processing Facility", value=random.randint(220000, 280000)*f, purchase_price=250000, income=3500, apr_mean=0.06, apr_std=0.025, asset_type=AssetType.PROPERTY),
            Asset(name="Saturn Research Lab", value=random.randint(300000, 400000)*f, purchase_price=350000, income=4500, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Saturn Rocket", value=random.randint(950000, 1050000)*f, purchase_price=1000000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Orbital Habitat Engineer", income=random.randint(80000, 130000)),
            Job(title="Cryogenic Mining Specialist", income=random.randint(90000, 135000)),
            Job(title="Solar Array Operator", income=random.randint(75000, 110000)),
            Job(title="Water Processing Technician", income=random.randint(70000, 105000)),
            Job(title="Orbital Station Supervisor", income=random.randint(90000, 140000)),
            Job(title="Planetary Scientist", income=random.randint(95000, 130000))
        ],
        "liabilities": [
            Liability(name="Station Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, months_left=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, months_left=18)
        ]
    }

def generate_uranus_level(f):
    return {
        "images" : {
            "stats_tab" : "../View/backgrounds/unicorn space.jpg",
            "assets_tab" : "../View/backgrounds/assets.jpg",
            "liabilities_tab" : "../View/backgrounds/Liabilities.jpg",
            "asset_market_tab" : "../View/backgrounds/markets.jpg",
            "taxes_tab" : "../View/backgrounds/tax.jpg",
            "career_tab" : "../View/backgrounds/careers.jpg",
        },
        "assets": [
            Asset(name="Uranus Research Outpost", value=random.randint(350000, 450000)*f, purchase_price=400000, income=4000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Outpost Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, months_left=36)),
            Asset(name="Uranus Gas Mining Rights", value=random.randint(250000, 350000)*f, purchase_price=275000, income=5000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.SECURITY, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, months_left=18)),
            Asset(name="Uranus Solar Array", value=random.randint(120000, 180000)*f, purchase_price=130000, income=2000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Uranus Water Extraction Facility", value=random.randint(220000, 280000)*f, purchase_price=240000, income=3500, apr_mean=0.06, apr_std=0.025, asset_type=AssetType.PROPERTY),
            Asset(name="Uranus Research Lab", value=random.randint(300000, 400000)*f, purchase_price=320000, income=4500, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Uranus Rocket", value=random.randint(950000, 1050000)*f, purchase_price=975000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Cryogenic Fuel Technician", income=random.randint(85000, 130000)),
            Job(title="Gas Mining Engineer", income=random.randint(90000, 135000)),
            Job(title="Research Scientist", income=random.randint(95000, 140000)),
            Job(title="Solar Panel Technician", income=random.randint(75000, 115000)),
            Job(title="Orbital Outpost Manager", income=random.randint(95000, 140000)),
            Job(title="Water Extraction Specialist", income=random.randint(85000, 125000))
        ],
        "liabilities": [
            Liability(name="Outpost Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, months_left=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, months_left=18)
        ]
    }

def generate_neptune_level(f):
    return {
        "images" : {
            "stats_tab" : "../View/backgrounds/unicorn space.jpg",
            "assets_tab" : "../View/backgrounds/assets.jpg",
            "liabilities_tab" : "../View/backgrounds/Liabilities.jpg",
            "asset_market_tab" : "../View/backgrounds/markets.jpg",
            "taxes_tab" : "../View/backgrounds/tax.jpg",
            "career_tab" : "../View/backgrounds/careers.jpg",
        },
        "assets": [
            Asset(name="Neptune Research Station", value=random.randint(350000, 450000)*f, purchase_price=425000, income=4000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Station Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, months_left=36)),
            Asset(name="Neptune Gas Mining Rights", value=random.randint(250000, 350000)*f, purchase_price=300000, income=5000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.SECURITY, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, months_left=18)),
            Asset(name="Neptune Solar Array", value=random.randint(120000, 180000)*f, purchase_price=140000, income=2000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Neptune Water Processing Facility", value=random.randint(220000, 280000)*f, purchase_price=245000, income=3500, apr_mean=0.06, apr_std=0.025, asset_type=AssetType.PROPERTY),
            Asset(name="Neptune Research Lab", value=random.randint(300000, 400000)*f, purchase_price=360000, income=4500, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Neptune Rocket", value=random.randint(950000, 1050000)*f, purchase_price=1000000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Deep Space Miner", income=random.randint(95000, 140000)),
            Job(title="Cryogenic Systems Engineer", income=random.randint(90000, 135000)),
            Job(title="Research Scientist", income=random.randint(95000, 145000)),
            Job(title="Atmospheric Chemist", income=random.randint(85000, 125000)),
            Job(title="Orbital Station Manager", income=random.randint(95000, 145000)),
            Job(title="Gas Extraction Specialist", income=random.randint(95000, 130000))
        ],
        "liabilities": [
            Liability(name="Station Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, months_left=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, months_left=18)
        ]
    }

# Dictionary containing all levels
levels = {
    "Earth": generate_earth_level(1),
    "Moon": generate_moon_level(3),
    "Venus": generate_venus_level(9),
    "Mars": generate_mars_level(27),
    "Mercury": generate_mercury_level(81),
    "Jupiter": generate_jupiter_level(243),
    "Saturn": generate_saturn_level(729),
    "Uranus": generate_uranus_level(3000),
    "Neptune": generate_neptune_level(100000)
}

serializable_levels = {
    level_name: {
        "images": data["images"],
        "assets": [asset.to_dict() for asset in data["assets"]],
        "careers": [job.to_dict() for job in data["careers"]],
        "liabilities": [liability.to_dict() for liability in data["liabilities"]]
    }
    for level_name, data in levels.items()
}


with open("game_data.json", "w") as file:
    json.dump(serializable_levels, file, indent=4)




