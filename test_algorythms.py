import automat_encoder
import automat_list
import play
import judge
import matplotlib.pyplot as plt
import numpy as np


def score_model(query_generator, k, n, epsilon=1.0) -> int:
    # Game simulation
    last_query = None
    score = None
    E0 = None
    round_n = 0
    hidden = play.generate_hidden(k, n)

    while True:
        round_n += 1
        new_query, E0 = query_generator(k, n, last_query, score, E0, epsilon=epsilon)
        score = judge.check(k, n, hidden, new_query)
        X1, _ = score
        if X1 == n:
            break
        last_query = new_query

    return round_n


if __name__ == '__main__':
    # Game parameters
    n_games = 1000
    k = 8
    n = 4
    algorythms_scores = []
    max_rounds = 10

    # Algorythms to test
    algorythms = {'List algorythm': automat_list.generate_query,
                  'Encoder algorythm': automat_encoder.generate_query}


    # Score models over n games
    for algorythm in algorythms.values():
        algorythm_scores = []
        # Simulate n games
        for game in range(n_games):
            score = score_model(algorythm, k, n, epsilon=1.0)
            algorythm_scores.append(score)
        algorythms_scores.append(algorythm_scores)

    x = np.linspace(1, n_games, n_games)

    # Plot scores
    fig, axs = plt.subplots(1,2,figsize=(20,10))
    fig.suptitle(f'Algorythm scores over {n_games} games', fontsize=20)

    for i, ax in enumerate(axs.ravel()):
        ax.plot(x, algorythms_scores[i], 'b', label='scores')
        ax.plot([np.min(x), np.max(x)], [np.mean(algorythms_scores[i]), np.mean(algorythms_scores[i])], '--r', label='mean score')
        ax.set_title(f'Algorythm = {list(algorythms.keys())[i]}', fontsize=15)
        ax.set_ylim(bottom=0, top=max_rounds)
        ax.set_xlabel('Number of games', fontsize=15)
        ax.set_ylabel('Number of rounds needed to win', fontsize=15)
        ax.text(len(algorythms_scores[i])-1, np.mean(algorythms_scores[i]), str(np.mean(algorythms_scores[i])))
        ax.legend()
    

    plt.savefig(r'C:\Users\patap\Desktop\Escuela\UW\Semestr1\Wstep_do_informatyki\Projekt2\testplots\test_algorythms_plot.png')