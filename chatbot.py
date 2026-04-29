# -------- CHATBOT --------

# predefined responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! How can I help you?",
    "how are you": "I'm just a bot, but I'm functioning perfectly!",
    "what is your name": "I am a simple customer service chatbot.",
    "thanks": "You're welcome! Let me know if you need more help.",
    "bye": "Goodbye! Have a great day!"
}

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Chatbot:", responses["bye"])
        break

    response_found = False

    for key in responses:
        if key in user_input:
            print("Chatbot:", responses[key])
            response_found = True
            break

    if response_found == False:
        print("Chatbot: I'm sorry, I don't understand that. Can you try rephrasing?")