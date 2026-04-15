"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9,
            "tempo_bpm": 130,
            "valence": 0.8,
            "danceability": 0.8,
            "acousticness": 0.2,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.3,
            "tempo_bpm": 75,
            "valence": 0.6,
            "danceability": 0.5,
            "acousticness": 0.8,
        },
        "Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95,
            "tempo_bpm": 150,
            "valence": 0.4,
            "danceability": 0.6,
            "acousticness": 0.1,
        },
    }

    for profile_name, user_prefs in profiles.items():
        print(f"\n🔥 Profile: {profile_name}")
        
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\nTop recommendations:\n")
        print("=" * 50)

        for i, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"{i}. {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f}")
            print(f"   Why: {explanation}")
            print("-" * 50)


if __name__ == "__main__":
    main()
