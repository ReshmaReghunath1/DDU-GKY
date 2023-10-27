

# Heart Dataset Analysis
### Introduction
This README provides an overview of the analysis of the "Heart" dataset, focusing on predicting the target variable. The dataset contains the following features:

Age 

Sex

Chest Pain Type (cp)

Resting Blood Pressure (trestbps)

Cholesterol (chol)

Fasting Blood Sugar (fbs)

Resting Electrocardiographic Results (restecg)

Maximum Heart Rate Achieved (thalach)

Exercise-Induced Angina (exang)

ST Depression Induced by Exercise Relative to Rest (oldpeak)

Slope of the Peak Exercise ST Segment (slope)

Number of Major Vessels Colored by Fluoroscopy (ca)

Thalassemia (thal)

The target variable represents the presence (1) or absence (0) of heart disease.

## Models
In this analysis, we have considered several machine learning models to predict the presence of heart disease. The models used are:

Logistic Regression
Decision Tree Classifier
Random Forest Classifier
K-Nearest Neighbors Classifier
Gradient Boosting Classifier
AdaBoost Classifier
Gaussian Naive Bayes (GaussianNB)
XGBoost Classifier
## Model Evaluation
Each of the models was evaluated using cross-validation, and the mean accuracy scores were recorded. The following observations were made:

Logistic Regression: Mention the accuracy achieved Model Evaluation
In this section, we provide a detailed evaluation of the performance of the machine learning models on the Heart dataset. The evaluation includes various metrics and insights to assess the models' effectiveness.

Cross-Validation Scores
Cross-validation is a crucial technique to assess how well a model generalizes to unseen data. It involves splitting the dataset into multiple subsets (folds), training the model on a portion of the data, and evaluating it on the remaining data. The following are the cross-validation mean scores for each model:

Logistic Regression:
Mean Score: 83.89%

Decision Tree Classifier:
Mean Score: 100.0%

Random Forest Classifier:
Mean Score: 99.71%

K-Nearest Neighbors Classifier:
Mean Score: 75.99%

Gradient Boosting Classifier:
Mean Score: 97.07%

AdaBoost Classifier:
Mean Score: 89.36%

Gaussian Naive Bayes (GaussianNB):
Mean Score: 82.13%

XGBoost Classifier:
Mean Score: 100.0%
### Analysis of Results
#### Decision Tree and XGBoost:
 The Decision Tree Classifier and XGBoost Classifier achieved perfect accuracy scores (100.0%). While this may seem impressive, it raises concerns about overfitting and data leakage. Further investigation into the models and potential model tuning is required to ensure their reliability on new data.

#### Random Forest Classifier:
 The Random Forest Classifier also achieved a very high accuracy score (99.71%). It appears to be a strong candidate, but further analysis is needed to assess its robustness and generalization capabilities.

#### K-Nearest Neighbors (KNN):
 The KNN model achieved a lower accuracy score (75.99%), indicating that it may not be the best-performing model in this context. Further optimization or consideration of alternative models is recommended.

#### Gradient Boosting and AdaBoost:
 The Gradient Boosting and AdaBoost classifiers demonstrated relatively high mean scores, suggesting their potential as viable models for this dataset. Fine-tuning hyperparameters and feature selection might further improve their performance.

#### Gaussian Naive Bayes (GaussianNB):
 Gaussian Naive Bayes achieved a moderate mean score (82.13%). It can be considered, especially if interpretability and simplicity are desired.

Additionally, ROC (Receiver Operating Characteristic) curves have been analyzed for model performance. However, Here ROC are done for models XGBoost Classifier,Random Forest Classifier,Decision Tree Classifier,Random Forest Classifier,Gradient Boosting Classifier

### Conclusion
The analysis of the Heart dataset using various machine learning models has shown promising results, with some models achieving high accuracy.

Done Deployment using Thonny Application using XGBoost Classifier as model .