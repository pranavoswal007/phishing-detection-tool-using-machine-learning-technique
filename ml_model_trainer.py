import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Load the dataset with specified dtypes
data = pd.read_csv(
    r'C:\Users\ASUS\Desktop\New folder\new\cleaned_data.csv', 
    dtype={'column1': str, 'column2': str, 'column3': str}  # Specify actual columns with mixed types
)

# Print the shape of the dataset
print(f"Data shape: {data.shape}")

# Check for missing values in the 'body' column
print(f"Missing values in 'body': {data['body'].isnull().sum()}")

# Fill NaN values with an empty string
data['body'] = data['body'].fillna('')
print("Filled NaN values in 'body'")

# Preprocess the data
def preprocess(text):
    # Ensure text is a string
    if isinstance(text, str):
        text = text.lower()
        text = re.sub(r'<.*?>', '', text)
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    else:
        return ''  # Return an empty string if not a string

# Clean the body text
print("Starting text preprocessing...")
data['cleaned_body'] = data['body'].apply(preprocess)
print("Completed text preprocessing.")

# Initialize the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the cleaned body text to get the feature matrix
X = tfidf_vectorizer.fit_transform(data['cleaned_body'])
print("TF-IDF vectorization complete.")

# Get the target labels
y = data['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data split into training and testing sets.")

# Initialize the model
model = RandomForestClassifier(n_estimators=10, random_state=42)  # Reduced for testing

# Train the model
print("Starting model training...")
model.fit(X_train, y_train)
print("Model training complete.")

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the model and vectorizer in the same folder
joblib.dump(model, r'C:\Users\ASUS\Desktop\New folder\new\phishing_detection_model.pkl')
joblib.dump(tfidf_vectorizer, r'C:\Users\ASUS\Desktop\New folder\new\tfidf_vectorizer.pkl')
print("Model and vectorizer saved.")
