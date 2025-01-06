from itertools import product
import numpy as np
import judge


def score_query_diversity(query: list[int], k: int) -> int:
    # Prefer queries with more different colors
    score = 0
    colors = []
    for color in query:
        if color not in colors:
            colors.append(color)
            score += k  # Score scaled by number of possible colors -> values similar to ranking values in score_query_frequency()

    return score


def score_query_frequency(query: list[int], E0_encoded: np.array) -> int:
    # Prefer colors most frequent on certain positions in E0
    color_scores = np.argsort(E0_encoded, axis=0)
    score = 0
    # Add color frequency ranking values in all positions to score
    for position, color in enumerate(query):
        score += np.where(color_scores[:, position] == color-1)[0][0]

    return score


def generate_query(k: int, n: int, last_query: list[int] = None,
                   response: tuple[int,int] = None, E0: list[list[int]] = None,
                   epsilon: float = 1.0) -> list[int]:
    '''Algorythm to generate a query based on the frequency of occurence of a given color in 
    a specific position in the set of eligable sequences (E0). Returns the new query and the new
    set of eligable sequences (E1).'''
    if last_query:
        X0, Y0 = response  # X0 - full hits, Y0 - color hits in the previous round
        E1 = []  # Set of new eligable sequences
        E1_encoded = np.zeros((k,n))  # Color position count matrix for eligable sequences
        # Iterate through the set of previous eligable sequences
        # Check for new eligable sequences
        for sequence in E0:
            X1, Y1 = judge.check(k, n, sequence, last_query)
            if X0 == X1 and Y0 == Y1:
                E1.append(sequence)
                # Count occurence of specific colors in specific positions
                for i, color in enumerate(sequence):
                    E1_encoded[color-1,i] += 1
        
        # Generate new query from new eligable sequences (E1)
        # Score queries by color frequencies in E1 eligability matrix and query diversity (exploitation vs exploration)
        # epsilon (default = 1.0) parameter controls diversity score influence on sequence choice
        top_score = 0
        for query in E1:
            score = score_query_frequency(query, E1_encoded) + epsilon * score_query_diversity(query, k)
            if score > top_score:
                new_query = query
                top_score = score

    else:
        new_query = [i%k+1 for i in range(n)]  # Initial fixed guess (preferably without duplicates -> high exploration)
        E1 = [list(sequence) for sequence in product([i for i in range(1, k+1)], repeat=n)]  # All possible combinations

    return new_query, E1