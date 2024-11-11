# Project Title
Group-Based Sequential Hybrid Aggregation Model for Movie Recommendations

This project applies a sequential hybrid aggregation model to generate personalized movie recommendations for user groups.
Using the MovieLens dataset, it explores various user-based and group-based recommendation techniques to enhance user satisfaction and reduce disagreement among group members.

Features
1.Data Processing: Downloads and processes the MovieLens dataset, 

2.dividing it into subsets for testing recommendations at different iterations.

3.User-Based Recommendations: Calculates user similarity based on ratings and makes recommendations for individual users.

4.Group-Based Recommendations: Uses three aggregation strategies (average, least misery, and Borda count) to make recommendations suitable for groups.

5.Sequential Hybrid Aggregation Model: Combines the three aggregation techniques with weighted parameters to maximize group satisfaction and reduce disagreement over multiple iterations.

6.Satisfaction and Disagreement Metrics: Tracks user and group satisfaction as well as intra-group disagreement for each recommendation iteration.

