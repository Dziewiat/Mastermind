import play
import judge


print('Welcome to the Mastermind Game! The rules are simple:')
print('Guess the hidden sequence of k colors and n positions!')
print('*Press (ctrl+d) to surrender\n')
k, n = play.ask_for_k_n()
hidden = play.generate_hidden(k, n)

# Play the game
print(f'Colors to choose from: {[color+1 for color in range(k)]}')
X_seq = 'X '*n
print(f'Hidden sequence: {X_seq}')

round_n = 0
MAX_ROUNDS = 10

while True:
    round_n += 1
    if round_n > MAX_ROUNDS:
        print('Maximum amount of rounds reached! You lose!')
        break
    new_query = play.ask_for_sequence(k, n, type='query', hidden=hidden)
    score = judge.check(k, n, hidden, new_query)
    X1, Y1 = score
    print(f'ROUND {round_n} ||| Query: {new_query} | full  hits: {X1}, color hits: {Y1}')
    if X1 == n:
        print('Congratulations! Hidden sequence guessed!')
        break