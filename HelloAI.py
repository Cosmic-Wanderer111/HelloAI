# Greet the user
print("Hello there! I am AI Bot. May I know your name please? : ")

# Get user input
name = input("Enter your name: ")

# Respond to the user's name
print(f"Hello {name}, Nice to meet you!")

# Ask a question
print("How are you feeling today? (good/bad) : ")
mood = input().lower()

# Use conditional statements to respond based on input
if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
else:
    print("I see. Sometimes it's hard to put feelings into words.")

# End the conversation
print(f"It was nice chatting with you {name}. Goodbye!")