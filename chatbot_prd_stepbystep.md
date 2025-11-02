# PRD — End-to-End Chatbot (Python + Streamlit)
**Format:** Command-Driven, Step-by-Step  
**Goal:** Build a complete local chatbot using TF-IDF + Logistic Regression, deployed with Streamlit.

---

## 📋 Progress Summary

### ✅ **PROJECT COMPLETED** - All Steps 0-8 Implemented Successfully!

**Complete Steps:**
- ✅ **Step 0**: Project setup and environment preparation
- ✅ **Step 1**: Virtual environment created and dependencies installed
- ✅ **Step 2**: Minimal chat loop tested (sandbox.py created)
- ✅ **Step 3**: Intents dataset built (intents.py created with 4 intents)
- ✅ **Step 4**: ML model training completed (ml.py created and executed, models saved)
- ✅ **Step 5**: Bot response logic implemented (bot.py created with 0.3 confidence threshold)
- ✅ **Step 6**: Streamlit UI built (app.py with enhanced features)
- ✅ **Step 7**: Package & verify (requirements.txt frozen, full testing complete)
- ✅ **Step 8**: Optional enhancements partially implemented (confidence slider, model caching)

### 📁 Files Created:
- `sandbox.py` - Basic chat loop for testing
- `intents.py` - Intent patterns and responses dataset (4 intents: greeting, goodbye, thanks, about)
- `ml.py` - Model training script (TF-IDF + Logistic Regression)
- `bot.py` - ML-powered response function with confidence threshold
- `app.py` - Enhanced Streamlit web interface with diagnostics, confidence slider, and session management
- `hello.py` - Streamlit test file
- `requirements.txt` - Frozen dependencies (45 packages)
- `models/vectorizer.pkl` - Trained TF-IDF vectorizer
- `models/classifier.pkl` - Trained Logistic Regression classifier
- `step7_verification_report.md` - Deployment verification documentation

### 🎉 **What We Accomplished:**

A fully functional end-to-end chatbot has been successfully built with:

1. **Machine Learning Pipeline**: TF-IDF vectorization + Logistic Regression classifier
2. **Intent System**: 4 intents (greeting, goodbye, thanks, about) with multiple patterns and responses
3. **Web Interface**: Professional Streamlit UI with chat history, diagnostics panel, and confidence threshold control
4. **Robust Error Handling**: Model loading protection, confidence thresholding, and graceful failure messages
5. **Deployment Ready**: All dependencies frozen, models portable, production-ready structure
6. **Enhanced Features**: 
   - Model caching with `@st.cache_resource`
   - Adjustable confidence slider in sidebar
   - Session management (chat history, graceful exit)
   - Diagnostics panel for troubleshooting
   - Form-based input to prevent duplicate messages

### 🎯 **Next Opportunities (Future Enhancements):**

If you want to continue improving the chatbot later, consider:

1. **Expand Intent Dataset**: Add more patterns per intent and new intents (e.g., weather, help, jokes)
2. **Text Preprocessing**: Implement lowercasing, lemmatization, or stemming in `ml.py`
3. **Advanced Models**: Upgrade to Sentence-Transformers or neural embeddings for better accuracy
4. **External Integrations**: Add API calls for real-time data (weather, news, etc.)
5. **Persistent Storage**: Save chat history to database or file
6. **User Authentication**: Add login and personalized conversations
7. **Analytics**: Track conversation metrics and user satisfaction
8. **Deployment**: Host on Streamlit Cloud, Heroku, or AWS

---

✅ ## STEP 0 — Project Setup & Requirements
*(Prepare your environment and confirm everything works before coding.)*

1. **Create a project folder**
   ```bash
   mkdir chatbot_project
   cd chatbot_project
   ```

2. **Check Python installation**
   ```bash
   python --version
   ```
   or
   ```bash
   py --version
   ```

3. **If Python ≥ 3.10 is not installed**
   - Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Run the Windows installer.
   - Tick **“Add Python to PATH.”**

