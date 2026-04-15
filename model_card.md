# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
**VibeMatch CLI 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

This system recommends songs from a small dataset based on user preferences like genre, mood, and energy. It is designed for educational purposes and not for real-world deployment.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

The model compares each song to a user's preferences and assigns a score. It gives strong weight to genre and mood matches, then adjusts the score based on how close the song’s energy, tempo, and valence are to the user’s target values. Songs are ranked by their total score.
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The dataset contains 17 songs with a mix of genres including pop, rock, lofi, jazz, and electronic. Each song includes features like energy, tempo, and mood. The dataset is small and does not represent all types of music or listeners.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition 

The system works well when the user has clear preferences, such as high-energy or chill music. It produces understandable recommendations and provides explanations for each result.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The system over-prioritizes genre, which can hide songs that match well in other ways. It also ignores danceability and acousticness, which may matter to users. Because the dataset is small, some genres appear more often and may dominate recommendations.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

I tested the system with three profiles: high-energy pop, chill lofi, and intense rock. The results generally matched expectations, but some songs appeared repeatedly due to strong genre weighting. Removing or adjusting weights changed results significantly.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

Add weighting customization for users
Include more features like danceability
Improve diversity in recommendations

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Building this recommender helped me understand how AI systems turn preferences into predictions. I was surprised how even a simple formula could produce meaningful recommendations. It also showed me how easily bias can enter through feature weighting.