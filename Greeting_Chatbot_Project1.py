import random

#Define a rule dictionary for generating greetings
greeting_rule = {
    "greeting" : ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Hello! What brings you here today?"],
    "how_are_you" : ["I'm doing well, thank you for asking!", "I'm great! How about you?", "I'm fine, thanks for checking in!"],
    "name" : ["My name is AI Assistant.", "You can call me AI Assistant.", "I go by the name AI Assistant."],
    "bye" : ["Goodbye! Have a great day!", "See you later! Take care!", "Farewell! Hope to talk to you soon!"]
}

def generate_greeting(user_input: str) -> str:
    """Generate a random greeting based on the specified category."""

    if any(keyword in user_input.lower() for keyword in ["hello","hi","hey","hy"]):
        return random.choice(greeting_rule["greeting"])
    elif any(keyword in user_input.lower() for keyword in ["how are you","how's it going"]):
        return random.choice(greeting_rule["how_are_you"])
    elif any(keyword in user_input.lower() for keyword in ["what's your name","who are you"]):
        return random.choice(greeting_rule["name"])
    elif any(keyword in user_input.lower() for keyword in ["bye","goodbye","see you"]):
        return random.choice(greeting_rule["bye"])
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"

#chat loop
print("Welcome to the AI Greeting Assistant! Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("AI: Goodbye! Have a great day!")
        break
    response = generate_greeting(user_input)
    print(f"AI: {response}")
