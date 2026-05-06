import os
import requests


CLIENT_ID = os.getenv("IGDB_CLIENT_ID")
CLIENT_SECRET = os.getenv("IGDB_CLIENT_SECRET")


def get_access_token():
    url = "https://id.twitch.tv/oauth2/token"

    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }

    response = requests.post(url, params=params)
    response.raise_for_status()

    return response.json()["access_token"]


def search_game(game_name, access_token):
    url = "https://api.igdb.com/v4/games"

    headers = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {access_token}"
    }

    body = f'''
        search "{game_name}";
        fields name, summary, first_release_date, platforms.name, genres.name;
        limit 3;
    '''

    response = requests.post(url, headers=headers, data=body)
    response.raise_for_status()

    return response.json()


def print_results(results):
    for game in results:
        print()
        print("Title:", game.get("name", "Unknown"))
        print("Summary:", game.get("summary", "No summary available"))

        platforms = game.get("platforms", [])
        platform_names = []

        for platform in platforms:
            platform_names.append(platform.get("name", "Unknown platform"))

        print("Platforms:", ", ".join(platform_names))

        genres = game.get("genres", [])
        genre_names = []

        for genre in genres:
            genre_names.append(genre.get("name", "Unknown genre"))

        print("Genres:", ", ".join(genre_names))


if CLIENT_ID is None or CLIENT_SECRET is None:
    print("Missing IGDB credentials.")
    print("Set IGDB_CLIENT_ID and IGDB_CLIENT_SECRET before running this file.")
else:
    token = get_access_token()
    results = search_game("Silent Hill 2", token)
    print_results(results)