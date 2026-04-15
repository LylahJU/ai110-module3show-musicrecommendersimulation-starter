from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numerical values to appropriate types
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    return songs

def score_song(user_prefs, song):
    """
    Scores a song based on user preferences.
    
    Returns: (score, reasons) where:
      - score is a float representing the total score
      - reasons is a list of strings explaining each component
    
    Algorithm:
      - Genre match: +2.0 points (categorical)
      - Mood match: +1.0 point (categorical)
      - Energy score: 0 to 1.0 based on closeness to target energy
      - Tempo score: 0 to 1.0 based on closeness to target tempo_bpm
      - Valence score: 0 to 1.0 based on closeness to target valence
    """
    score = 0.0
    reasons = []
    
    # Genre match: 2.0 points
    if song['genre'].lower() == user_prefs['genre'].lower():
        score += 2.0
        reasons.append("genre match (+2.0)")
    
    # Mood match: 1.0 point
    if song['mood'].lower() == user_prefs['mood'].lower():
        score += 1.0
        reasons.append("mood match (+1.0)")
    
    # Energy score: based on how close the song's energy is to the user's target
    # Max distance is 1.0 (0 to 1 scale), so we calculate: 1.0 - abs_distance
    energy_distance = abs(song['energy'] - user_prefs['energy'])
    energy_score = max(0, 1.0 - energy_distance)  # Clamp to [0, 1]
    score += energy_score
    reasons.append(f"energy match (+{energy_score:.2f})")
    
    # Tempo score: based on how close the song's tempo is to the user's target
    # Normalize by dividing distance by 200 (reasonable tempo range)
    tempo_distance = abs(song['tempo_bpm'] - user_prefs['tempo_bpm'])
    tempo_score = max(0, 1.0 - (tempo_distance / 200))  # Clamp to [0, 1]
    score += tempo_score
    reasons.append(f"tempo match (+{tempo_score:.2f})")
    
    # Valence score: based on how close the song's valence is to the user's target
    # Max distance is 1.0 (0 to 1 scale), so we calculate: 1.0 - abs_distance
    valence_distance = abs(song['valence'] - user_prefs['valence'])
    valence_score = max(0, 1.0 - valence_distance)  # Clamp to [0, 1]
    score += valence_score
    reasons.append(f"valence match (+{valence_score:.2f})")
    
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    
    # Score all songs and create (song, score, explanation) tuples
    scored_songs = [
        (song, score, ", ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    
    # Sort by score (descending) and return top k
    return sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
