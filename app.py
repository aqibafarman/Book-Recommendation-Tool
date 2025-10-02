from flask import Flask, render_template, request
import pickle
import numpy as np
from difflib import get_close_matches

# Load the data files
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
merged_df = pickle.load(open('merged_df.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))

# Initialize Flask app
app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['original_title'].values),
        author=list(popular_df['author'].values),
        image=list(popular_df['image_url'].values),
        votes=list(popular_df['ratings_count'].values),
        rating=list(popular_df['avg_rating'].values)
    )

# Route to show the recommendation form
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

# Route to handle book recommendations
from difflib import get_close_matches

@app.route('/recommend_books', methods=['POST'])
def recommend_books():
    user_input = request.form.get('user_input')

    # Convert to lowercase for matching
    titles = list(pt.index)
    titles_lower = [title.lower() for title in titles]
    user_input_lower = user_input.strip().lower()

    close_matches = get_close_matches(user_input_lower, titles_lower, n=1, cutoff=0.5)

    if not close_matches:
        return render_template('recommend.html', data=[], message="Book not found. Try another title.")

    matched_index = titles_lower.index(close_matches[0])
    matched_title = titles[matched_index]

    index = np.where(pt.index == matched_title)[0][0]

    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_items:
        item = []
        temp_df = merged_df[merged_df['original_title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('original_title')['original_title'].values))
        item.extend(list(temp_df.drop_duplicates('original_title')['author'].values))
        item.extend(list(temp_df.drop_duplicates('original_title')['image_url'].values))
        data.append(item)

    return render_template('recommend.html', data=data)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
