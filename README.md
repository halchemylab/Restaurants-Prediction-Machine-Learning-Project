# Restaurant Rating Prediction App

This project is a web application built using Streamlit that predicts a restaurant's rating based on its features. The app uses a machine learning model trained on a dataset of restaurants, which is analyzed in the accompanying Jupyter Notebook (`analysis.ipynb`).

## Features

* Predicts a restaurant's rating based on:
	+ Average cost for two
	+ Table booking availability
	+ Online delivery availability
	+ Price range (1-4)
* Uses a trained machine learning model to make predictions
* Allows users to input restaurant features and trigger predictions

## Technical Details

* Analyzes a dataset of restaurants in `analysis.ipynb`
* Built using Streamlit for the web application
* Uses scikit-learn for machine learning model training and prediction
* Utilizes joblib for model and scaler serialization

## Requirements

* Python 3.x
* Streamlit
* scikit-learn
* joblib
* pandas
* numpy

## Usage

1. Run `app.py` to launch the Streamlit app
2. Input restaurant features in the app's input fields
3. Click the "Predict the rating" button to trigger the prediction
4. View the predicted rating in the app

## Dataset Analysis

The `analysis.ipynb` Jupyter Notebook contains the analysis of the restaurant dataset. It includes:

* Data cleaning and preprocessing
* Exploratory data analysis (EDA)
* Model training and tuning using GridSearchCV
* Model evaluation and selection

dataset = "https://www.kaggle.com/datasets/mohdshahnawazaadil/restaurant-dataset"

## Model Training

The machine learning model is trained on the preprocessed dataset using scikit-learn's `GridSearchCV` class. The model is tuned for optimal hyperparameters and evaluated using metrics such as mean squared error.

## Model Deployment

The trained model is serialized using joblib and loaded into the Streamlit app. The app uses the loaded model to make predictions on user-inputted restaurant features.

## Future Work

* Collect and integrate more data to improve model accuracy
* Experiment with different machine learning algorithms and techniques
* Refine the app's user interface and user experience