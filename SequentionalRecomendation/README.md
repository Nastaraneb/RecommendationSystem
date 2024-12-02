# Sequential Recommendation System for Group Satisfaction

This project aims to develop a **sequential recommendation model** that suggests movie lists to groups of users over multiple iterations within a given time interval. The primary objective is to **minimize disagreements within the group** and **enhance overall satisfaction** with each iteration. By continuously improving the recommendations, the model delivers progressively better movie lists tailored to group preferences.

---

## **Core Concept**
In group recommendation systems, satisfying diverse preferences is a challenging task. Our proposed model adopts a **balanced and moderate approach** to address this challenge, ensuring that group members' satisfaction increases while reducing disagreement. 

### **Key Features**
1. **Dynamic Adjustment**: The model adapts to group dynamics, leveraging three aggregation methods to balance satisfaction and disagreement.
2. **Iterative Improvement**: Recommendations evolve over time, leading to higher satisfaction and reduced variance in opinions.
3. **Weighted Aggregation**: The model utilizes coefficients to dynamically adjust the influence of each method.

---

## **Methods of Aggregation**

The model integrates three aggregation methods, each contributing to the recommendation process:

1. **Average Method**: Focuses on balancing satisfaction when disagreements are minimal.
2. **Least Misery Method**: Considers the minimum satisfaction scores to prevent dissatisfaction.
3. **Borda Count Method**: Accounts for ranked preferences to produce impactful, high-scoring recommendations.

### **Weighted Formula**
The final score is calculated using a weighted combination of the three methods:

Score = α × AVG + β × BORDA + γ × LEAST

- **α (Alpha)**: Coefficient for the Average method
- **β (Beta)**: Coefficient for the Borda Count method
- **γ (Gamma)**: Coefficient for the Least Misery method

The coefficients are determined dynamically based on satisfaction metrics:
- **Beta (β)** = (Average Satisfaction / 2) - Variance of Satisfaction
- **Gamma (γ)** = (Average Satisfaction / 2) + Variance of Satisfaction
- **Alpha (α)** = 1 - (β + γ)

---

## **How It Works**
- **Balancing Methods**: The model adjusts the influence of each method (AVG, Borda, Least Misery) using the calculated coefficients. 
  - When users have **balanced satisfaction** and low disagreement, the **Average method** is prioritized.
  - For groups with **high disagreement**, the model shifts weight toward the **Least Misery** and **Borda Count** methods to minimize variance and dissatisfaction.

- **Role of Variance**:
  - **Borda Count**: Reducing variance decreases disagreement and improves overall satisfaction.
  - **Least Misery**: Increasing variance ensures minority opinions are adequately addressed.
  - The dynamic use of variance balances these effects and drives group satisfaction toward equilibrium.

---

## **Conclusion**
This sequential recommendation model is designed to iteratively improve group satisfaction by leveraging dynamic weighting and diverse aggregation methods. By balancing preferences and addressing disagreements, it delivers movie lists that cater to diverse user groups effectively.

Feel free to explore and contribute to the project!
