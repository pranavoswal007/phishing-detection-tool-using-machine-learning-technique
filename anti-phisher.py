import tkinter as tk
from tkinter import messagebox
import joblib
import pandas as pd
import re
import random

# Load the model and vectorizer
model = joblib.load(r'C:\Users\ASUS\Desktop\New folder\anti-phisher\phishing_detection_model.pkl')
tfidf_vectorizer = joblib.load(r'C:\Users\ASUS\Desktop\New folder\anti-phisher\tfidf_vectorizer.pkl')  # Load your TF-IDF vectorizer here

# Create the main window
root = tk.Tk()
root.title("Advanced Phishing Email Detector")
root.geometry("500x500")

# Set color theme
root.configure(bg="#1c1c1c")

# Function to check for phishing
def check_phishing():
    email_body = text_input.get("1.0", tk.END).strip()  # Get text from the input field
    if not email_body:
        messagebox.showwarning("Input Error", "Please enter an email body to analyze.")
        return

    # Preprocess the input text
    cleaned_body = preprocess(email_body)
    
    # Transform the input text using the loaded TF-IDF vectorizer
    X_new = tfidf_vectorizer.transform([cleaned_body])
    
    # Make predictions
    prediction = model.predict(X_new)
    prediction_proba = model.predict_proba(X_new)

    # Calculate additional metrics
    suspicious_words_count = count_suspicious_words(email_body)
    email_complexity_score = calculate_complexity(email_body)
    suspicious_links_count = count_suspicious_links(email_body)
    sender_reputation = assess_sender_reputation()

    # Display results
    if prediction[0] == 1:
        result_text = (
            f"This email is likely a phishing attempt.\n\n"
            f"Confidence: {prediction_proba[0][1] * 100:.2f}%\n"
            f"Suspicious Words Detected: {suspicious_words_count}\n"
            f"Complexity Score: {email_complexity_score}/10\n"
            f"Suspicious Links Detected: {suspicious_links_count}\n"
            f"Sender Reputation Score: {sender_reputation}/10"
        )
    else:
        result_text = (
            f"This email seems safe.\n\n"
            f"Confidence: {prediction_proba[0][0] * 100:.2f}%\n"
            f"Suspicious Words Detected: {suspicious_words_count}\n"
            f"Complexity Score: {email_complexity_score}/10\n"
            f"Suspicious Links Detected: {suspicious_links_count}\n"
            f"Sender Reputation Score: {sender_reputation}/10"
        )

    messagebox.showinfo("Prediction Result", result_text)

# Function to preprocess the text
def preprocess(text):
    if isinstance(text, str):
        text = text.lower()
        text = re.sub(r'<.*?>', '', text)
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    else:
        return ''  # Return an empty string if not a string

# Function to count suspicious words
def count_suspicious_words(text):
    suspicious_words = ['urgent', 'account', 'verify', 'click', 'login', 'secure', 'update', 'bank']
    words = text.lower().split()
    return sum(1 for word in words if word in suspicious_words)

# Function to calculate complexity score (arbitrary for demo)
def calculate_complexity(text):
    avg_sentence_length = sum(len(sentence.split()) for sentence in text.split('.')) / max(1, text.count('.'))
    score = min(10, max(1, int(avg_sentence_length / 3)))  # Scale score from 1 to 10
    return score

# Function to count suspicious links
def count_suspicious_links(text):
    return len(re.findall(r'http\S+|www\S+|https\S+', text))

# Function to simulate sender reputation assessment
def assess_sender_reputation():
    return random.randint(3, 9)  # Random score for demo

# Create GUI components with the new color scheme and styles
label = tk.Label(root, text="Enter Email Body:", font=("Helvetica", 14, "bold"), bg="#1c1c1c", fg="#FF4C4C")
label.pack(pady=10)

text_input = tk.Text(root, height=10, width=50, font=("Helvetica", 12), bg="#2e2e2e", fg="#ffffff", insertbackground="#FF4C4C")
text_input.pack(pady=10)

check_button = tk.Button(root, text="Check Phishing", command=check_phishing, font=("Helvetica", 12, "bold"), 
                         bg="#FF4C4C", fg="#ffffff", activebackground="#ff3333", activeforeground="#ffffff", width=15)
check_button.pack(pady=20)

# Run the application
root.mainloop()
