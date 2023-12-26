# Day 2: Balls
This days puzzle should have been the first day judging by the difficulty.
We are given a list of games. Each game is a consecutive list of balls being drawn from a bag and put back in.

Part one requires you to select all Games, that are possible within a given constraint.
This constraint is that the maximum number of balls cannot exceed 12 (for red balls), 13 (for green) and 14 (for blue). As we only get the minimum number of balls per game, one can only exclude games that have definitely more balls drawn in their color, than the maximum allows.

Iterating over all games and checking if the given ball number is below the maximum satisfies the constraint.

## Part 2
Part 2 removes the constraint and instead wants us to find the minimum number of balls per game.
The minimum number of balls that need to be present per game is the maximum number of balls we see during each game.
Again, this is done with a simple iteration.