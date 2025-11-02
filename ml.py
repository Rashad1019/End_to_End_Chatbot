from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from joblib import dump
from intents import intents
import random, os

patterns, tags = [], []
for intent in intents:
    for p in intent["patterns"]:
        patterns.append(p)
        tags.append(intent["tag"])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

clf = LogisticRegression(max_iter=10000)
clf.fit(X, tags)

os.makedirs("models", exist_ok=True)
dump(vectorizer, "models/vectorizer.pkl")
dump(clf, "models/classifier.pkl")

print("Training complete. Models saved to /models/")

