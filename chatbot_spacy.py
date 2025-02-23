import spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Chatbot responses
responses = {
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm just a chatbot, but I'm doing great!",
    "what is your name": "I'm a chatbot powered by spaCy!",
    "bye": "Goodbye! Have a great day!",
}

def get_response(user_input):
    doc = nlp(user_input.lower())
    for key in responses:
        if key in doc.text:
            return responses[key]
    return "I'm not sure how to respond to that. Can you rephrase?"

# Chat loop
print("ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("ChatBot:", responses["bye"])
        break
    response = get_response(user_input)
    print("ChatBot:", response)
