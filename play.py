import judge
import random
import re


def ask_for_k_n() -> tuple[int, int]:
    '''Ask user to input k (number of colors) and n (sequence length).'''
    # Enter n and k
    print('Choose k (number of colors) and n (sequence length)!')
    while True:
        k = input('Choose k: ')
        n = input('Choose n: ')
        if k.isdigit() and n.isdigit() and int(k) > 0 and int(n) > 0:
            k = int(k)
            n = int(n)
            break
        else:
            print('k and n should be positive integers! Try again:')

    return k, n


def generate_hidden(k: int, n: int) -> list[int]:
    '''Generate random hidden sequence with k colors and n length.'''
    hidden = [random.randint(1,k) for i in range(1, n+1)]
    return hidden


def ask_for_sequence(k: int, n: int, type='query', hidden=None) -> list[int]:
    '''Ask user to input an integer sequence separated by spaces.'''
    if type == 'query':
        chosen_sequence_type = 'query'
    elif type == 'hidden':
        chosen_sequence_type = 'hidden sequence'

    # Enter query / hidden sequence
    while True:
        try:
            chosen_sequence = input(f'Type your {chosen_sequence_type}: ')

        # Press (ctrl+z) to surrender
        except EOFError:
            print(f'You chose to surrender! The hidden sequence was: {hidden}')
            quit()

        else:
            chosen_sequence = re.match(r'([1-9][0-9]* +)+[1-9][0-9]*$', chosen_sequence)
            if chosen_sequence:
                chosen_sequence = [int(color) for color in chosen_sequence.group(0).split()]
                if judge.validate_sequence(k, n, chosen_sequence, chosen_sequence[:]):
                    if type == 'hidden':
                        print(f'Hidden sequence: {chosen_sequence}')
                    break
            else:
                print('Sequence should consist only of positive integers separated by spaces! Try again:')

    return chosen_sequence
