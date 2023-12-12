# Final_Housing_Project

# Introduction
Housing price prediction utilizes data-driven models to estimate property values based on factors like 
income, house characteristics, and location. It aids buyers and sellers in making informed decisions and 
guides real estate investments. Key challenges include non-linearity in market dynamics and data 
variability over time. Regression models, such as Linear Regression and Decision Trees, are commonly 
employed for this task. Accurate predictions contribute to a transparent and efficient real estate market, 
benefiting various stakeholders.

# Dataset Cleaning
In this step, the focus was on ensuring the dataset's completeness and addressing any missing values that 
might impact the subsequent analysis and modeling. The process involves the following steps:
1. Identification of Missing Values
2. Handling Missing Values
3. Significance of No Missing Values
4. Impact on Analysis
5. Preparation for Exploration

# Data Exploration
1. Statistical Overview:
Utilized df.describe() to generate basic statistical summaries (mean, standard deviation, min, max, 
quartiles) for each numeric column in the dataset. This provides insights into the central tendency and 
spread of the data.
2. Visual Exploration:
Correlation values close to 1 or -1 indicate strong positive or negative correlations, 
respectively. Employed scatter plots, such as 'MedInc' vs. 'target,' to identify patterns and relationships 
between specific features and the target variable.

# Feature Engineering
1. Creating a New Feature: 'RoomsPerHousehold': A new feature, 'RoomsPerHousehold,' is created by taking the ratio of 'AveRooms' to 'HouseAge.'
2. Handling Categorical Variables:
Handling categorical variables is a common aspect of feature engineering.In the above data, a hypothetical 
categorical variable 'categorical_column' is used as an illustration. One-hot encoding is applied to convert 
categorical variables into numerical format, creating binary columns for each category.

# Model Selection
Two regression models were chosen for experimentation: Linear Regression and Decision Tree Regressor. 
These models serve as initial candidates for predicting housing prices based on the dataset's features.

# Hyperparameter tuning 
The step utilizes GridSearchCV to perform hyperparameter tuning for Linear Regression and Decision 
Tree Regressor. It defines hyperparameter grids for each model, iterates through the models, and 
identifies the best parameters through cross-validated search. The best models are then used to make 
predictions on the test set, and the Mean Squared Error is calculated for evaluation. Finally, the best 
hyperparameters and model performance metrics are printed for both Linear Regression and Decision 
Tree Regressor. The code encapsulates a comprehensive hyperparameter optimization process for 
regression models.

# Pickle Files
This step trains a Decision Tree Regressor on housing data, splits it into training and testing sets, and 
evaluates performance using Mean Squared Error. The trained model is then saved as a pickle file named 
'Decision_Tree_Regressor_model.pkl.' The code encapsulates model training, evaluation, and persistence 
for future use.

# Model Deployment
The provided code trains a Decision Tree Regressor on housing data, saves the model as a pickle file, and 
deploys an interactive dashboard using Panel for users to explore model predictions and evaluation 
metrics. The deployment includes creating a user-friendly interface with input widgets, integrating the 
saved model into the Panel app, and launching an interactive dashboard for users to interact with the 
deployed Decision Tree Regressor model.

# Prediction
A function was created to take a new review as input, preprocess it, and predict its sentiment 
using the deployed model. The project successfully conducted sentiment analysis on food reviews,
providing insightsinto the sentiment distribution, frequently used words, and review patterns over
time. The Logistic Regression model demonstrated reliable performance in classifying
sentiments, and the deploymentpipeline allows for real time predictions on new reviews.

