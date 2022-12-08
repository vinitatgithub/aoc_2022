"""
--- Day 2: Rock Paper Scissors ---

The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant
Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each
simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected:
Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the
round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say
will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and
C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores
for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3
for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get
if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you
with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for
you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round
needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the
round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also
choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly
according to your strategy guide?
"""

filename = "day02.txt"
# filename = "day02_sample.txt"
# optimized code https://github.com/judifer/aoc_2022
game = [x.strip() for x in open(filename).readlines()]
part_one = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
part_two = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
print(f"Part one: {sum(part_one[i] for i in game)} | Part two: {sum(part_two[i] for i in game)}")

# my code
with open(filename, 'r') as filehandle:
    total1 = 0
    total2 = 0
    for line in filehandle:
        decisions = line.strip().split(" ")

        # Score for what you chose
        total1 += 1 if decisions[1] == "X" else 2 if decisions[1] == "Y" else 3
        # Score for the round outcome
        if line.strip() == "A Y" or line.strip() == "B Z" or line.strip() == "C X":
            total1 += 6
        elif line.strip() == "A Z" or line.strip() == "B X" or line.strip() == "C Y":
            pass
        else:
            total1 += 3

        # Score the round outcome
        total2 += 0 if decisions[1] == "X" else 3 if decisions[1] == "Y" else 6
        # Score for what you chose
        if line.strip() == "A Y" or line.strip() == "B X" or line.strip() == "C Z":  # chose rock
            total2 += 1
        elif line.strip() == "A Z" or line.strip() == "B Y" or line.strip() == "C X":
            total2 += 2
        else:
            total2 += 3


print("Part one: " + str(total1) + " | Part two: " + str(total2))
