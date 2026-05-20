###############################################################################
#Title: Splunking Game
#Version: 005
###############################################################################
import diver
import highscore    


def introduction():
    print("Welcome!...")
    highscore.getHighScore()
    print(f"Current high score: {highscore.highScore}")


def action():
    print("Choose one of the following options:")
    print(" - Enjoy the Sights (enjoy)")
    print(" - Search for Treasure (search)")
    print(" - Quit the Game (quit)")
    choice = input("Choice: ").lower()
    if choice == "enjoy":
        scuba_steve.enjoy()
    elif choice == "search":
        scuba_steve.search()
    elif choice == "quit":
        ending()
        quit()
    else:
        print("not an option...try again")


def game():
    introduction()
    # Game Ending Conditions.
    while scuba_steve.tank.air>0 \
    and len(scuba_steve.bag.inventory)<scuba_steve.bag.capacity:
        action()    
    print("Returned to the surface.")
    scuba_steve.calculate_score()
    ending()


def ending():
    print("Good-bye...")


# Main -------------------------------------------------------------------------
scuba_steve = diver.Diver("Steve", 5, 3)

game()