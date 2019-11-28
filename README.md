Implement a performance-measuring environment simulator for the vacuum-cleaner world.
This world can be described as follows:

- **Percepts:** Each vacuum-cleaner agent gets a three-element percept vector on each turn.
The first element, a touch sensor, should be a 1 if the machine has bumped into something
and a 0 otherwise. The second comes from a photosensor under the machine, which emits
a 1 if there is dirt there and a 0 otherwise. The third comes from an infrared sensor, which
emits a 1 when the agent is in its home location, and a 0 otherwise.

- **Actions:** There are five actions available: go forward, turn right by 90 , turn left by 90 ,
suck up dirt, and turn off.

- **Goals:** The goal for each agentis to clean up and go home. To be precise,the performance
measure will be 100 points for each piece of dirt vacuumed up, minus 1 point for each
action taken, and minus 1000 points if it is not in the home location when it turns itself off.

- **Environment:** The environment consists of a grid of squares. Some squares contain
obstacles (walls and furniture) and other squares are open space. Some of the open squares
contain dirt. Each “go forward” action moves one square unless there is an obstacle in that
square, in which case the agent stays where it is, but the touch sensor goes on. A “suck up
dirt” action always cleans up the dirt. A “turn off” command ends the simulation.

We can vary the complexity of the environment along three dimensions:

- **Room shape:** In the simplest case, the room is an n n square, for some fixed n. We can
make it more difficult by changing to a rectangular, L-shaped, or irregularly shaped room,
or a series of rooms connected by corridors.

- **Furniture:** Placing furniture in the room makes it more complex than an empty room. To
the vacuum-cleaning agent, a piece of furniture cannot be distinguished from a wall by
perception; both appear as a 1 on the touch sensor.

- **Dirt placement:** In the simplest case, dirt is distributed uniformly around the room. But
it is more realistic for the dirt to predominate in certain locations, such as along a heavily
travelled path to the next room, or in front of the couch.