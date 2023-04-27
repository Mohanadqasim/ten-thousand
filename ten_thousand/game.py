from ten_thousand.game_logic import GameLogic
dice_roller = GameLogic.roll_dice
calculate_points = GameLogic.calculate_score
total=0


def play(roller =GameLogic.roll_dice):
    """
    this function starts the game and asks the user if he wants to play or not
    
    """
    global dice_roller
    dice_roller = roller
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    response = input("> ")
    if response == "y":
        start_game()
    elif response == "n":
        quitter()
    else:
        print("invalid input")
        play(roller =GameLogic.roll_dice)





def quitter():
    """
    this function quit the ten thousand game if user's response is "q" without playing any round
    
    """
    print("OK. Maybe another time")


    



def start_game(round=1,total_score=total,dices_num = 6):
    """
    this function is responsible for rolling the 6 dices and saving the dices that user wants to keep and calclate their points and :
    1-playing the next round without banking the points by responding with 'r'
    2-playing the next round and have the points banked by responding with 'b'
    3-quit the game by responding with 'q'
    """

    
    first_roll = dice_roller(dices_num)
    dices = " ".join(str (x) for x in first_roll)
    print("Starting round {}\nRolling {} dice...\n*** {} ***".format(round, dices_num, dices))
    

    if calculate_points(first_roll) == 0 or dices_num == 0:
        print("~~ WASTED ~~")
        round += 1       
    else:
        print("Enter dice to keep, or (q)uit:")
        user_response = input("> ")
        if user_response == "q":
            end_game(total_score)
        else:
            kept_dices = tuple(int (x) for x in user_response)
            dices_num= dices_num-len(kept_dices)
            score = calculate_points(kept_dices)
            
            # for i in kept_dices:
            #     if i not in dices:
            #         print("~~ WASTED ~~")
            #         return start_game(round=1,total_score=total,dices_num = 6)
                
            print("You have {} unbanked points and {} dice remaining".format(score, dices_num))
            print("(r)oll again, (b)ank your points or (q)uit:")

            user_choice = input("> ")

            if user_choice == "q":
                end_game(total_score)
            elif user_choice == "r":
                if dices_num > 0 :
                    total_score += score
                    start_game(round,total_score,dices_num)
                else:
                    print("~~ WASTED ~~")
                    round+=1
                    start_game(round=1,total_score=total,dices_num = 6)
                
            elif user_choice == "b":
                bank(score,round,total_score)






def bank(score,round,total_score):
    """
    this function is responsible for saving the points for the user and start the next round
    
    """
    total_score += score
    print("You banked {} points in round {}\nTotal score is {} points".format(score,round,total_score))
    round += 1
    start_game(round,total_score)






def end_game(points):
    """
    this function quit the ten thousand game whenever user's response is "q"
    
    """
    print("Thanks for playing. You earned {} points".format(points))

if __name__ == "__main__":
    play()