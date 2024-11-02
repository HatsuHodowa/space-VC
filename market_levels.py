import json
from models.Asset import Asset
from models.Liability import Liability
from models.Job import Job
from numpy import random


def generate_earth_level():
    return {
        "assets": [
            Asset(name="House", value=random.randint(250000, 350000), income=1500, apr_mean=0.03, apr_std=0.01, liability=Liability(name="Mortgage", debt_amount=random.randint(150000, 250000), interest_rate=0.04, payoff_date=36)),
            Asset(name="Car", value=random.randint(15000, 25000), income=0, apr_mean=0.02, apr_std=0.005, liability=Liability(name="Car Loan", debt_amount=random.randint(10000, 20000), interest_rate=0.05, payoff_date=6)),
            Asset(name="Tech Stock", value=random.randint(8000, 12000), income=200, apr_mean=0.08, apr_std=0.2),
            Asset(name="Government Bond", value=random.randint(4000, 6000), income=100, apr_mean=0.03, apr_std=0.0),
            Asset(name="Farm Land", value=random.randint(40000, 60000), income=300, apr_mean=0.04, apr_std=0.015),
            Asset(name="Small Business", value=random.randint(70000, 80000), income=1000, apr_mean=0.06, apr_std=0.02),
            Asset(name="Earth Rocket", value=random.randint(450000, 550000), income=0, apr_mean=0.03, apr_std=0.01)
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
            Liability(name="Mortgage", debt_amount=random.randint(150000, 250000), interest_rate=0.04, payoff_date=18),
            Liability(name="Car Loan", debt_amount=random.randint(10000, 20000), interest_rate=0.05, payoff_date=6)
        ]
    }

