while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break
    elif "hi" in user_input.lower():
        print("Bot: Hello there!")
    else:
        print("Bot: I didn't understand that.")


