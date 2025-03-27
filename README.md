# Queens Solver

This is a solver for the LinkedIn game [Queens](https://www.linkedin.com/games/queens/). My goal is to use this as an example of a "no goal" PuLP program. That is, a PuLP program that is not trying to minimize or maximize any number but to simply come up with a valid solution.

## Adjacency Constraints

With a 2x2 grid there are:

- 2 Vertical constraints
- 2 Horizontal constraints
- 2 Diagonal constraints

With a 3x3 grid there are:

- 6 Vertical constraints
- 6 Horizontal constraints
- 8 Diagonal constraints

With a 4x4 grid there are:

- 12 Vertical constraints
- 12 Horizontal constraints
- 18 Diagonal constraints

The diagonal constraints appear to follow [this pattern](https://oeis.org/A001105).

## Next Steps

### Visual Output

I need some way of displaying a Queens game as an image. Whatever I use for rendering, it would be nice to also be able to display the location of the Queens themselves after the game is solved.

### Board Editor

Some way of clicking and dragging on tiles to increase the boundary of a color. That seems like the fastest way.

### Image into board

This seems pretty difficult, but if it worked it would be the fastest way to load a Queens game into the solver.

### Detect if more than one solution

I'm very sure that [this](https://www.queens-game.com/?map=map87) game of queens has more than 1 solution. I would like to be able to test a game of Queens to detect if more than one solution is possible. It could also be cool to then generate Queens games with only a single solution.
