import argparse
from typing import List
import numpy as np


def levenshtein_distance(string1: str, string2: str, subs_weight:float) -> int:
    """
    A DP Style soltuion for levenshtein edit distance
    """
    # two pronged array with strings as indices
    table = np.zeros((len(string1), len(string2)))
    
    # iterating through dp table and populating entries
    for i in range(table.shape[0]):
        for j in range(table.shape[1]):

            # special case where cannot rely on predecessor, so must evaluate match. Best option is either subs or deletion+insertion
            if i == 0 and j == 0:
                table[i][j] = 0 if string1[i] == string2[j] else min(subs_weight, 2)
            
            # otherwise, checking best path from a predecessor
            else:
                # if common char, don't need to use a formal substitution to make transition
                if string1[i] == string2[j]:
                    # maintaining sub cost
                    subs_cost = table[i-1, j-1] if i > 0 and j > 0 else np.infty
                else:
                    subs_cost = table[i-1, j-1] + subs_weight if i > 0 and j > 0 else np.infty

                # computing min addition, subtraction cost
                del_cost = table[i-1, j] + 1 if i > 0 else np.infty
                add_cost = table[i, j-1] + 1 if j > 0 else np.infty

                # updating table with the minimum of all three costs
                table[i,j] = min(subs_cost, del_cost, add_cost)

    # returning final entry
    print(table)
    return table[-1][-1]


if __name__ == "__main__":
    # obtaining arguments with argparse
    parser = argparse.ArgumentParser("Levenshtein Distance", description="Computes Levenshtein Distance between two given strings")
    parser.add_argument("-s1", type=str, help="First string", required=False, default="Mary had a little lamb")
    parser.add_argument("-s2", type=str, help="Second string", required=False, default="Mary had a large lamb, wow what a world")
    parser.add_argument("-s-weight", type=float, help="The weight of a substition", required=False, default=1)
    args = parser.parse_args()

    # printing Levenshtein distance
    print(levenshtein_distance(args.s1, args.s2, args.s_weight))


