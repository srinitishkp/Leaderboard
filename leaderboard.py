import math
import os
import random
import re
import sys
from collections import OrderedDict

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked=list(OrderedDict.fromkeys(ranked))
    ranked.sort(reverse=True)
    print(ranked)
    print(player)
    for i,valp in enumerate(player):
        if valp not in ranked:
            ranked.append(valp)
            ranked.sort(reverse=True)
            player[i]=ranked.index(valp)+1
        else:
             player[i]=ranked.index(valp)+1
    return player
    
if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(result)
