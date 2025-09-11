while True:
    command = input(">")
    print("ECHO ", command)
    if command.lower == "quit":
        break                        # Infinite loops run forever. It can be caused issues