print("Play Ur Car Now")
isStop, hasStarted = True, False
helpDisplay = """
start - to start the car
stop - to stop the car
status - show your car status
quit - to exit
"""

while True:
    choice = input("> ").lower()
 
    if choice == "help":
        print(helpDisplay)
    elif choice == "start":
        if isStop:
            print("Car started... ready to go!")
            isStop, hasStarted = False, True
        else:
            print("WDYM? Ur car already started!")
    elif choice == "stop":
        if isStop and hasStarted:
            print("Heyy ur car already stopped!")
        elif isStop and not hasStarted:
            print("U not even start the car yet, dumbass!")
        else:
            print("Car stopped")
            isStop = True
    elif choice == "status":
        if isStop:
            print("Currently, your car stopped.")
        else:
            print("Your car already started...")
    elif choice == "quit":
        break
    else:
        print("I dont understand that")