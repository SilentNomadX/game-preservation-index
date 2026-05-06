import json


with open("games.json", "r") as file:
    games = json.load(file)


weights = {
    "playable_access": 0.30,
    "platform_dependency": 0.20,
    "documentation": 0.15,
    "technical_preservation": 0.15,
    "community_preservation": 0.10,
    "cultural_value": 0.10
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


def get_rarity_status(rarity_score):
    if rarity_score >= 80:
        return "Extremely Rare"
    elif rarity_score >= 60:
        return "Rare"
    elif rarity_score >= 40:
        return "Scarce"
    elif rarity_score >= 20:
        return "Uncommon"
    else:
        return "Common"


def get_collector_alert(game):
    rarity_score = game["rarity_score"]
    playable_access = game["playable_access"]
    platform_dependency = game["platform_dependency"]

    if rarity_score >= 80 and playable_access < 40:
        return "High Priority"
    elif rarity_score >= 60 and playable_access < 50:
        return "Buy Soon"
    elif rarity_score >= 40 or platform_dependency < 50:
        return "Monitor"
    else:
        return "Safe to Wait"


def generate_preservation_actions(game):
    actions = []

    if game["playable_access"] < 40:
        actions.append("Research legal ways to access and play the game today.")
        actions.append("Archive evidence of delisting, store removal, or lack of modern release.")

    if game["platform_dependency"] < 40:
        actions.append("Document hardware, operating system, controller, server, or platform dependencies.")

    if game["documentation"] < 50:
        actions.append("Collect manuals, guides, credits, box art, patch notes, interviews, and making-of material.")

    if game["technical_preservation"] < 50:
        actions.append("Search for technical information such as engine details, file formats, mod tools, patches, and source code history.")

    if game["community_preservation"] < 50:
        actions.append("Look for fan communities, modding groups, speedrunners, forums, wikis, and preservation projects.")

    if game["cultural_value"] >= 80:
        actions.append("Prioritise cultural documentation, including design analysis, historical context, and developer commentary.")

    if game["rarity_score"] >= 70:
        actions.append("Track rarity evidence, including current availability, pricing patterns, and platform access limits.")

    if not actions:
        actions.append("Game appears relatively well preserved. Continue monitoring availability and documentation.")

    return actions


def print_category_breakdown(game):
    print("Category Breakdown:")
    print("- Playable Access:", game["playable_access"])
    print("- Platform Dependency:", game["platform_dependency"])
    print("- Documentation:", game["documentation"])
    print("- Technical Preservation:", game["technical_preservation"])
    print("- Community Preservation:", game["community_preservation"])
    print("- Cultural Value:", game["cultural_value"])
    print("- Rarity Score:", game["rarity_score"])


def print_preservation_actions(game):
    print("Recommended Preservation Actions:")

    for action in game["preservation_actions"]:
        print("-", action)


def print_game_report(game):
    print()
    print("Game:", game["title"])
    print("Year:", game["release_year"])
    print("Platform:", game["platform"])
    print("GPI Score:", game["gpi_score"], "%")
    print("Preservation Status:", game["preservation_status"])
    print("Rarity Score:", game["rarity_score"], "%")
    print("Rarity Status:", game["rarity_status"])
    print("Collector Alert:", game["collector_alert"])
    print("Preservation Evidence:", game["evidence_note"])
    print("Rarity Reason:", game["rarity_reason"])
    print_category_breakdown(game)
    print_preservation_actions(game)


print("Game Preservation Index")
print("-----------------------")

for game in games:
    game["gpi_score"] = calculate_gpi_score(game)
    game["preservation_status"] = get_preservation_status(game["gpi_score"])
    game["rarity_status"] = get_rarity_status(game["rarity_score"])
    game["collector_alert"] = get_collector_alert(game)
    game["preservation_actions"] = generate_preservation_actions(game)

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

print()
print("Collector Priority Ranking")
print("--------------------------")

collector_ranked_games = sorted(games, key=lambda game: game["rarity_score"], reverse=True)

for position, game in enumerate(collector_ranked_games, start=1):
    print(
        position,
        "-",
        game["title"],
        "-",
        game["rarity_score"],
        "%",
        "-",
        game["rarity_status"],
        "-",
        game["collector_alert"]
    )

most_at_risk_game = min(games, key=lambda game: game["gpi_score"])

print()
print("!!! PRESERVATION PRIORITY !!!")
print("-----------------------------")
print("Urgent Focus:", most_at_risk_game["title"])
print("GPI Score:", most_at_risk_game["gpi_score"], "%")
print("Status:", most_at_risk_game["preservation_status"])
print("Evidence:", most_at_risk_game["evidence_note"])
print_preservation_actions(most_at_risk_game)

highest_collector_priority = max(games, key=lambda game: game["rarity_score"])

print()
print("!!! COLLECTOR PRIORITY !!!")
print("--------------------------")
print("Collector Focus:", highest_collector_priority["title"])
print("Rarity Score:", highest_collector_priority["rarity_score"], "%")
print("Rarity Status:", highest_collector_priority["rarity_status"])
print("Collector Alert:", highest_collector_priority["collector_alert"])
print("Reason:", highest_collector_priority["rarity_reason"])
