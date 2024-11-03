import json
from models.Asset import Asset, AssetType
from models.Liability import Liability
from models.Job import Job
from numpy import random


def generate_earth_level():
    return {
        "assets": [
            Asset(name="House", value=random.randint(250000, 350000), purchase_price=275000, income=1500, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY, liability=Liability(name="Mortgage", debt_amount=random.randint(150000, 250000), interest_rate=0.04, months_left=36)),
            Asset(name="Car", value=random.randint(15000, 25000), purchase_price=20000, income=0, apr_mean=0.02, apr_std=0.005, asset_type=AssetType.PROPERTY, liability=Liability(name="Car Loan", debt_amount=random.randint(10000, 20000), interest_rate=0.05, months_left=6)),
            Asset(name="Tech Stock", value=random.randint(8000, 12000), purchase_price=10000, income=200, apr_mean=0.08, apr_std=0.2, asset_type=AssetType.SECURITY),
            Asset(name="Government Bond", value=random.randint(4000, 6000), purchase_price=5000, income=100, apr_mean=0.03, apr_std=0.0, asset_type=AssetType.SECURITY),
            Asset(name="Farm Land", value=random.randint(40000, 60000), purchase_price=50000, income=300, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Small Business", value=random.randint(70000, 80000), purchase_price=75000, income=1000, apr_mean=0.06, apr_std=0.02, asset_type=AssetType.BUSINESS),
            Asset(name="Earth Rocket", value=random.randint(450000, 550000), purchase_price=500000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Software Engineer", income=random.randint(60000, 120000)),
            Job(title="Doctor", income=random.randint(80000, 150000)),
            Job(title="Agricultural Scientist", income=random.randint(50000, 90000)),
            Job(title="Construction Worker", income=random.randint(40000, 70000)),
            Job(title="Small Business Owner", income=random.randint(30000, 80000)),
            Job(title="Stock Trader", income=random.randint(50000, 100000))
        ],
        "liabilities": [
            Liability(name="Mortgage", debt_amount=random.randint(150000, 250000), interest_rate=0.04, months_left=18),
            Liability(name="Car Loan", debt_amount=random.randint(10000, 20000), interest_rate=0.05, months_left=6)
        ]
    }

def generate_moon_level():
    return {
        "assets": [
            Asset(name="Lunar Habitat", value=random.randint(3500000, 4500000), purchase_price=400000, income=4000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Habitat Mortgage", debt_amount=random.randint(2500000, 3500000), interest_rate=0.05, months_left=36)),
            Asset(name="Moon Mining Rights", value=random.randint(2500000, 3500000), purchase_price=300000, income=5000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.SECURITY, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(1500000, 2500000), interest_rate=0.06, months_left=18)),
            Asset(name="Lunar Solar Array", value=random.randint(1200000, 1800000), purchase_price=150000, income=2000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Lunar Water Extraction Facility", value=random.randint(2200000, 280000), purchase_price=250000, income=3500, apr_mean=0.06, apr_std=0.025, asset_type=AssetType.PROPERTY),
            Asset(name="Lunar Research Lab", value=random.randint(3000000, 4000000), purchase_price=350000, income=4500, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Moon Rocket", value=random.randint(9500000, 10500000), purchase_price=1000000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Lunar Engineer", income=random.randint(800000, 1200000)),
            Job(title="Astrogeologist", income=random.randint(700000, 1100000)),
            Job(title="Water Processing Technician", income=random.randint(600000, 900000)),
            Job(title="Solar Array Technician", income=random.randint(550000, 850000)),
            Job(title="Lunar Miner", income=random.randint(500000, 800000)),
            Job(title="Habitat Manager", income=random.randint(700000, 1000000))
        ],
        "liabilities": [
            Liability(name="Habitat Mortgage", debt_amount=random.randint(2500000, 3500000), interest_rate=0.05, months_left=24),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(1500000, 2500000), interest_rate=0.06, months_left=18)
        ]
    }

def generate_venus_level():
    return {
        "assets": [
            Asset(name="Venus Dome", value=random.randint(35000000, 45000000), purchase_price=400000, income=4000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Dome Mortgage", debt_amount=random.randint(25000000, 35000000), interest_rate=0.05, months_left=36)),
            Asset(name="Atmosphere Mining Rights", value=random.randint(25000000, 35000000), purchase_price=300000, income=5000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.SECURITY, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(15000000, 25000000), interest_rate=0.06, months_left=18)),
            Asset(name="Solar Energy Array", value=random.randint(12000000, 18000000), purchase_price=130000, income=2000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Venus Water Extraction Facility", value=random.randint(22000000, 28000000), purchase_price=250000, income=3500, apr_mean=0.06, apr_std=0.025, asset_type=AssetType.PROPERTY),
            Asset(name="Venus Research Station", value=random.randint(30000000, 40000000), purchase_price=35000000, income=4500, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Venus Rocket", value=random.randint(95000000, 105000000), purchase_price=1000000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Atmospheric Processor Engineer", income=random.randint(800000, 12000000)),
            Job(title="Astrobiologist", income=random.randint(7000000, 11000000)),
            Job(title="Solar Energy Specialist", income=random.randint(6000000, 10000000)),
            Job(title="Mining Operator", income=random.randint(6000000, 900000)),
            Job(title="Venus Dome Supervisor", income=random.randint(7500000, 11000000)),
            Job(title="Water Extraction Technician", income=random.randint(5500000, 8500000))
        ],
        "liabilities": [
            Liability(name="Dome Mortgage", debt_amount=random.randint(25000000, 35000000), interest_rate=0.05, months_left=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(15000000, 25000000), interest_rate=0.06, months_left=18)
        ]
    }

def generate_mars_level():
    return {
        "assets": [
            Asset(name="Mars Rover", value=random.randint(120000000, 180000000), purchase_price=150000, income=500, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY, liability=Liability(name="Rover Loan", debt_amount=random.randint(80000000, 120000000), interest_rate=0.05, months_left=12)),
            Asset(name="Martian Colony Unit", value=random.randint(200000000, 300000000), purchase_price=250000, income=3000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Colony Unit Mortgage", debt_amount=random.randint(150000000, 250000000), interest_rate=0.04, months_left=24)),
            Asset(name="Solar Farm", value=random.randint(80000000, 120000000), purchase_price=90000, income=800, apr_mean=0.05, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Martian Mineral Rights", value=random.randint(100000000, 150000000), purchase_price=120000, income=1500, apr_mean=0.06, apr_std=0.02, asset_type=AssetType.SECURITY),
            Asset(name="Martian Research Facility", value=random.randint(180000000, 220000000), purchase_price=200000, income=2500, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Mars Rocket", value=random.randint(750000000, 850000000), purchase_price=800000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Rover Technician", income=random.randint(65000000, 90000000)),
            Job(title="Martian Geologist", income=random.randint(70000000, 110000000)),
            Job(title="Solar Farm Manager", income=random.randint(60000000, 95000000)),
            Job(title="Mineral Extraction Specialist", income=random.randint(75000000, 100000000)),
            Job(title="Colony Unit Supervisor", income=random.randint(80000000, 120000000)),
            Job(title="Mars Research Scientist", income=random.randint(85000000, 125000000))
        ],
        "liabilities": [
            Liability(name="Rover Loan", debt_amount=random.randint(80000000, 120000000), interest_rate=0.05, months_left=12),
            Liability(name="Colony Unit Mortgage", debt_amount=random.randint(150000000, 250000000), interest_rate=0.04, months_left=24)
        ]
    }

def generate_mercury_level():
    return {
        "assets": [
            Asset(name="Mercury Habitat", value=random.randint(3500000000, 4500000000), purchase_price=425000, income=4000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Habitat Mortgage", debt_amount=random.randint(2500000000, 3500000000), interest_rate=0.05, months_left=36)),
            Asset(name="Mercury Mining Rights", value=random.randint(2500000000, 3500000000), purchase_price=275000, income=5000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.SECURITY, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(1500000000, 2500000000), interest_rate=0.06, months_left=18)),
            Asset(name="Mercurial Solar Array", value=random.randint(1200000000, 1800000000), purchase_price=140000, income=2000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Mercury Water Extraction Facility", value=random.randint(2200000000, 2800000000), purchase_price=240000, income=3500, apr_mean=0.06, apr_std=0.025, asset_type=AssetType.PROPERTY),
            Asset(name="Mercury Research Station", value=random.randint(3000000000, 4000000000), purchase_price=350000, income=4500, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Mercury Rocket", value=random.randint(9500000000, 10500000000), purchase_price=975000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Solar Technician", income=random.randint(700000000, 1100000000)),
            Job(title="Mining Engineer", income=random.randint(800000000, 1200000000)),
            Job(title="Atmospheric Scientist", income=random.randint(700000000, 1000000000)),
            Job(title="Water Processing Specialist", income=random.randint(750000000, 1050000000)),
            Job(title="Mercury Habitat Manager", income=random.randint(900000000, 1300000000)),
            Job(title="Geologist", income=random.randint(750000000, 1150000000))
        ],
        "liabilities": [
            Liability(name="Habitat Mortgage", debt_amount=random.randint(2500000000, 3500000000), interest_rate=0.05, months_left=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(1500000000, 2500000000), interest_rate=0.06, months_left=18)
        ]
    }

def generate_jupiter_level():
    return {
        "assets": [
            Asset(name="Jupiter Orbital Station", value=random.randint(35000000000000000, 45000000000000000), purchase_price=440000, income=4000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Station Mortgage", debt_amount=random.randint(25000000000000000, 35000000000000000), interest_rate=0.05, months_left=36)),
            Asset(name="Jovian Mining Rights", value=random.randint(25000000000000000, 35000000000000000), purchase_price=320000, income=5000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.SECURITY, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(15000000000000000, 25000000000000000), interest_rate=0.06, months_left=18)),
            Asset(name="Jupiter Solar Array", value=random.randint(12000000000000000, 18000000000000000), purchase_price=160000, income=2000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Jupiter Atmospheric Processor", value=random.randint(22000000000000000, 28000000000000000), purchase_price=260000, income=3500, apr_mean=0.06, apr_std=0.025, asset_type=AssetType.PROPERTY),
            Asset(name="Jupiter Research Lab", value=random.randint(30000000000000000, 40000000000000000), purchase_price=380000, income=4500, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Jupiter Rocket", value=random.randint(95000000000000000, 105000000000000000), purchase_price=1025000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Orbital Engineer", income=random.randint(8000000000000000, 13000000000000000)),
            Job(title="Atmosphere Processor Technician", income=random.randint(7000000000000000, 11000000000000000)),
            Job(title="Gas Mining Specialist", income=random.randint(8500000000000000, 12500000000000000)),
            Job(title="Solar Array Engineer", income=random.randint(7500000000000000, 11500000000000000)),
            Job(title="Orbital Station Manager", income=random.randint(9000000000000000, 14000000000000000)),
            Job(title="Research Scientist", income=random.randint(9500000000000000, 13000000000000000))
        ],
        "liabilities": [
            Liability(name="Station Mortgage", debt_amount=random.randint(25000000000000000, 35000000000000000), interest_rate=0.05, months_left=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(15000000000000000, 25000000000000000), interest_rate=0.06, months_left=18)
        ]
    }

def generate_saturn_level():
    return {
        "assets": [
            Asset(name="Saturn Orbital Station", value=random.randint(350000000000, 450000000000), purchase_price=425000, income=4000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Station Mortgage", debt_amount=random.randint(250000000000, 350000000000), interest_rate=0.05, months_left=36)),
            Asset(name="Titan Mining Rights", value=random.randint(250000000000, 350000000000), purchase_price=300000, income=5000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.SECURITY, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000000000, 250000000000), interest_rate=0.06, months_left=18)),
            Asset(name="Saturn Solar Array", value=random.randint(120000000000, 180000000000), purchase_price=135000, income=2000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Saturn Water Processing Facility", value=random.randint(220000000000, 280000000000), purchase_price=250000, income=3500, apr_mean=0.06, apr_std=0.025, asset_type=AssetType.PROPERTY),
            Asset(name="Saturn Research Lab", value=random.randint(300000000000, 400000000000), purchase_price=350000, income=4500, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Saturn Rocket", value=random.randint(950000000000, 1050000000000), purchase_price=1000000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Orbital Habitat Engineer", income=random.randint(80000000000, 130000000000)),
            Job(title="Cryogenic Mining Specialist", income=random.randint(90000000000, 135000000000)),
            Job(title="Solar Array Operator", income=random.randint(75000000000, 110000000000)),
            Job(title="Water Processing Technician", income=random.randint(70000000000, 105000000000)),
            Job(title="Orbital Station Supervisor", income=random.randint(90000000000, 140000000000)),
            Job(title="Planetary Scientist", income=random.randint(95000000000, 130000000000))
        ],
        "liabilities": [
            Liability(name="Station Mortgage", debt_amount=random.randint(25000000000, 35000000000), interest_rate=0.05, months_left=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000000000, 250000000000), interest_rate=0.06, months_left=18)
        ]
    }

def generate_uranus_level():
    return {
        "assets": [
            Asset(name="Uranus Research Outpost", value=random.randint(350000000000, 450000000000), purchase_price=400000, income=4000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Outpost Mortgage", debt_amount=random.randint(250000000000, 350000000000), interest_rate=0.05, months_left=36)),
            Asset(name="Uranus Gas Mining Rights", value=random.randint(250000000000, 350000000000), purchase_price=275000, income=5000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.SECURITY, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000000000, 250000000000), interest_rate=0.06, months_left=18)),
            Asset(name="Uranus Solar Array", value=random.randint(120000000000, 180000000000), purchase_price=130000, income=2000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Uranus Water Extraction Facility", value=random.randint(220000000000, 280000000000), purchase_price=240000, income=3500, apr_mean=0.06, apr_std=0.025, asset_type=AssetType.PROPERTY),
            Asset(name="Uranus Research Lab", value=random.randint(300000000000, 400000000000), purchase_price=320000, income=4500, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Uranus Rocket", value=random.randint(950000000000, 1050000000000), purchase_price=975000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Cryogenic Fuel Technician", income=random.randint(85000000000, 130000000000)),
            Job(title="Gas Mining Engineer", income=random.randint(90000000000, 135000000000)),
            Job(title="Research Scientist", income=random.randint(95000000000, 140000000000)),
            Job(title="Solar Panel Technician", income=random.randint(75000000000, 115000000000)),
            Job(title="Orbital Outpost Manager", income=random.randint(95000000000, 140000000000)),
            Job(title="Water Extraction Specialist", income=random.randint(85000000000, 125000000000))
        ],
        "liabilities": [
            Liability(name="Outpost Mortgage", debt_amount=random.randint(250000000000, 350000000000), interest_rate=0.05, months_left=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000000000, 250000000000), interest_rate=0.06, months_left=18)
        ]
    }

def generate_neptune_level():
    return {
        "assets": [
            Asset(name="Neptune Research Station", value=random.randint(350000000000, 450000000000), purchase_price=425000, income=4000, apr_mean=0.04, apr_std=0.02, asset_type=AssetType.PROPERTY, liability=Liability(name="Station Mortgage", debt_amount=random.randint(250000000000, 350000000000), interest_rate=0.05, months_left=36)),
            Asset(name="Neptune Gas Mining Rights", value=random.randint(250000000000, 350000000000), purchase_price=300000, income=5000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.SECURITY, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000000000, 250000000000), interest_rate=0.06, months_left=18)),
            Asset(name="Neptune Solar Array", value=random.randint(120000000000, 180000000000), purchase_price=140000, income=2000, apr_mean=0.05, apr_std=0.02, asset_type=AssetType.PROPERTY),
            Asset(name="Neptune Water Processing Facility", value=random.randint(220000000000, 280000000000), purchase_price=245000, income=3500, apr_mean=0.06, apr_std=0.025, asset_type=AssetType.PROPERTY),
            Asset(name="Neptune Research Lab", value=random.randint(300000000000, 400000000000), purchase_price=360000, income=4500, apr_mean=0.04, apr_std=0.015, asset_type=AssetType.PROPERTY),
            Asset(name="Neptune Rocket", value=random.randint(950000000000, 1050000000000), purchase_price=1000000, income=0, apr_mean=0.03, apr_std=0.01, asset_type=AssetType.PROPERTY)
        ],
        "careers": [
            Job(title="Deep Space Miner", income=random.randint(95000000000, 140000000000)),
            Job(title="Cryogenic Systems Engineer", income=random.randint(90000000000, 135000000000)),
            Job(title="Research Scientist", income=random.randint(95000000000, 145000000000)),
            Job(title="Atmospheric Chemist", income=random.randint(85000000000, 125000000000)),
            Job(title="Orbital Station Manager", income=random.randint(95000000000, 145000)),
            Job(title="Gas Extraction Specialist", income=random.randint(95000000000, 130000000000))
        ],
        "liabilities": [
            Liability(name="Station Mortgage", debt_amount=random.randint(250000000000, 350000000000), interest_rate=0.05, months_left=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000000000, 250000000000), interest_rate=0.06, months_left=18)
        ]
    }

# Dictionary containing all levels
levels = {
    "Earth": generate_earth_level(),
    "Moon": generate_moon_level(),
    "Venus": generate_venus_level(),
    "Mars": generate_mars_level(),
    "Mercury": generate_mercury_level(),
    "Jupiter": generate_jupiter_level(),
    "Saturn": generate_saturn_level(),
    "Uranus": generate_uranus_level(),
    "Neptune": generate_neptune_level()
}

serializable_levels = {
    level_name: {
        "assets": [asset.to_dict() for asset in data["assets"]],
        "careers": [job.to_dict() for job in data["careers"]],
        "liabilities": [liability.to_dict() for liability in data["liabilities"]]
    }
    for level_name, data in levels.items()
}


with open("game_data.json", "w") as file:
    json.dump(serializable_levels, file, indent=4)




