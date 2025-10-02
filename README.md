# 🎬 Movie Recommendation System

## 📌 Project Overview
This is a **content-based recommendation system** that suggests movies similar to a given movie using **cosine similarity** and **movie metadata**.

## 🎯 Goals
- Build a personalized recommendation system.
- Extract meaningful insights from movie metadata.
- Provide movie suggestions in real-time.

## 🛠 Business Need
With the growing volume of movies, it’s challenging for users to discover content they might like. This system solves that problem by recommending similar titles based on a movie the user already enjoys.

## 📊 How It Works
1. Load movie dataset.
2. Extract features (genre, keywords, cast, crew).
3. Transform text into numerical vectors using **TF-IDF**.
4. Calculate **cosine similarity** between movies.
5. Recommend the top N similar movies.

## 🚀 Installation
```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
cd Movie-Recommendation-System
pip install -r requirements.txt


