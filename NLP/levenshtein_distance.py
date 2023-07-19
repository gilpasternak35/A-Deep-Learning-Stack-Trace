import argparse
from typing import List


def levenshtein_distance(string1: str, string2: str) -> int:
    """
    Returns Levenshtein distance between two given strings
    """
    # ensuring string2 is longer of the two strings, swapping if this is not the case
    if len(string1) > len(string2):
        string1, string2 = string2, string1

    # computing necessary additions
    necessary_additions = len(string2) - len(string1)

    # computing naive solution - pure substitutions and necessary additions, with aligned subs having cost 0
    naive_solution = max(len(string1), len(string2)) - compute_aligned_chars(string1, string2)

    # to maintain best improvement
    best_improvement  = 0

    # computing offset by trying every possible offset given an insertion (at most k insertions make sense at all, where k is naive solution)
    # algorithm should run in quadratic time, which is worse than DP. However, shows an interesting thought exercise
    for j in range(len(string1)):
        # temporarily modifying string1 so as to see how many commonalities we can create
        # field theory: should be able to have insert characters only in beginning. Alignment anywhere will result from insertion at beginning
        string2 = string1[:j] + string2
        best_improvement = max(best_improvement, compute_aligned_chars(string1, string2) - j)


    # best solution is naive = best improvement we could make by aligning common chars
    return naive_solution - best_improvement
        

            


def compute_aligned_chars(s1: str, s2: str):
    """
    Returns number of corresponding positional characters in two strings
    """
    return sum([s1[i] == s2[i] for i in range(min(len(s1), len(s2)))])


if __name__ == "__main__":
    # obtaining arguments with argparse
    parser = argparse.ArgumentParser("Levenshtein Distance", description="Computes Levenshtein Distance between two given strings")
    parser.add_argument("-s1", type=str, help="First string", required=False, default="Mary had a little lamb")
    parser.add_argument("-s2", type=str, help="Second string", required=False, default="Mary had a large lamb, wow what a world")
    args = parser.parse_args()

    # printing Levenshtein distance
    print(levenshtein_distance(args.s1, args.s2))


