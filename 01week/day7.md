# Angela Yu - Python Course
## Day 7
- I did first bit of coding for hangman game. I will call it [hang-0.1](hang-0.1.py). User selects letter and program goes through randomly selcted word and checks if it's been used. It throws true or false respectively. The request wasn't precisely worded in the comment so I only did the if statement to start of, but corrected while watching solution.
- Another bit of [Hangman](hang-0.11.py) written following day. A little bit of cheating, some unique solutions. I avoided using one of the loops by implementation of this line of code:

word_matrix = ['_'] * word_length

- Set up end_of_game variable on False and added while loop that runs through all the letters and gets player to guess them until no more left and end_of_game is getting switched to True