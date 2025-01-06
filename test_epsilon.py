import automat_encoder
from test_algorythms import score_model
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    # Game parameters
    n_games = 1000
    k = 8
    n = 4
    algorythm = automat_encoder.generate_query
    epsilons = [0, 0.5, 1, 1.25, 1.5, 2]
    epsilon_scores = []
    max_rounds = 10

    x = np.linspace(1, n_games, n_games)

    for epsilon in epsilons:
        algorythm_scores = []

        # Simulate n games
        for game in range(n_games):
            score = score_model(algorythm, k, n, epsilon=epsilon)
            algorythm_scores.append(score)

        epsilon_scores.append(algorythm_scores)

    
    # Plot scores
    fig, axs = plt.subplots(2,3,figsize=(30,20))
    fig.suptitle(f'Encoder algorythm scores over {n_games} games', fontsize=20)

    for i, ax in enumerate(axs.ravel()):
        ax.plot(x, epsilon_scores[i], 'b', label='scores')
        ax.plot([np.min(x), np.max(x)], [np.mean(epsilon_scores[i]), np.mean(epsilon_scores[i])], '--r', label='mean score')
        ax.set_title(f'Epsilon = {epsilons[i]}', fontsize=15)
        ax.set_ylim(bottom=0, top=max_rounds)
        ax.set_xlabel('Number of games', fontsize=15)
        ax.set_ylabel('Number of rounds needed to win', fontsize=15)
        ax.text(len(epsilon_scores[i])-1, np.mean(epsilon_scores[i]), str(np.mean(epsilon_scores[i])))
        ax.legend()
    

    plt.savefig(r'C:\Users\patap\Desktop\Escuela\UW\Semestr1\Wstep_do_informatyki\Projekt2\testplots\test_epsilon_plot.png')