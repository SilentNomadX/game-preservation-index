games = [
    {
        "title": "God of War",
        "release_year": 2018,
        "platform": "PlayStation 4",
        "physical_availability": 8,
        "digital_availability": 10,
        "hardware_dependency": 8,
        "documentation": 7,
        "community_activity": 9
    },
    {
        "title": "The Simpsons: Hit & Run",
        "release_year": 2003,
        "platform": "PlayStation 2",
        "physical_availability": 4,
        "digital_availability": 0,
        "hardware_dependency": 4,
        "documentation": 5,
        "community_activity": 8
    },
    {
        "title": "P.T.",
        "release_year": 2014,
        "platform": "PlayStation 4",
        "physical_availability": 0,
        "digital_availability": 0,
        "hardware_dependency": 2,
        "documentation": 6,
        "community_activity": 9
    }
]

print("Game Preservation Index")
print("-----------------------")

for game in games:
    total_score = (
        game["physical_availability"]
        + game["digital_availability"]
        + game["hardware_dependency"]
        + game["documentation"]
        + game["community_activity"]
    )

    max_score = 50
    gpi_score = (total_score / max_score) * 100

    if gpi_score >= 75:
        risk_level = "Low Risk"
    elif gpi_score >= 50:
        risk_level = "Medium Risk"
    elif gpi_score >= 25:
        risk_level = "High Risk"
    else:
        risk_level = "Critical Risk"

    print()
    print("Game:", game["title"])
    print("Year:", game["release_year"])
    print("Platform:", game["platform"])
    print("GPI Score:", gpi_score, "%")
    print("Risk Level:", risk_level)