# 🎬 Sentiment-Based Movie Recommendation System 🍿

Welcome to the **Sentiment-Based Movie Recommendation System**! This project provides personalized movie recommendations based on user sentiment, leveraging the power of sentiment analysis, the **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) algorithm, and user preferences. 

This interactive web application, built with **Streamlit**, allows users to explore and filter movie recommendations based on mood, sentiment, and personal preferences. Whether you're looking for a **thriller with strong female leads** or a **heartwarming family movie**, this system has got you covered!

## 🚀 Features

- **Top 15 Movie Recommendations**: Personalized movie suggestions based on sentiment analysis of reviews and **TOPSIS** ranking.
- **Emotion-Aware Recommendations**: Match movie suggestions to your mood (e.g., happy, sad, excited, etc.).
- **User Preferences**: Refine your recommendations by selecting specific genres, languages, runtimes, and more.
- **Interactive Web Interface**: Built using **Streamlit**, providing an intuitive, easy-to-use platform for movie recommendations.
- **Future Chatbot Integration**: Ask the system for specific movie recommendations using natural language (e.g., "I want a thriller with a strong female lead.").

## 🛠️ Technologies Used

- **Python 3.x**
- **Streamlit**: For building the interactive web app
- **pandas**: Data manipulation and analysis
- **scikit-learn**: For machine learning tasks, such as normalization (for TOPSIS)
- **VADER Sentiment Analysis**: For sentiment scoring of movie reviews
- **numpy**: For numerical operations
- **matplotlib** & **seaborn**: For data visualization

## 📁 Project Structure

Sentiment-Based_Movie_Recommendation_System/
│
├── app.py                      # Main Streamlit app entry point (frontend + logic)
├── requirements.txt            # List of Python dependencies
│
├── data/                       # Input datasets
│   ├── imdb_tmdb_dataset.csv   # Movie metadata dataset (from IMDb and TMDB)
│   └── README.md               # Information on the dataset (optional)
│
├── output/                     # Output results
│   └── final_recommendations.csv  # Generated movie recommendations
│
├── src/                        # Source code / core logic
│   ├── __init__.py             # Makes src a Python package
│   ├── data_preprocessing.py   # Data loading, cleaning, merging
│   ├── sentiment_analysis.py   # Sentiment scoring logic (e.g., using VADER)
│   ├── recommendation.py       # TOPSIS algorithm and filtering logic
│   ├── utils.py                # Helper functions (e.g., for genre filters)
│
├── .gitignore                  # Git ignore file for excluding unnecessary files/folders
├── LICENSE                     # License file (e.g., MIT License)
├── README.md                   # Project overview & instructions
└── setup.py                    # Python package setup (optional if you want to distribute your code)


## 🏁 Getting Started

    1. Clone the repository:
   ```bash
   git clone https://github.com/Gyuhan1004/Sentiment-based_Movie_Recommendation_System.git
   cd Sentiment-based_Movie_Recommendation_System
    2. Install dependencies:
        First, create a virtual environment (optional but recommended):
          python -m venv venv
          source venv/bin/activate  # On Windows use `venv\Scripts\activate`
        Then, install the required dependencies:
          pip install -r requirements.txt
    3. Dataset
       You can download the required movie metadata dataset from https://drive.google.com/file/d/1EWq0WhCyIONyuMp3UW7CZ214XAseDQKr/view?usp=sharing.

       The dataset includes movie information like title, genres, ratings, etc. Place it in the data/ folder as imdb_tmdb_dataset.csv.

    4. Run the application
       To start the Streamlit app and view your recommendations, run the following command:
        streamlit run app.py

🧐 How It Works
Data Preprocessing: The movie metadata and user reviews are cleaned, merged, and prepared for sentiment analysis and recommendation ranking.

Sentiment Analysis: The system uses VADER Sentiment Analysis to assign sentiment scores to movie reviews. Positive, negative, and neutral sentiments are captured and used in ranking movies.

TOPSIS Ranking: The TOPSIS method ranks movies based on their sentiment scores and metadata (e.g., average rating, number of votes, etc.).

User Preferences: After showing the top 15 movies, the user can set preferences (such as genre, language, etc.) to refine the movie suggestions.

Emotion-Aware Recommendations: Users can specify their mood (e.g., "happy," "sad"), and the app will provide movie recommendations that match their emotional state.

Voice/Chatbot Integration (Coming Soon!): In future versions, users will be able to interact with the system using natural language to request specific types of movies.

📊 Sample Output
The final recommendations will be displayed as a list of movies with the following information:

Movie Title

Genres

Average Rating

Overview

Poster Link

The recommendations will also be saved in output/final_recommendations.csv for later use.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Contributing
We welcome contributions! To contribute:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Implement your changes.

Commit your changes (git commit -am 'Add feature').

Push to the branch (git push origin feature-name).

Create a pull request.

👥 Acknowledgments
IMDb and TMDB for providing rich movie metadata.

VADER for enabling sentiment analysis of movie reviews.

Streamlit for making it easy to build interactive web applications.

Python Libraries: pandas, scikit-learn, numpy, matplotlib, seaborn, and more.

🤝 Contact
If you have any questions or suggestions, feel free to open an issue or reach out via the repository!

Enjoy discovering your next favorite movie! 🎥✨


