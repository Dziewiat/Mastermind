def is_positive_integer(n) -> bool:
    return (isinstance(n, int) and n >= 1)


def validate_sequence(k: int, n: int, hidden: list[int], query: list[int]) -> bool:
    '''This function takes arguments: k - number of colors, n - code length, hidden - 
    - hidden sequence and query - player's guess on the sequence. It evaluates both
    hidden sequence and query for input errors. Returns True if there are no errors.'''

    # Calculate negative and non-integer counts for hidden and query
    hidden_non_integers = [color for color in hidden if not is_positive_integer(color)]
    query_non_integers = [color for color in query if not is_positive_integer(color)]

    # Check for invalid colors in hidden
    if max(hidden) > k:
        print(f'Invalid colors in the hidden code: {[color for color in hidden if color > k]} (max color = {k})')

    # Check for invalid colors in query
    elif max(query) > k:
        print(f'Invalid colors in the query: {[color for color in query if color > k]} (max color = {k})')
    
    # Check if hidden and query lengths match
    elif len(hidden) != len(query):
        print(f'Lengths of hidden code ({len(hidden)}) and query ({len(query)}) don\'t match!')

    # Check for negatives and non-integers in hidden
    elif len(hidden_non_integers) > 0:
        print(f'Invalid colors in the query: {hidden_non_integers} (positive integers only)')

    # Check for negatives and non-integers in query
    elif len(query_non_integers) > 0:
        print(f'Invalid colors in the query: {query_non_integers} (positive integers only)')

    # Check if sequence length matches n
    elif len(hidden) != n:
        print(f'Given sequence length ({len(hidden)}) doesn\'t match n ({n})')

    else:
        return True


def check(k: int, n: int, hidden: list[int], query: list[int]) -> tuple[int,int]:
    '''This function calculates the number of color positions and colors guessed
    correctly and returns a tuple containing both values, respectfully.'''

    # For valid sequences calculate the number of full hits and color hits
    if validate_sequence(k, n, hidden, query):
        full_hits = 0
        color_hits = 0
        hidden_copy = hidden[:]
        query_copy = query[:]

        # Check for full hits
        for h, q in zip(hidden, query):
            if h == q:
                full_hits += 1
                hidden_copy.remove(h)
                query_copy.remove(q)
        
        # Calculate color hits
        for q in query_copy:
            if q in hidden_copy:
                color_hits += 1
                hidden_copy.remove(q)

        return full_hits, color_hits
