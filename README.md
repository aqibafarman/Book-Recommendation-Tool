Book Recommendation System

A personalized Book Recommendation System built using collaborative filtering.
The project predicts and suggests books that a user might enjoy based on their past ratings and preferences.

📌 Project Goals

Develop a recommendation system that improves user engagement.

Provide personalized suggestions to reduce choice overload.

Help platforms increase user retention and discoverability of content.

💼 Business Need

Book platforms, online bookstores, or libraries often face the challenge of keeping users engaged while helping them discover new books.
A good recommendation system:

Boosts sales and rentals by showing relevant items.

Improves user satisfaction with tailored suggestions.

Enhances content discoverability for niche titles.

🔍 Approach & Insights

Exploratory Data Analysis (EDA)

Discovered rating patterns (popular books, active users).

Identified data sparsity and handled missing ratings.

Data Preprocessing

Removed outliers and inactive users.

Standardized formats for book titles and authors.

Model Development

Implemented collaborative filtering using KNN (item-based) and matrix factorization (SVD).

Evaluated models with RMSE and recommendation accuracy.

Meaningful Insights

Found clusters of readers with similar taste profiles.

Popular titles like Harry Potter had high cross-user recommendation scores.

Niche genres benefited most from personalization.

⚙️ Tech Stack

Python (Pandas, NumPy, Scikit-learn, Surprise)

Flask (for web app)

Matplotlib/Seaborn (for visualization)

Git & GitHub (for version control)


python app/app.py
