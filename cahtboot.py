print("Chatbot: hi! whats your name? ")

name = input("you:")

print(f"chatbot: nice to meet you , {name}!")

while True:
    user_input  = input(f"{name}:").lower()
    if "hi" in user_input or "hello" in user_input:
        print ("Chatboot: hi! there ")
    elif "how are you" in user_input:
        print("chatbot: I am just code, but i am feeling fast!")
    elif "bye" in user_input:
        print("Chatbot: Goodbye!")
        break

    else:
        print("Chatbot: Hmm... i dont understand  that... ")