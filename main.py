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


def prepare_games(games):
    for game in games:
        game["gpi_score"] = calculate_gpi_score(game)
        game["preservation_status"] = get_preservation_status(game["gpi_score"])
        game["rarity_status"] = get_rarity_status(game["rarity_score"])
        game["collector_alert"] = get_collector_alert(game)
        game["preservation_actions"] = generate_preservation_actions(game)


def print_score_explanation(game, category):
    explanation = game["score_explanations"][category]

    print("  Reason:", explanation["reason"])
    print("  Confidence:", explanation["confidence"])


def print_category_breakdown(game):
    print("Category Breakdown:")

    print("- Playable Access:", game["playable_access"])
    print_score_explanation(game, "playable_access")

    print("- Platform Dependency:", game["platform_dependency"])
    print_score_explanation(game, "platform_dependency")

    print("- Documentation:", game["documentation"])
    print_score_explanation(game, "documentation")

    print("- Technical Preservation:", game["technical_preservation"])
    print_score_explanation(game, "technical_preservation")

    print("- Community Preservation:", game["community_preservation"])
    print_score_explanation(game, "community_preservation")

    print("- Cultural Value:", game["cultural_value"])
    print_score_explanation(game, "cultural_value")

    print("- Rarity Score:", game["rarity_score"])
    print_score_explanation(game, "rarity_score")


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


def print_terminal_report(games):
    print("Game Preservation Index")
    print("-----------------------")

    for game in games:
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


def add_markdown_score_explanation(report_lines, game, category):
    explanation = game["score_explanations"][category]

    report_lines.append(f"  - Reason: {explanation['reason']}")
    report_lines.append(f"  - Confidence: {explanation['confidence']}")


def generate_markdown_report(games):
    report_lines = []

    report_lines.append("# Game Preservation Index Report")
    report_lines.append("")
    report_lines.append("This report evaluates games by preservation risk, rarity, collector priority, evidence, and recommended preservation actions.")
    report_lines.append("")

    for game in games:
        report_lines.append(f"## {game['title']}")
        report_lines.append("")
        report_lines.append(f"- Year: {game['release_year']}")
        report_lines.append(f"- Platform: {game['platform']}")
        report_lines.append(f"- GPI Score: {game['gpi_score']}%")
        report_lines.append(f"- Preservation Status: {game['preservation_status']}")
        report_lines.append(f"- Rarity Score: {game['rarity_score']}%")
        report_lines.append(f"- Rarity Status: {game['rarity_status']}")
        report_lines.append(f"- Collector Alert: {game['collector_alert']}")
        report_lines.append("")
        report_lines.append("### Preservation Evidence")
        report_lines.append("")
        report_lines.append(game["evidence_note"])
        report_lines.append("")
        report_lines.append("### Rarity Reason")
        report_lines.append("")
        report_lines.append(game["rarity_reason"])
        report_lines.append("")
        report_lines.append("### Score Breakdown")
        report_lines.append("")

        categories = [
            ("Playable Access", "playable_access"),
            ("Platform Dependency", "platform_dependency"),
            ("Documentation", "documentation"),
            ("Technical Preservation", "technical_preservation"),
            ("Community Preservation", "community_preservation"),
            ("Cultural Value", "cultural_value"),
            ("Rarity Score", "rarity_score")
        ]

        for label, key in categories:
            report_lines.append(f"- {label}: {game[key]}")
            add_markdown_score_explanation(report_lines, game, key)

        report_lines.append("")
        report_lines.append("### Recommended Preservation Actions")
        report_lines.append("")

        for action in game["preservation_actions"]:
            report_lines.append(f"- {action}")

        report_lines.append("")

    ranked_games = sorted(games, key=lambda game: game["gpi_score"], reverse=True)
    collector_ranked_games = sorted(games, key=lambda game: game["rarity_score"], reverse=True)

    report_lines.append("## GPI Ranking")
    report_lines.append("")

    for position, game in enumerate(ranked_games, start=1):
        report_lines.append(f"{position}. {game['title']} - {game['gpi_score']}% - {game['preservation_status']}")

    report_lines.append("")
    report_lines.append("## Collector Priority Ranking")
    report_lines.append("")

    for position, game in enumerate(collector_ranked_games, start=1):
        report_lines.append(f"{position}. {game['title']} - {game['rarity_score']}% - {game['rarity_status']} - {game['collector_alert']}")

    most_at_risk_game = min(games, key=lambda game: game["gpi_score"])
    highest_collector_priority = max(games, key=lambda game: game["rarity_score"])

    report_lines.append("")
    report_lines.append("## Preservation Priority")
    report_lines.append("")
    report_lines.append(f"Urgent Focus: {most_at_risk_game['title']}")
    report_lines.append(f"GPI Score: {most_at_risk_game['gpi_score']}%")
    report_lines.append(f"Status: {most_at_risk_game['preservation_status']}")
    report_lines.append(f"Evidence: {most_at_risk_game['evidence_note']}")

    report_lines.append("")
    report_lines.append("## Collector Priority")
    report_lines.append("")
    report_lines.append(f"Collector Focus: {highest_collector_priority['title']}")
    report_lines.append(f"Rarity Score: {highest_collector_priority['rarity_score']}%")
    report_lines.append(f"Rarity Status: {highest_collector_priority['rarity_status']}")
    report_lines.append(f"Collector Alert: {highest_collector_priority['collector_alert']}")
    report_lines.append(f"Reason: {highest_collector_priority['rarity_reason']}")

    return "\n".join(report_lines)


def save_markdown_report(games):
    markdown_report = generate_markdown_report(games)

    with open("gpi_report.md", "w") as file:
        file.write(markdown_report)

    print()
    print("Markdown report created: gpi_report.md")


prepare_games(games)
print_terminal_report(games)
save_markdown_report(games)