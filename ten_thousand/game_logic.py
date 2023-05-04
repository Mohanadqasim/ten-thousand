import random
from collections import Counter


class GameLogic:

    def __init__(self):
        pass

    """
    the below function will take an argument of num_dice and will return a tuple of random numbers between 1-6 and the length of the tuple is the same as the taken argument
    """

    def roll_dice(int):
        list = []
        for i in range(int):
            x = random.randint(1,6)
            list.append(x)
        return tuple(list)
    
    """
    the function below takes argument of a tuple and works as :
    The input to calculate_score function is a tuple of integers that represents a dice roll.
    The output from calculate_score is an integer representing the roll's score according to rules of the game.
    link to the rules :
    https://en.wikipedia.org/wiki/Dice_10000
    """
    
    def calculate_score(tup):
        unbancked_points = 0 
        num_counter=Counter(tup)

######################################### ones and fives ####################################################
        if num_counter[1] == 1:
            unbancked_points += 100
        if num_counter[1] == 2:
            unbancked_points += 200
        if num_counter[5] == 1:
            unbancked_points += 50
        if num_counter[5] == 2:
            unbancked_points += 100

######################################### three of a kind ####################################################
        if num_counter[1] == 3:
            unbancked_points += 1000
        if num_counter[2] == 3:
            unbancked_points += 200
        if num_counter[3] == 3:
            unbancked_points += 300
        if num_counter[4] == 3:
            unbancked_points += 400
        if num_counter[5] == 3:
            unbancked_points += 500
        if num_counter[6] == 3:
            unbancked_points += 600

######################################### four of a kind ####################################################
        if num_counter[1] == 4:
            unbancked_points += 2000
        if num_counter[2] == 4:
            unbancked_points += 400
        if num_counter[3] == 4:
            unbancked_points += 600
        if num_counter[4] == 4:
            unbancked_points += 800
        if num_counter[5] == 4:
            unbancked_points += 1000
        if num_counter[6] == 4:
            unbancked_points += 1200

######################################### five of a kind ####################################################
        if num_counter[1] == 5:
            unbancked_points += 4000
        if num_counter[2] == 5:
            unbancked_points += 800
        if num_counter[3] == 5:
            unbancked_points += 1200
        if num_counter[4] == 5:
            unbancked_points += 1600
        if num_counter[5] == 5:
            unbancked_points += 2000
        if num_counter[6] == 5:
            unbancked_points += 2400

######################################### six of a kind ####################################################
        if num_counter[1] == 6:
            unbancked_points += 8000
        if num_counter[2] == 6:
            unbancked_points += 1600
        if num_counter[3] == 6:
            unbancked_points += 2400
        if num_counter[4] == 6:
            unbancked_points += 3200
        if num_counter[5] == 6:
            unbancked_points += 4000
        if num_counter[6] == 6:
            unbancked_points += 4800
        
######################################### straight ####################################################
        if len(num_counter) == 6:
             unbancked_points = 2000
        
######################################### three pairs ####################################################
        if len(num_counter) == 3 and len(set(num_counter.values())) == 1 and list(set(num_counter.values()))[0] == 2:
             unbancked_points = 1500
        # Double Trips when 2 sets of a 3 of a kind are hit
        if len(num_counter) == 2 and list(set(num_counter.values()))[0] == 3:
             unbancked_points = unbancked_points
        # if len(num_counter) == 3 and all(count == 2 for count in num_counter.values()):
        #     unbancked_points += 1500

        return unbancked_points
    
    def validate_keepers(tup1,tup2):
         """this function will take two tuples and check if the first tuple contain the value from the scond tuple with the same itarrtion"""
         to_test_cheater = list(tup1)
         for i in tup2:
            if i not in to_test_cheater:
                return False             
            index = to_test_cheater.index(i)
            to_test_cheater.pop(index)
         return True
    
    def get_scorers(dices):
        """ this function will take a tuple and return a tuple contain the values that give a score """

        all_dice_score = GameLogic.calculate_score(dices)
        scorers = []
        input_list = list(dices)
        for i,val in enumerate(input_list):
            input_list.pop(i)
            element_score = GameLogic.calculate_score(tuple(input_list))
            if element_score != all_dice_score:
                scorers.append(val)
                input_list.insert(i,val)
            else:
                input_list.insert(i,val)   
        scorers_tuple = tuple(scorers) 
        # print(scorers_tuple)       
        return scorers_tuple


if __name__=="__main__":
    GameLogic.get_scorers((1,2,3,4,5,6))