def generate_moon_level():
    return {
        "assets": [
            Asset(name="Lunar Habitat", value=random.randint(350000, 450000), income=4000, apr_mean=0.04, apr_std=0.02, liability=Liability(name="Habitat Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, payoff_date=36)),
            Asset(name="Moon Mining Rights", value=random.randint(250000, 350000), income=5000, apr_mean=0.05, apr_std=0.02, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, payoff_date=18)),
            Asset(name="Lunar Solar Array", value=random.randint(120000, 180000), income=2000, apr_mean=0.05, apr_std=0.02),
            Asset(name="Lunar Water Extraction Facility", value=random.randint(220000, 280000), income=3500, apr_mean=0.06, apr_std=0.025),
            Asset(name="Lunar Research Lab", value=random.randint(300000, 400000), income=4500, apr_mean=0.04, apr_std=0.015),
            Asset(name="Moon Rocket", value=random.randint(950000, 1050000), income=0, apr_mean=0.03, apr_std=0.01)
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
            Liability(name="Habitat Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, payoff_date=24),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, payoff_date=18)
        ]
    }

def generate_venus_level():
    return {
        "assets": [
            Asset(name="Venus Dome", value=random.randint(350000, 450000), income=4000, apr_mean=0.04, apr_std=0.02, liability=Liability(name="Dome Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, payoff_date=36)),
            Asset(name="Atmosphere Mining Rights", value=random.randint(250000, 350000), income=5000, apr_mean=0.05, apr_std=0.02, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, payoff_date=18)),
            Asset(name="Solar Energy Array", value=random.randint(120000, 180000), income=2000, apr_mean=0.05, apr_std=0.02),
            Asset(name="Venus Water Extraction Facility", value=random.randint(220000, 280000), income=3500, apr_mean=0.06, apr_std=0.025),
            Asset(name="Venus Research Station", value=random.randint(300000, 400000), income=4500, apr_mean=0.04, apr_std=0.015),
            Asset(name="Venus Rocket", value=random.randint(950000, 1050000), income=0, apr_mean=0.03, apr_std=0.01)
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
            Liability(name="Dome Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, payoff_date=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, payoff_date=18)
        ]
    }

def generate_mars_level():
    return {
        "assets": [
            Asset(name="Mars Rover", value=random.randint(120000, 180000), income=500, apr_mean=0.03, apr_std=0.01, liability=Liability(name="Rover Loan", debt_amount=random.randint(80000, 120000), interest_rate=0.05, payoff_date=12)),
            Asset(name="Martian Colony Unit", value=random.randint(200000, 300000), income=3000, apr_mean=0.04, apr_std=0.02, liability=Liability(name="Colony Unit Mortgage", debt_amount=random.randint(150000, 250000), interest_rate=0.04, payoff_date=24)),
            Asset(name="Solar Farm", value=random.randint(80000, 120000), income=800, apr_mean=0.05, apr_std=0.015),
            Asset(name="Martian Mineral Rights", value=random.randint(100000, 150000), income=1500, apr_mean=0.06, apr_std=0.02),
            Asset(name="Martian Research Facility", value=random.randint(180000, 220000), income=2500, apr_mean=0.05, apr_std=0.02),
            Asset(name="Mars Rocket", value=random.randint(750000, 850000), income=0, apr_mean=0.03, apr_std=0.01)
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
            Liability(name="Rover Loan", debt_amount=random.randint(80000, 120000), interest_rate=0.05, payoff_date=12),
            Liability(name="Colony Unit Mortgage", debt_amount=random.randint(150000, 250000), interest_rate=0.04, payoff_date=24)
        ]
    }

def generate_mercury_level():
    return {
        "assets": [
            Asset(name="Mercury Habitat", value=random.randint(350000, 450000), income=4000, apr_mean=0.04, apr_std=0.02, liability=Liability(name="Habitat Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, payoff_date=36)),
            Asset(name="Mercury Mining Rights", value=random.randint(250000, 350000), income=5000, apr_mean=0.05, apr_std=0.02, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, payoff_date=18)),
            Asset(name="Mercurial Solar Array", value=random.randint(120000, 180000), income=2000, apr_mean=0.05, apr_std=0.02),
            Asset(name="Mercury Water Extraction Facility", value=random.randint(220000, 280000), income=3500, apr_mean=0.06, apr_std=0.025),
            Asset(name="Mercury Research Station", value=random.randint(300000, 400000), income=4500, apr_mean=0.04, apr_std=0.015),
            Asset(name="Mercury Rocket", value=random.randint(950000, 1050000), income=0, apr_mean=0.03, apr_std=0.01)
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
            Liability(name="Habitat Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, payoff_date=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, payoff_date=18)
        ]
    }

def generate_jupiter_level():
    return {
        "assets": [
            Asset(name="Jupiter Orbital Station", value=random.randint(350000, 450000), income=4000, apr_mean=0.04, apr_std=0.02, liability=Liability(name="Station Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, payoff_date=36)),
            Asset(name="Jovian Mining Rights", value=random.randint(250000, 350000), income=5000, apr_mean=0.05, apr_std=0.02, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, payoff_date=18)),
            Asset(name="Jupiter Solar Array", value=random.randint(120000, 180000), income=2000, apr_mean=0.05, apr_std=0.02),
            Asset(name="Jupiter Atmospheric Processor", value=random.randint(220000, 280000), income=3500, apr_mean=0.06, apr_std=0.025),
            Asset(name="Jupiter Research Lab", value=random.randint(300000, 400000), income=4500, apr_mean=0.04, apr_std=0.015),
            Asset(name="Jupiter Rocket", value=random.randint(950000, 1050000), income=0, apr_mean=0.03, apr_std=0.01)
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
            Liability(name="Station Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, payoff_date=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, payoff_date=18)
        ]
    }

def generate_saturn_level():
    return {
        "assets": [
            Asset(name="Saturn Orbital Station", value=random.randint(350000, 450000), income=4000, apr_mean=0.04, apr_std=0.02, liability=Liability(name="Station Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, payoff_date=36)),
            Asset(name="Titan Mining Rights", value=random.randint(250000, 350000), income=5000, apr_mean=0.05, apr_std=0.02, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, payoff_date=18)),
            Asset(name="Saturn Solar Array", value=random.randint(120000, 180000), income=2000, apr_mean=0.05, apr_std=0.02),
            Asset(name="Saturn Water Processing Facility", value=random.randint(220000, 280000), income=3500, apr_mean=0.06, apr_std=0.025),
            Asset(name="Saturn Research Lab", value=random.randint(300000, 400000), income=4500, apr_mean=0.04, apr_std=0.015),
            Asset(name="Saturn Rocket", value=random.randint(950000, 1050000), income=0, apr_mean=0.03, apr_std=0.01)
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
            Liability(name="Station Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, payoff_date=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, payoff_date=18)
        ]
    }

def generate_uranus_level():
    return {
        "assets": [
            Asset(name="Uranus Research Outpost", value=random.randint(350000, 450000), income=4000, apr_mean=0.04, apr_std=0.02, liability=Liability(name="Outpost Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, payoff_date=36)),
            Asset(name="Uranus Gas Mining Rights", value=random.randint(250000, 350000), income=5000, apr_mean=0.05, apr_std=0.02, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, payoff_date=18)),
            Asset(name="Uranus Solar Array", value=random.randint(120000, 180000), income=2000, apr_mean=0.05, apr_std=0.02),
            Asset(name="Uranus Water Extraction Facility", value=random.randint(220000, 280000), income=3500, apr_mean=0.06, apr_std=0.025),
            Asset(name="Uranus Research Lab", value=random.randint(300000, 400000), income=4500, apr_mean=0.04, apr_std=0.015),
            Asset(name="Uranus Rocket", value=random.randint(950000, 1050000), income=0, apr_mean=0.03, apr_std=0.01)
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
            Liability(name="Outpost Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, payoff_date=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, payoff_date=18)
        ]
    }

def generate_neptune_level():
    return {
        "assets": [
            Asset(name="Neptune Research Station", value=random.randint(350000, 450000), income=4000, apr_mean=0.04, apr_std=0.02, liability=Liability(name="Station Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, payoff_date=36)),
            Asset(name="Neptune Gas Mining Rights", value=random.randint(250000, 350000), income=5000, apr_mean=0.05, apr_std=0.02, liability=Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, payoff_date=18)),
            Asset(name="Neptune Solar Array", value=random.randint(120000, 180000), income=2000, apr_mean=0.05, apr_std=0.02),
            Asset(name="Neptune Water Processing Facility", value=random.randint(220000, 280000), income=3500, apr_mean=0.06, apr_std=0.025),
            Asset(name="Neptune Research Lab", value=random.randint(300000, 400000), income=4500, apr_mean=0.04, apr_std=0.015),
            Asset(name="Neptune Rocket", value=random.randint(950000, 1050000), income=0, apr_mean=0.03, apr_std=0.01)
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
            Liability(name="Station Mortgage", debt_amount=random.randint(250000, 350000), interest_rate=0.05, payoff_date=36),
            Liability(name="Mining Rights Loan", debt_amount=random.randint(150000, 250000), interest_rate=0.06, payoff_date=18)
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




