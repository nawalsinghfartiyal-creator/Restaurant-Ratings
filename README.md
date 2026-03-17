# Restaurant Ratings Predictor

A machine learning project that predicts restaurant ratings based on various features such as location, cost, and customer engagement. This project demonstrates a complete data science workflow, from data preprocessing and exploratory analysis to model building and deployment using Streamlit

## 🚀 Live Demo
####  Streamlit App:

https://restaurant-ratings-hzrvhdy5iz8ezoaaz6u2dd.streamlit.app/


## 📌 Project Overview

The objective of this project is to build a predictive model capable of estimating restaurant ratings using structured data. By leveraging machine learning techniques, the project aims to uncover patterns in customer preferences and restaurant characteristics

The workflow includes:
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training and evaluation
- Deployment via an interactive web application


## 📊 Exploratory Data Analysis (EDA)

Exploratory analysis was conducted to understand the structure of the data and identify key factors influencing restaurant ratings

  #### Key Insights

  - **City-wise Pricing Trends:**

    Certain cities exhibit significantly higher average dining costs, indicating regional differences in pricing and customer
     expectations
  
  - **Feature Relationships:**

    Relationships between cost, number of votes, and ratings suggest that more popular restaurants tend to receive higher engagement
     and potentially better ratings
 
  - **Online Delivery Distribution:**

     A noticeable proportion of restaurants offer online delivery, which may influence accessibility and customer satisfaction
  
  - **Rating Distribution:**  

    Ratings are not uniformly distributed across categories, indicating possible class imbalance and varying customer experiences



## 🧠 Models Implemented
  
  The following machine learning models were developed and evaluated:

  - **Linear Regression**
  - **Decision Tree Regressor**
  - **Support Vector Regression (SVR)**

  

## 📈 Model Performance & Findings

#### ◆ Linear Regression

  - **_MAE: ~1.11_**
  - **_RMSE: ~1.34_**
  - Provides a strong baseline with stable and interpretable predictions
  - Errors are balanced, with no significant impact from outliers
  - Effectively captures overall trends in the data


#### ◆ Decision Tree Regressor

  - **_MAE: ~0.99_**
  - **_RMSE: ~1.25_**
  - Achieved the best performance among tested models
  - Predictions are highly accurate with low average error
  - Minimal large deviations, indicating stable performance
  - Suitable for real-world use with a good balance of accuracy and interpretability


#### ◆ Support Vector Regression (SVR)

  - **_MAE: ~1.01_**
  - **_RMSE: ~1.49_**
  - Demonstrates strong generalization and robustness
  - Maintains consistent prediction performance
  - Slightly higher RMSE suggests sensitivity to some larger errors



## 📊 Overall Conclusion

  - All models performed well, with errors close to **1 rating point on average**
  - The **Decision Tree model** provided the best balance of accuracy and consistency
  - Linear Regression served as a reliable baseline
  - SVR showed strong robustness and generalization

  These results demonstrate that restaurant ratings can be effectively predicted using structured features and appropriate machine
  learning techniques


## 🛠️ Tech Stack

  - **Programming Language**: Python
  - **Libraries:**
      - Pandas
      - NumPy
      - Scikit-learn
      - Matplotlib & Seaborn
      - Streamlit


## ⚙️ Deployment

The model is deployed using **Streamlit**, allowing users to interactively input restaurant features and receive predicted ratings in real time
