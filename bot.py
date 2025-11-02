import random
from joblib import load
from intents import intents

vectorizer = load("models/vectorizer.pkl")
clf = load("models/classifier.pkl")

def get_response(text, threshold=0.2):
    probs = clf.predict_proba(vectorizer.transform([text]))[0]
    tag_index = probs.argmax()
    confidence = probs[tag_index]
    if confidence < threshold:
        return "I'm not sure I understand."
    tag = clf.classes_[tag_index]
    for intent in intents:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

