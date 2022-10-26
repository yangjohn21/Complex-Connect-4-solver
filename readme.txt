John Yang

My tournament bot name is "co-lateral"

The thinking behind my evaluation function was to look at the empty spaces where a piece may eventually end up.
Looking at these empty spaces, if they border a piece of a certain player, that player would be more likely to get points.
As such, my evaluation function increments the value (from the perspective of player 1) of a move if player one's piece borders the empty space on 
a side (one increment for every side) and decrements the value if player two's piece borders that side. It also utilizes the GameState class's
utility function as a means of determining the current point advantage of player 1 in this position.
The function is utility value + sides of empty squares that border player 1's piece - sides of empty squares that border player 2's piece.

your_test is designed to test that minimax and prune give the correct move in a very simple scenario.
your_tester is designed to test that minimax and prune give the same result (point totals) in a more complicated game GameState
your_testest is designed to test the effectiveness of my lookn function against other altn evaluation functions

