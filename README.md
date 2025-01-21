Welcome to the exciting Mastermind Game!

The goal of the game is to guess a hidden sequence of colors. Choose to play either as a player or as a judge against one of 3 solving algorythms.


To play as a player run:

- master_play.py
  

To test 3 different playing algorythms run:

- master_automat_list.py (base time efficient algorythm)

The algorythm generates a set of eligable sequences every round. Sequence eligability is determined based on the fact, that all eligable sequences should get the same score when compared to the last query, as the score got from comparing the last query to the hidden sequence. This guarantees, that the eligable sequences have only color frequencies that are indicated by the last rounds score. Each round the set of eligable sequences is generated based on the set from the previous round (genetic algorythm), which causes the set to get smaller with every round. At the end of the round the next query is randomly selected from eligable sequences.

- master_automat_encoder (upgraded list algorythm)

The algorythm generates a set of eligable sequences every round in the same way as the list algorythm. In addition, instead of selecting a query randomly, queries are scored by two factors:

1. Query diversity - diversity score is proportional to the number of unique colors present in the query.
2. Color frequency - for every eligable sequences set, a frequency matrix (n x k) is calculated. The matrix encodes how many times a certain color occurs at a certain position in the sequence. Frequency score is proportional to the frequency of occurence of the queries colors at certain positions in the eligable sequences set.

The query with the highest score: frequency_score + epsilon * diversity_score (epsilon is a parameter used to control diversity score's influence on the frequency score - see epsilon value testing in test_epsilon.py) is chosen as the next query. This algorythm is an upgraded version of the list algorythm (see test_algorythms.py).

- master_automat_generator (memory efficient version of list algorythm)

The algorythm generates the set of eligable sequences every round, but instead of using a set stored in the memory it uses a generator. The only values stored by the Automat class are previous queries and scores. Every round, last query and score are added to the memory, then the generator calculates next query eligability by comparing its scores with scores and queries from previous rounds. This algorithm has a worse time complexity, but uses a lot less memory, which can be beneficial with larger eligable sequences sets.


Experimental Neural Network Reinforcement Learning model:

- Mastermind_RL.ipynb


Enjoy!
