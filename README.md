
# Phishing Detection Tool Using Machine Learning

This project leverages machine learning techniques to detect phishing emails by analyzing their content. The tool employs a Random Forest Classifier trained on a cleaned dataset of emails. The application includes a graphical user interface (GUI) for user-friendly interaction and functionalities to preprocess text, train models, and make predictions.

## Table of Contents

- [Features](#features)
- [Technical Details](#technical-details)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features

- **Email Classification**: Classifies emails as phishing or not phishing based on textual analysis.
- **Data Preprocessing**: Cleans and prepares raw email data for analysis.
- **Model Training**: Trains a Random Forest Classifier on the cleaned dataset.
- **GUI Interface**: User-friendly interface for inputting text and displaying results.
- **Model Persistence**: Saves the trained model and vectorizer for future use.

## Technical Details

1. **Data Cleaning**: 
   - The script `dataset_clean.py` is responsible for loading the dataset, removing duplicates, and handling missing values. It ensures that the dataset is ready for analysis by normalizing the email body text.
   
2. **Text Vectorization**: 
   - The `TfidfVectorizer` from the scikit-learn library transforms the cleaned text data into numerical format, allowing the machine learning model to process it. This vectorization represents the importance of words in the emails.

3. **Random Forest Classifier**: 
   - The `RandomForestClassifier` is used to train the model on the processed dataset. It works by creating multiple decision trees and aggregating their predictions to improve accuracy and robustness.

4. **Model Training and Prediction**: 
   - The script `ml_model_trainer.py` handles the training of the model and evaluates its performance. It splits the dataset into training and testing sets, fits the model, and saves the trained model and vectorizer using `joblib`.

5. **GUI for Predictions**: 
   - The `anti-phisher.py` script implements the GUI. It allows users to input email content and displays the prediction results based on the trained model.

## File Structure

```
phishing-detection-tool-using-machine-learning-technique/
│
├── anti-phisher.py              # GUI application for phishing detection
├── cleaned_data.csv             # Cleaned dataset for training
├── dataset_clean.py             # Script for cleaning the dataset
├── ml_model_trainer.py          # Script for training the machine learning model
├── phishing_detection_model.pkl  # Trained Random Forest model
├── tfidf_vectorizer.pkl         # Saved TF-IDF vectorizer
└── dataset/                     # Folder containing raw datasets
    ├── Ling/
    ├── phishing_email/
    └── SpamAssasin/
```

## Installation

To run this project on your Windows machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/aarizkhanshaikh/phishing-detection-tool-using-machine-learning-technique.git
   ```
   
2. Change the directory to the project folder:
   ```bash
   cd phishing-detection-tool-using-machine-learning-technique
   ```

3. Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the GUI application:
   ```bash
   python anti-phisher.py
   ```

2. Input the email text you want to analyze in the provided text area.

3. Click the "Predict" button to get the classification result indicating whether the email is phishing or not.
