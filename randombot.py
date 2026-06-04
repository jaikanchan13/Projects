import random
responses= ["hi", "hello", "how are you"]

while True:
    question = input("You: ").lower()
    if question == "bye":
        print("Bot: GoodBye")
        break
    print ("Bot: "+random.choice(responses))