print("Welcome to the car game! Enter commands...")
print("enter 'help' to see the commands available")
started = False
while True:
    command = input(">").lower()
    if command == 'start':
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started...")
    elif command == 'stop':
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == 'quit':
        break
    else:
        print("Sorry! I don't understand that!")

# Welcome to the car game! Enter commands...
# enter 'help' to see the commands available
# > help
#
# start - to start the car
# stop - to stop the car
# quit - to quit
#
# > start
# Car started...
# > start
# Car is already started.
# > stop
# Car stopped.
# > stop
# Car is already stopped!
# > quit
#
# Process finished with exit code 0