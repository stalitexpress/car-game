print("~~~~~~~~~~~~ CAR GAME ~~~~~~~~~~~~")
print("Type ';help' for help with commands")
# Variables command and started
command = ""
started = False
inCar = False
# Main code
while True:
    command = input(";")
    if command.lower() == "enter":  # Enter car command
        if inCar:
            print("You are already in the car.")
        elif inCar is False:
            inCar = True
            print("Entering the car... ")
    elif command.lower() == "exit":
        if inCar:
            inCar = False
            print("Exiting the car... ")
        elif inCar is False:
            print("You are already out of the car.")
    if command.lower() == "start":  # Start command
        if started:
            if inCar:
                print("The car is already started.")
        elif inCar:
            started = True
            print("Starting the car... ")
        else:
            print("You must be in the car to start it.")
        if command.lower() == "stop":  # Stop command
            if not started:
                print("The car is already stopped.")
            if started:
                started = False
                print("Stopping the car... ")
    elif command.lower() == "help":  # Help command
        # Help command output
        print("1. ';start' Starts the car.")
        print("2. ';stop' Stops the car.")
        print("3. ';steer_r' Steers the car right.")
        print("4. ';steer_l' Steers the car left.")
        print("5. ';enter' Enters the car. (Hint: First command.)")
        print("6. ';exit' Exits the car.")
        print("7. ';quit' or ';q' Quits the game.")
        print("8. ';help' Lists commands.")
    elif command.lower() == "steer_r":
        if not started:
            print("You must start the car to steer.")
        else:
            print("Steering right!")
    elif command.lower() == "steer_l":
        if not started:
            print("You must start the car to steer.")
        else:
            print("Steering left!")
    elif command.lower() == "q" or command.lower() == "quit":
        print("Quitting the game...")
        break
    else:
        print("Invalid command. Type ;help for help.")

# End of program
