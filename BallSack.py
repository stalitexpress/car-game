print("~~~~~~~~~~~~ CAR GAME ~~~~~~~~~~~~")
print("Type ';help' for help with commands")

# Variables command and started

const command = ""
const started = False

# Main code

while True:
    command = input(";")
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
            print(":Stopped car... ")  # Stop command output
    elif command.lower() == "help":  # help command

        # Help command output

        print("1. ';start' Starts the car; ")
        print("2. ';stop' Stops the car; ")
        print("3. ';steer_r' Steers the car right; ")
        print("4. ';steer_l' Steers the car left; ")
        print("5. ';quit/;q' Quits the game; ")
        print("6. ';help' Lists commands; ")

        # Steer function

    elif command.lower() == "steer_r":
        if not started:
            print("Car must be started to steer! ")
        else:
            print("Steering right! ")
    elif command.lower() == "steer_l":
        if not started:
            print("Car must be started to steer! ")
        else:
            print("Steering left! ")
    elif command.lower() == "q":
        print("Quitting... ")
        break
    elif command.lower() == "quit":
        print("Quitting... ")
        break
    else:
        print("Invalid command. Type ';help' for a list of commands")
