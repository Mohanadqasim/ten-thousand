from ten_thousand.game_logic import GameLogic
# from game_logic import GameLogic
dice_roller = GameLogic.roll_dice
calculate_points = GameLogic.calculate_score
validate_keepers = GameLogic.validate_keepers
get_scorers = GameLogic.get_scorers


def play(roller =GameLogic.roll_dice,num_rounds=10):
    """
    this function starts the game and asks the user if he wants to play or not
    
    """
    global dice_roller
    dice_roller = roller
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    response = input("> ")
    if response == "y":
        start_game(num_rounds)
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


    



def start_game(num_rounds,round=1, total_score=0, dices_num=6, points=0, new_round=True):
    """this function starts the rounds when the user type y to start the game"""

    if new_round:
        print("Starting round {}".format(round))
    first_roll = dice_roller(dices_num)
    dices = " ".join(str(x) for x in first_roll)
    print("Rolling {} dice...\n*** {} ***".format(dices_num, dices))

    if calculate_points(first_roll) == 0:
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")
        print("You banked 0 points in round {}".format(round))
        print("Total score is {} points".format(total_score))
        if round == num_rounds:
            return end_game(total_score)
        round += 1
        points = 0
        return start_game(num_rounds,round, total_score, dices_num=6)
    

    print("Enter dice to keep, or (q)uit:")
    user_choice = input('> ').replace(' ', '')

    if user_choice == "q":
        end_game(total_score)

    else:
        dices_to_keep = tuple(int(x) for x in user_choice)
        cheat_test = validate_keepers(first_roll, dices_to_keep)
        check_hot_dice = get_scorers(dices_to_keep)
        if len(check_hot_dice) == 6:
            points += calculate_points(dices_to_keep)

        while not cheat_test:
            print("""Cheater!!! Or possibly made a typo...""")
            print("*** {} ***".format(dices))
            print("Enter dice to keep, or (q)uit:")
            user_choice = input('> ')

            if user_choice == "q":
                return end_game(total_score)

            else:
                dices_to_keep = tuple(int(x) for x in user_choice if x.isdigit())
                cheat_test = validate_keepers(first_roll, dices_to_keep)


        if len(dices_to_keep) != 6:
            dices_num = dices_num - len(dices_to_keep)
            points += calculate_points(dices_to_keep)

        print("You have {} unbanked points and {} dice remaining".format(points, dices_num))
        print("(r)oll again, (b)ank your points or (q)uit:")
        user_choice = input('> ')

        if user_choice == 'q':
            end_game(total_score)
        elif user_choice == 'r':
            if dices_num > 0:
                start_game(num_rounds,round, total_score, dices_num, points, new_round=False)
            else:
                # print('~~ WASTED ~~')
                # round += 1
                start_game(num_rounds,round, total_score, dices_num=6, points=points,new_round=False)
        elif user_choice == "b":
            bank(num_rounds,round, total_score, points)


def bank(num_rounds,round, total_score, points):
    """this function bank points when the user type b to store his point"""

    total_score += points
    print("You banked {} points in round {}\nTotal score is {} points".format(points, round, total_score))
    if round == num_rounds:
       return end_game(total_score)
    round += 1
    # print('Starting round {}'.format(round))
    start_game(num_rounds,round, total_score)


def end_game(points):
    """this function print a string when the player type q"""
    print("Thanks for playing. You earned {} points".format(points))


if __name__ == "__main__":
    play()