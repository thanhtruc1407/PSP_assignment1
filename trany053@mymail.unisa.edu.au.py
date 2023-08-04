import tic_tac_toe_gui
import tkinter

# Display details:   
def display_details():
    print ("File :  tic-tac-toe.py")
    print ("Author :  Tran Nguyen Thanh Truc - Katherine")
    print ("Student Id : 43557")
    print ("Email Id : trany053@mymail.unisa.edu.au")
    print ("Version : 3.11.4")
    print ("This is my own work as defined by the University’s")
    print ("Academic Misconduct policy.")
display_details()

# Ask the user if they want to play the game 
play = input ("\nWould you like to play Tic Tac Toe? [y/n] ")
while play != "y" and play != "n":
    play = input ("Would you like to play Tic Tac Toe? [y/n] ")

if play == "y":
    user_name = input ("Please enter your name: ")

    # The object of the TicTacToeGUI class that renders the GUI.
    # You can use this object to access the methods listed in the specification.
    ttt = tic_tac_toe_gui.TicTacToeGUI(user_name)
    
# Set game played to 0
total_games = 0
draw = 0

# Check for win function
def check_win(slots, letter):
    if slots [0] == letter and slots [1] == letter and slots [2] == letter:
        return True
    elif slots[3] == letter and slots [4] == letter and slots [5] == letter:
        return True
    elif slots [6] == letter and slots [7] == letter and slots [8] == letter:
        return True
    
    elif slots [0] == letter and slots [3] == letter and slots [6] == letter:
        return True
    elif slots [1] == letter and slots [4] == letter and slots [7] == letter:
        return True
    elif slots [2] == letter and slots [5] == letter and slots [8] == letter:
        return True
    
    elif slots [0] == letter and slots [4] == letter and slots [8] == letter:
        return True
    elif slots [2] == letter and slots [4] == letter and slots [6] == letter:
        return True

    return False

# Check conditions to move the computer
def move_computer(ttt):

    # Making a copy of the slots
    slots = list(ttt.slots)
        
    winning_move_found = False
    blocking_move_found = False

    # Check for winning move
    index = 0
    while index < len(slots):
        if slots[index] == "":
            slot[index] == "O"
            if check_win (slots, "O"):
                winning_move_found = True
                ttt.move_computer(index)
                index += 100
            else:
                slot[index] = ""
        index += 1

    # Check for blocking move
    index = 0
    while index < len(slots):          
        if slots[index] == "":
            slot[index] == "X"
            if check_win (slots, "X"):
                blocking_move_found = True
                ttt.move_computer(index)
                index += 100
            else:
                slot[index] = ""
        index += 1

    # Check for corners
    if not winning_move_found and not block_move_found:
        if slots [0] == "":
            ttt.move_computer(0)
        elif slots [2] == "":
            ttt.move_computer(2)
        elif slots [6] == "":
            ttt.move_computer(6)
        elif slots [8] == "":
            ttt.move_computer(8)

        # Check for center
        elif slots [4] == "":
            ttt.move_computer(4)

        # Check for the sides 
        elif slots [1] == "":
            ttt.move_computer(1)
        elif slots [3] == "":
            ttt.move_computer(3)
        elif slots [5] == "":
            ttt.move_computer(5)
        elif slots [7] == "":
            ttt.move_computer(7)

# Check for draws
def check_draw (slots):
    slots = list(ttt.slots)
    
    full_slots = True
    index = 0
    
    while index < len(slots):
        if slots[index] == "":
            full_slots = False
        
        index += 1
        
    return full_slots

# Ask the user if they want to play the game again
def end_game():
    print ("\nThat was fun!")
           
    play = input ("\nPlay again? [y/n] ")
    while play != "y" and play != "n":
        play = input ("\nPlay again? [y/n] ")
    return play

# Display the game's slot 
def display_game(slots):
    print (slots[0], "|", slots[1], "|", slots[2])
    print (slots[3], "|", slots[4], "|", slots[5])
    print (slots[6], "|", slots[7], "|", slots[8])
    

# Main game loop.
while play == "y":
    total_games += 1
    print ("\n---------------------- START GAME ----------------------")

    while not check_win(ttt.slots,"O") and not check_win(ttt.slots,"X") and not check_draw (ttt.slots):
        
        if not ttt.player_turn:
            move_computer(ttt)

        if check_win(ttt.slots, "X"):
            print ("−−−− Player wins! −−−−")
            ttt.imcrement_wins()
            display_game(ttt.slots)
            print ("\n ----------------------- END GAME -----------------------")
        elif check_win(ttt.slots, "O"):
            print ("−−−− Computer wins! −−−−")
            ttt.imcrement_losses()
            display_game(ttt.slots)
            print ("\n ----------------------- END GAME -----------------------")
        elif check_draw (ttt.slots):
            print ("−−−− Draw! −−−−")
            draw += 1
            display_game(ttt.slots)
            print ("\n ----------------------- END GAME -----------------------")

        play = end_game()
  
        # Updates the GUI. DO NOT REMOVE OR MODIFY!
        try:
            ttt.main_window.update()
        except (tkinter.TclError, KeyboardInterrupt):
            quit(0)

if total_games == 1:
    print ("You played", total_games, "game!")
else:
    print ("You played", total_games, "games!")
print (" -> Won:", get_wins())
print (" -> Lost:", get_losses())
print (" -> Drawn", draw)
print ("\nThanks for playing!  :)")



