games = [
    {
        "title": "God of War",
        "release_year": 2018,
        "platform": "PlayStation 4 / PC",
        "playable_access": 90,
        "platform_dependency": 85,
        "documentation": 75,
        "technical_preservation": 40,
        "community_preservation": 90,
        "cultural_value": 85,
        "evidence_note": "Widely available on modern platforms, but source code and deeper technical materials are not publicly available."
    },
    {
        "title": "The Simpsons: Hit & Run",
        "release_year": 2003,
        "platform": "PlayStation 2 / Xbox / GameCube / PC",
        "playable_access": 35,
        "platform_dependency": 45,
        "documentation": 55,
        "technical_preservation": 35,
        "community_preservation": 85,
        "cultural_value": 80,
        "evidence_note": "No modern digital release, but strong fan interest and community preservation keep it visible."
    },
    {
        "title": "P.T.",
        "release_year": 2014,
        "platform": "PlayStation 4",
        "playable_access": 5,
        "platform_dependency": 10,
        "documentation": 65,
        "technical_preservation": 20,
        "community_preservation": 90,
        "cultural_value": 95,
        "evidence_note": "Delisted from the PlayStation Store, difficult to legally access, but heavily documented and culturally significant."
    }
]

weights = {
    "playable_access": 0.30,
    "platform_dependency": 0.20,
    "documentation": 0.15,
    "technical_preservation": 0.15,
    "community_preservation": 0.10,
    "cultural_value": 0.10,
}


def calculate_gpi_score(game):
    gpi_score = (
        game["playable_access"] * weights["playable_access"]
        + game["platform_dependency"] * weights["platform_dependency"]
        + game["documentation"] * weights["documentation"]
        + game["technical_preservation"] * weights["technical_preservation"]
        + game["community_preservation"] * weights["community_preservation"]
        + game["cultural_value"] * weights["cultural_value"]
    )

    return round(gpi_score, 2)


def get_preservation_status(score):
    if score >= 80:
        return "Well Preserved"
    elif score >= 60:
        return "Stable"
    elif score >= 40:
        return "Vulnerable"
    elif score >= 20:
        return "High Risk"
    else:
        return "Critical Risk"

def print_game_report(game):
    print()
    print("Game:", game["title"])
    print("Year:", game["release_year"])
    print("Platform:", game["platform"])
    print("GPI Score:", game["gpi_score"], "%")
    print("Status:", game["preservation_status"])
    print("Evidence:", game["evidence_note"])


print("Game Preservation Index")
print("-----------------------")

for game in games:
    game["gpi_score"] = calculate_gpi_score(game)
    game["preservation_status"] = get_preservation_status(game["gpi_score"])
    
    print_game_report(game)

print()
print("GPI Ranking")
print("-----------")

ranked_games = sorted(games, key=lambda game: game["gpi_score"], reverse=True)

for position, game in enumerate(ranked_games, start=1):
    print(
        position,
        "-",
        game["title"],
        "-",
        game["gpi_score"],
        "%",
        "-",
        game["preservation_status"]
    )
