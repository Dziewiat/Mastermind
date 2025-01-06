import automat_encoder
import judge
import play


# Enter n and k
k, n = play.ask_for_k_n()

# Enter hidden sequence
hidden = play.ask_for_sequence(k, n, type='hidden')

# Game simulation
last_query = None
score = None
E0 = None
round_n = 0

while True:
    round_n += 1
    new_query, E0 = automat_encoder.generate_query(k, n, last_query, score, E0)
    print(f'Number of possible sequences left: {len(E0)}')
    score = judge.check(k, n, hidden, new_query)
    X1, Y1 = score
    print(f'ROUND {round_n} ||| Query: {new_query} | full  hits: {X1}, color hits: {Y1}')
    if X1 == n:
        print('Hidden sequence guessed!')
        break
    last_query = new_query