# battleship
This is a battleship game.

I was forced to abandon a lot of the validation code. The number of ships and the number of each type of ship, and non-collision between the ships, was not implemented.

I had to rebuild the data structure holding the game state when I realized that I could shoot the same part of a ship twice and score hits. This led to  a change from storing the root coordinate and its orientation and type, to the Ship/ShipPart classes I used here. This made hit totalling easier, but hit totals would have been trivial. I didn't feel comfortable storing some place every shot taken ane making sure shots weren't duplicated; I'm not sure why that felt wrong. Shot duplication is allowed anywhere on the board; disabling that would have solved the whole problem.

In any case, there were minimum mechanics that were required before making additional AI experimentation possible. It was about 4, 4:30 when I spoke with Igor and realized that I should stop working on mechanics and at least attempt better AI algorithms. I created the one where it fires randomly but follows up a hit with a search pattern. I did not extensively debug that. I also came up with an AI that is described but not implemented to try and target the largest untargeted areas.

An additional feature the AI could use would be notice that a specific ship had been sunk. The UI feedback could tell this to the user, but the AI needs to be notified "The cruiser has been sunk" to potentially take into account that only the destroyer remains and empty spaces of less than 3 spaces can be disregarded. Etc.
