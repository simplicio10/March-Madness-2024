The code in this repository uses Python to create brackets for the 2024 NCAA Men's and Women's Basketball Tournaments. 

The tool uses the difference between each team's seed to assign odds for each team to win that game. For example, if a 1 seed plays an 8 seed, the probability of winning is assigned based on the spread between the seeds (in this case, 7). As I develop this tool, I will use a more sophisticated metric to assign probabilities. For now, these are the rudimentary probabilities based on spread:

Evenly matched (e.g., 1 seed v 1 seed) = 50%
Difference of 1 = 54%
Difference of 2 = 58%
Difference of 3 = 62%
Difference of 4 = 66%
Difference of 5 = 70%
Difference of 6 = 74%
Difference of 7 = 78%
Difference of 8 = 82%
Difference of 9 = 86%
Difference of 10 = 90%
Difference of 11 = 94%
Difference of 12 = 96%
Difference of 13 = 98%
Difference of 14 = 99%
Difference of 15 = 99.9%