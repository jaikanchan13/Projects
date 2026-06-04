responses = {
    "hi" : "Hello!",
    "major" : "Computer Science",
    "school" : "University of Virginia",
    "age" : "10"
}

def respond(question):
    if question in responses:
        return responses[question]
while True:

    question = input("You: ").lower()

    if question == "bye":
        print("Bot: Goodbye!")
        break
    elif question in responses:
        print("Bot: " + respond(question))
    else:
        print("Bot: I dont understand")