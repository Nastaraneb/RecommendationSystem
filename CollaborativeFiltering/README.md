# Collaborative Filtering Implementation

This project focuses on implementing **User-Based** and **Item-Based Collaborative Filtering** using the **Pandas** library for data manipulation.

## 1. User-Based Collaborative Filtering

### Initial Steps
- The data file is loaded, and the first row is displayed for verification.
- The `user_based_sim` function calculates the similarity between two users based on their shared ratings.

### Key Details
- Instead of directly using `userId`, the ratings data (`rates_by_a` and `rates_by_b`) are passed as parameters to improve performance.
- **Commonly rated movies** between two users are identified to calculate similarity.  
  - If no common movies are found, the similarity is set to **zero**.
- Ratings from shared movies are extracted, and the similarity is computed using the formula provided in the lecture.

### Prediction and Recommendation
1. The `user_based_pred` function predicts a user’s rating for a specific movie.
2. A random user is selected to identify similar users. The results are sorted to find the **top 10 similar users**.
3. Recommended movies for the user are determined based on predicted ratings, and the **top 10 recommendations** are extracted.

---

## 2. Item-Based Collaborative Filtering

### Overview
This approach is similar to User-Based Collaborative Filtering but focuses on comparing items (movies) rather than users.

### Key Details
- The `item_based_sim` function calculates similarity between two movies based on shared user ratings.
- If no users have rated both movies, the similarity is set to **zero**.

### Prediction and Recommendation
1. The `item_based_pred` function predicts a user’s rating for a specific movie based on item similarity.
2. For a random user, predictions are made for all unique movies in the dataset.
3. Recommended movies are sorted by predicted ratings, and the **top 10 are identified**.

---

This project demonstrates the implementation of collaborative filtering methods using Python and highlights the steps to derive recommendations based on user and item similarities.
