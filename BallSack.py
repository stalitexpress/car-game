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
            print("Already in car! ")
        else:
            inCar = True
            print("Entering car... ")
    elif command.lower() == "exit":
        if inCar:
            inCar = False
            print("Exiting car... ")
        else:
            print("Already out of car! ")
    
    if inCar:  # Check if inCar is True before allowing start and stop commands
        if command.lower() == "start":  # Start command
            if started:
                print("Car is already started! ")  # Start command stop
            else:
                started = True
                print("Started car... ")  # Start command output
        elif command.lower() == "stop":  # Stop command
            if not started:
                print("Car is already stopped! ")  # Stop command stop
            else:
                started = False
                print("Stopped car... ")  # Stop command output
        elif command.lower() == "steer_r":  # Steer right command
            if not started:
                print("Car must be started to steer! ")
            else:
                print("Steering right! ")
        elif command.lower() == "steer_l":  # Steer left command
            if not started:
                print("Car must be started to steer! ")
            else:
                print("Steering left! ")
    elif command.lower() == "help":  # help command
        # Help command output
        print("1. ';start' Starts the car. ")
        print("2. ';stop' Stops the car. ")
        print("3. ';steer_r' Steers the car right. ")
        print("4. ';steer_l' Steers the car left. ")
        print("5. ';enter' Enters the car. Hint; first command; ")
        print("6. ';exit' Exits the car; ")
        print("7. ';quit/;q' Quits the game. ")
        print("8. ';help' Lists commands. ")
    elif command.lower() == "q" or command.lower() == "quit":  # Quit command
        print("Quitting... ")
        break
    else:
        print("Invalid command. Type ';help' for a list of commands")
