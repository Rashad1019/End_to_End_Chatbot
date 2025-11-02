intents = [
    {"tag": "greeting",
     "patterns": ["Hi", "Hello", "Hey", "Good morning", "Good afternoon", "Good evening", "What's up", "Howdy", "Greetings", "Sup", "Hiya", "Yo"],
     "responses": ["Hi there!", "Hello!", "Hey!", "Good day!", "Greetings!", "Hi! How can I help you?"]},
    
    {"tag": "goodbye",
     "patterns": ["Bye", "Goodbye", "See you later", "See you", "Take care", "Catch you later", "Gotta go", "Later", "Bye bye", "Talk to you later", "I'm leaving", "Have to go"],
     "responses": ["Goodbye!", "See you soon!", "Take care!", "Bye bye!", "Until next time!", "Have a great day!"]},
    
    {"tag": "thanks",
     "patterns": ["Thanks", "Thank you", "Thank you so much", "Thanks a lot", "I appreciate it", "Cheers", "Thx", "Appreciate it", "Thanks a bunch", "Much appreciated", "Thank you very much"],
     "responses": ["You're welcome!", "No problem!", "Happy to help!", "Anytime!", "My pleasure!", "Glad I could help!", "Don't mention it!"]},
    
    {"tag": "about",
     "patterns": ["Who are you", "What can you do", "What are you", "Tell me about yourself", "What is your purpose", "Who made you", "Introduce yourself", "What do you do"],
     "responses": ["I'm a simple chatbot built with Python.", "I'm an AI assistant here to chat!", "I'm a machine learning chatbot built with TF-IDF and Logistic Regression.", "I'm your friendly chatbot assistant!"]},
    
    # NEW INTENT 1
    {"tag": "name",
     "patterns": ["What's your name", "What is your name", "Your name", "Do you have a name", "How should I call you", "What do they call you"],
     "responses": ["I'm Chatbot!", "You can call me Chatbot.", "My name is Chatbot!", "I go by Chatbot."]},
    
    # NEW INTENT 2
    {"tag": "age",
     "patterns": ["How old are you", "What's your age", "When were you created", "When were you born", "Your age"],
     "responses": ["I'm timeless!", "I was just created recently!", "Age is just a number for bots like me.", "I'm brand new!"]},
    
    # NEW INTENT 3
    {"tag": "help",
     "patterns": ["Help", "Can you help me", "I need help", "What can you help with", "Support", "Assist me", "I need assistance"],
     "responses": ["I'm here to help! What do you need?", "Sure! How can I assist you?", "I'd be happy to help! What's up?", "Tell me what you need help with."]},
    
    # NEW INTENT 4
    {"tag": "hobbies",
     "patterns": ["What are your hobbies", "What do you like to do", "Do you have hobbies", "What do you enjoy", "What's your favorite activity"],
     "responses": ["I love chatting with people like you!", "I enjoy answering questions!", "Talking to you is my favorite hobby!", "I like helping people and having conversations."]},
    
    # NEW INTENT 5
    {"tag": "joke",
 "patterns": ["Tell me a joke", "Make me laugh", "Do you know any jokes", "Say something funny", "Can you be funny", "Joke please", "tell joke", "give me a joke", "I want a joke", "joke", "funny joke", "be funny", "say a joke"],
 "responses": ["Why don't programmers like nature? It has too many bugs!", "Why did the chatbot go to therapy? It had too many issues!", "I told my computer a joke... but it didn't laugh. It had no sense of humor!"]},
    
    # NEW INTENT 6
    {"tag": "feelings",
     "patterns": ["How are you", "How are you doing", "How do you feel", "Are you okay", "What's up with you", "How's it going"],
     "responses": ["I'm doing great, thanks for asking!", "I'm functioning perfectly!", "I'm excellent! How are you?", "I'm wonderful! Thanks for asking."]},
    
    # NEW INTENT 7
    {"tag": "weather",
     "patterns": ["What's the weather", "How's the weather", "Is it sunny", "Will it rain", "Weather forecast", "Is it cold outside"],
     "responses": ["I can't check the weather, but I hope it's nice where you are!", "I'm not connected to weather services yet.", "I don't have weather data, sorry!"]},
    
    # NEW INTENT 8
    {"tag": "time",
     "patterns": ["What time is it", "What's the time", "Tell me the time", "Do you know the time", "Current time"],
     "responses": ["I don't have access to the current time, sorry!", "I can't tell time yet!", "Time is a mystery to me!"]},
    
    # NEW INTENT 9
    {"tag": "compliment",
     "patterns": ["You're awesome", "You're great", "You're cool", "I like you", "You're smart", "You're helpful", "Good job"],
     "responses": ["Thank you! You're awesome too!", "That's so kind of you to say!", "Thanks! I really appreciate that!", "You just made my day!"]},
    
    # NEW INTENT 10
    {"tag": "insult",
     "patterns": ["You're dumb", "You're stupid", "You're useless", "I hate you", "You're annoying", "You're bad"],
     "responses": ["I'm sorry you feel that way. How can I do better?", "I'm still learning! Let me know how I can improve.", "I apologize if I upset you. What can I help with?"]}
]