4. **(Optional)** Verify Git
   ```bash
   git --version
   ```
   If missing, install from [https://git-scm.com/downloads](https://git-scm.com/downloads)

5. **Open folder in Cursor**
   - Launch Cursor  
   - *File → Open Folder → select `chatbot_project`*

6. **Create placeholder README**
   ```bash
   echo Chatbot Project Initialized > README.md
   ```

✅ **Expected Result:**  
- Folder `chatbot_project` open in Cursor  
- `python --version` ≥ 3.10  
- (Optional) `git --version` works  
- `README.md` exists  

---

✅ ## STEP 1 — Create Virtual Environment & Install Dependencies
*(Isolate environment; install required libraries.)*

1. **Create venv**
   ```bash
   py -m venv .venv
   ```

2. **Activate venv**
   ```bash
   .venv\Scripts\activate
   ```

3. **Upgrade pip**
   ```bash
   python -m pip install --upgrade pip
   ```

4. **Install core dependencies**
   ```bash
   pip install streamlit scikit-learn nltk joblib
   ```

5. **Confirm installation**
   ```bash
   pip list
   ```

6. **Run Streamlit hello test**
   ```bash
   echo "import streamlit as st; st.title('Hello Streamlit')" > hello.py
   streamlit run hello.py
   ```

✅ **Expected Result:**  
Browser opens → “Hello Streamlit” appears at http://localhost:8501  

---

✅ ## STEP 2 — Create Minimal Chat Loop
*(Verify input/output works before adding ML.)*

1. **Create `sandbox.py`**
   ```bash
   echo. > sandbox.py
   ```

2. **Paste and save this code**
   ```python
   while True:
       user_input = input("You: ")
       if user_input.lower() in ["bye", "exit", "quit"]:
           print("Bot: Goodbye!")
           break
       elif "hi" in user_input.lower():
           print("Bot: Hello there!")
       else:
           print("Bot: I didn't understand that.")
   ```

3. **Run**
   ```bash
   python sandbox.py
   ```

✅ **Expected Result:**  
Terminal responds correctly to “hi” and “bye.”  

---

✅ ## STEP 3 — Build Intents Dataset
*(Define patterns and responses for training.)*

1. **Create `intents.py`**
   ```bash
   echo. > intents.py
   ```

2. **Paste this starter content**
   ```python
   intents = [
       {"tag": "greeting",
        "patterns": ["Hi", "Hello", "Hey"],
        "responses": ["Hi there!", "Hello!", "Hey!"]},
       {"tag": "goodbye",
        "patterns": ["Bye", "Goodbye", "See you later"],
        "responses": ["Goodbye!", "See you soon!"]},
       {"tag": "thanks",
        "patterns": ["Thanks", "Thank you"],
        "responses": ["You're welcome!", "No problem!"]},
       {"tag": "about",
        "patterns": ["Who are you", "What can you do"],
        "responses": ["I'm a simple chatbot built with Python."]}
   ]
   ```

3. **Save file**

✅ **Expected Result:**  
`intents.py` exists and imports without error:  
```bash
python -c "import intents; print(len(intents.intents))"
```  
Output ≥ 4 intents.

---

✅ ## STEP 4 — Train Model (TF-IDF + Logistic Regression)
*(Train and save classifier.)*

1. **Create `ml.py`**
   ```bash
   echo. > ml.py
   ```

2. **Paste this code**
   ```python
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
   ```

3. **Run**
   ```bash
   python ml.py
   ```

✅ **Expected Result:**  
`models/` folder contains `vectorizer.pkl` and `classifier.pkl`.

---

✅ ## STEP 5 — Create Bot Response Logic
*(Connect model to chat function.)*

1. **Create `bot.py`**
   ```bash
   echo. > bot.py
   ```

2. **Paste**
   ```python
   import random
   from joblib import load
   from intents import intents

   vectorizer = load("models/vectorizer.pkl")
   clf = load("models/classifier.pkl")

   def get_response(text, threshold=0.5):
       probs = clf.predict_proba(vectorizer.transform([text]))[0]
       tag_index = probs.argmax()
       confidence = probs[tag_index]
       if confidence < threshold:
           return "I'm not sure I understand."
       tag = clf.classes_[tag_index]
       for intent in intents:
           if intent["tag"] == tag:
               return random.choice(intent["responses"])
   ```

3. **Test**
   ```bash
   python -c "from bot import get_response; print(get_response('hello'))"
   ```

✅ **Expected Result:**  
Prints a valid response like “Hi there!”  

---

✅ ## STEP 6 — Build Streamlit UI
*(Web interface for conversation.)*

1. **Create `app.py`**
   ```bash
   echo. > app.py
   ```

2. **Paste**
   ```python
   import streamlit as st
   from bot import get_response

   st.title("End-to-End Chatbot")
   st.write("Type a message and press Enter:")

   if "chat" not in st.session_state:
       st.session_state.chat = []

   user_input = st.text_input("You:")

   if user_input:
       reply = get_response(user_input)
       st.session_state.chat.append(("You", user_input))
       st.session_state.chat.append(("Bot", reply))

   for speaker, msg in st.session_state.chat:
       st.write(f"**{speaker}:** {msg}")
   ```

3. **Run**
   ```bash
   streamlit run app.py
   ```

✅ **Expected Result:**  
Browser shows chat interface; bot responds to input.  

---

✅ ## STEP 7 — Package & Verify
*(Freeze deps and test clean run.)*

1. **Freeze requirements**
   ```bash
   pip freeze > requirements.txt
   ```

2. **Test full flow**
   ```bash
   streamlit run app.py
   ```

3. **Exit chat**
   - Type “bye” → bot responds and session ends.

✅ **Expected Result:**  
End-to-end chatbot runs cleanly with no console errors.

---

✅ ## STEP 8 — Optional Enhancements
*(Future upgrades.)*

1. ✅ Add sidebar confidence slider in Streamlit (Implemented in app.py)
2. ✅ Cache model load with `st.cache_resource` (Implemented in app.py)
3. ⏳ Add lemmatization or lower-casing to preprocessing (Future)
4. ⏳ Expand intents dataset for better accuracy (Future)
5. ⏳ Swap classifier for Sentence-Transformer embeddings (Future)

---

✅ **Final Deliverable:**  
A functional local end-to-end chatbot using Python, TF-IDF + Logistic Regression, and Streamlit.

---

## 🚀 **PROJECT COMPLETION SUMMARY**

### **Status: 100% COMPLETE**

The End-to-End Chatbot project has been successfully completed! All steps from 0-8 have been implemented and verified.

### **🎯 Quick Start Guide (When You Return):**

1. **Activate environment**: `.venv\Scripts\activate` (Windows)
2. **Run the chatbot**: `streamlit run app.py`
3. **Access in browser**: http://localhost:8501
4. **Test conversations**: Try "Hi", "Thanks", "Who are you", "Bye"

### **📝 Key Configuration:**
- **Confidence threshold**: 0.3 (in `bot.py`)
- **ML Model**: TF-IDF + Logistic Regression
- **Intents**: 4 categories (greeting, goodbye, thanks, about)
- **Enhanced UI**: Diagnostics panel, confidence slider, session management

### **🔧 Next Time You Continue:**
Consider implementing any of the enhancement opportunities listed in the "Next Opportunities" section above, such as expanding the intent dataset, adding text preprocessing, or deploying to the cloud.

**Happy Chatting! 🤖💬**

