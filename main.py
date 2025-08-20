print("Rule-based Chatbot")
print()

game_start = True
game_continue = True

responses = {
    "hello" : "Hello there!",
    "how are you?" : "I'm just code, but thanks for asking!",
}

while game_start:
    start_game = input("would you like to enter y/n? ").lower()
    match start_game:
        case "y":
            while game_continue:
                user_chat = input("Say something to the bot. ").lower()

                if user_chat in responses:
                    print(responses.get(user_chat))
                elif user_chat == "exit":
                    print("Bye...")
                    game_continue = False
                    game_start = False
                else:
                    print("Sorry, I don't understand that.")

        case "n":
            print("Bye...")
            game_start = False
        case _:
            print("Invalid input...")