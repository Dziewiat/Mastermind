import random
from itertools import product
from judge import check


def score_sequence(sequence: list[int]) -> int:
        # Prefer sequences with more different colors -> TRY DIFFERENT STRATEGY
        score = 0
        colors = []
        for color in sequence:
            if color not in colors:
                colors.append(color)
                score += 1

        return score


def generate_query(k: int, n: int, last_query: list[int] = None,
                   response: tuple[int,int] = None, E0: list[list[int]] = None,
                   epsilon=None) -> list[int]:
    if last_query:
        X0, Y0 = response  # X0 - full hits, Y0 - color hits in the previous round
        E1 = []  # Set of new eligable combinations
        # Iterate through the set of previous eligable sequences
        top_score = 0
        # Check for new eligable sequences
        for sequence in E0:
            X1, Y1 = check(k, n, sequence, last_query)
            if X0 == X1 and Y0 == Y1:
                E1.append(sequence)
        
        # Generate new query from eligable sequences RANDOMLY -> TRY DIFFERENT STRATEGY (scoring)
        new_query = random.sample(E1, 1)[0]
        # new_query = E1[0]

    else:
        new_query = [random.randint(1,k) for i in range(1, n+1)]  # Initial guess
        E1 = [list(sequence) for sequence in product([i for i in range(1, k+1)], repeat=n)]  # All possible combinations

    return new_query, E1