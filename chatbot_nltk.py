from nltk.chat.util import Chat, reflections # type: ignore

# Define chatbot responses
pairs = [
    [r"(hi|hello|hey)", ["Hello!", "Hey there!", "Hi! How can I help you?"]],
    [r"how are you?", ["I'm good, thanks for asking!", "I'm just a bot, but I'm doing well!"]],
    [r"what is your name?", ["I am a chatbot!", "You can call me ChatBot."]],
    [r"bye|goodbye", ["Goodbye!", "See you later!", "Have a great day!"]],
    [r"(.*)", ["I'm not sure how to respond to that. Can you rephrase?"]],
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Run chatbot
print("ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("ChatBot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("ChatBot:", response)
