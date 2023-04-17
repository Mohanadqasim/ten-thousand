import random
from collections import Counter


class GameLogic:
    def __init__(self):
        pass

    def roll_dice(int):
        list = []
        for i in range(int):
            x = random.randint(1,6)
            list.append(x)
        return tuple(list)
    
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
        if len(num_counter) == 3 and all(count == 2 for count in num_counter.values()):
            unbancked_points += 1500

        return unbancked_points