# 🎬 Movie Recommender System

A content-based movie recommender system built with Python and Streamlit that suggests similar movies along with their posters and ratings.

## 🔗 Live Demo
[Click here to try it!](https://movie-recommender-system-aradhya-tiwari-app.streamlit.app)

## 📌 Features
- Select any movie from 5000+ movies
- Get 5 similar movie recommendations instantly
- Displays movie posters fetched from TMDB API
- Shows TMDB ratings for each recommended movie
- Click "More Info" to learn more about any movie

## 🛠 Tech Stack
- Python
- Pandas
- Scikit-learn
- NLTK
- Streamlit
- TMDB API
- Git & GitHub

## 🧠 How It Works
1. Movie metadata (genres, cast, crew, keywords, overview) is combined into tags
2. Tags are vectorized using CountVectorizer
3. Cosine similarity is calculated between all movies
4. Top 5 most similar movies are returned for any selected movie

## 📂 Dataset
TMDB 5000 Movie Dataset from Kaggle (https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## ⚙️ Run Locally
```bash
git clone https://github.com/aradhyatw16/Movie-Recommender-System.git
cd Movie-Recommender-System
pip install -r requirements.txt
streamlit run app.py
```

## 📸 Screenshot
(<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8864faf3-497b-4da1-9b98-307f65aecb39" />
)

## 👤 Author

**Aradhya Tiwari**
- GitHub: [@aradhyatw16](https://github.com/aradhyatw16)
- LinkedIn: [Aradhya Tiwari](https://www.linkedin.com/in/aradhya-tiwari2006)

