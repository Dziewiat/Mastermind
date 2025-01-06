import re
import automat_list
import judge


# Enter n and k
while True:
    k = input('Choose k: ')
    n = input('Choose n: ')
    if k.isdigit() and n.isdigit() and int(k) > 0 and int(n) > 0:
        k = int(k)
        n = int(n)
        break
    else:
        print('k and n should be positive integers! Try again:')

# Enter hidden sequence
while True:
    hidden = input('Choose hidden sequence: ')
    hidden = re.match(r'([1-9][0-9]* +)+[1-9][0-9]*$', hidden)
    if hidden:
        hidden = [int(color) for color in hidden.group(0).split()]
        if judge.validate_sequence(k, n, hidden, hidden[:]):
            print(f'Hidden sequence: {hidden}')
            break
    else:
        print('Sequence should consist only of positive integers separated by spaces! Try again:')

# Game simulation
last_query = None
score = None
E0 = None
round_n = 0

while True:
    round_n += 1
    new_query, E0 = automat_list.generate_query(k, n, last_query, score, E0)
    print(f'Number of possible sequences left: {len(E0)}')
    score = judge.check(k, n, hidden, new_query)
    X1, Y1 = score
    print(f'ROUND {round_n} ||| Query: {new_query} | full  hits: {X1}, color hits: {Y1}')
    if X1 == n:
        print('Hidden sequence guessed!')
        break
    last_query = new_query