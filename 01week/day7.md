# Angela Yu - Python Course
## Day 7
- I did first bit of coding for hangman game. I will call it [hang-0.1](hang-0.1.py). User selects letter and program goes through randomly selcted word and checks if it's been used. It throws true or false respectively. The request wasn't precisely worded in the comment so I only did the if statement to start of, but corrected while watching solution.
- Another bit of [Hangman](hang-0.11.py) written following day. A little bit of cheating, some unique solutions. I avoided using one of the loops by implementation of this line of code:

word_matrix = ['_'] * word_length

- Set up end_of_game variable on False and added while loop that runs through all the letters and gets player to guess them until no more left and end_of_game is getting switched to True. You can see source code [here](hang-0.2.py).
- I added stages list and tried to add some functionality, but failed for now... To be continued.. Source code [here](hang-0.2.1.py)
- I put Hangman into debugger and I think there is little light in the tunnel...
- I checked my Hangman app with solution. Well, code was right, but wrong indentation and sequence plus I used wrong operator: == instead of =. Very naughty! Source code available [here](hang-0.2.3.py)
- I started final stage of Hangman project. I added [art](hangman_art.py) and [list of words](han_words.py) which is just copying coursebook and importing it to the code.