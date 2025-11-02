from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from joblib import dump
from intents import intents
import random
import os

# Collect all patterns and their corresponding tags
patterns = []
tags = []

for intent in intents:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])

# Create and train the vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

# Create and train the classifier
clf = LogisticRegression(max_iter=10000, random_state=0)
clf.fit(X, tags)

# Save the models
os.makedirs("models", exist_ok=True)
dump(vectorizer, "models/vectorizer.pkl")
dump(clf, "models/classifier.pkl")

print("Training complete. Models saved to models/")