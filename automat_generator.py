from itertools import product
from judge import check


class Automat:

    def __init__(self, k: int, n: int):
        self.k = k
        self.n = n
        self.n_possible = pow(k,n)  # Number of possible sequences
        self.len_E0 = self.n_possible
        self.query_memory = []
        self.score_memory = []


    def generate_E0(self, last_query: list[int] = None, response: tuple[int, int] = None):
        self.len_E0 = 0
        i = 0

        sequences = product([color for color in range(1, self.k+1)], repeat=self.n)

        if last_query:
            self.query_memory.append(last_query)
            self.score_memory.append(response)

            while i < self.n_possible:
                i += 1
                sequence = list(next(sequences))
                # Check if sequence passes conditions from all previous rounds
                conditions = [(check(self.k, self.n, sequence, query) == score)*1 for query, score in zip(self.query_memory, self.score_memory)]
                # If all conditions are passed, yield sequence
                if min(conditions) == 1:
                    self.len_E0 += 1

                    yield sequence
        
        else:
            while i < self.n_possible:
                i += 1
                self.len_E0 += 1

                yield list(next(sequences))
    

    @staticmethod
    def score_sequence(sequence: list[int]) -> int:
        # Prefer sequences with more different colors -> TRY DIFFERENT STRATEGY
        score = 0
        colors = []
        for color in sequence:
            if color not in colors:
                colors.append(color)
                score += 1

        return score


    def generate_query(self, last_query: list[int] = None, response: tuple[int,int] = None) -> list[int]:
        top_score = 0
        for sequence in self.generate_E0(last_query, response):
            score = self.score_sequence(sequence)
            if score > top_score:
                top_score = score
                new_query = sequence

        return new_query