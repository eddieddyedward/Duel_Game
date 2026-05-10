Duel Game

Overview
Simulation of a turn-based duel between two characters.

Character Setup
Each character starts with:
• 100 health
• A random attack power (between 15 and 20)
• A random defense power (between 10 and 15)

Special Abilities
Each character has a special ability, assigned randomly. An ability has a 25% chance of
activation on each relevant round.
The abilities are:
1. Damage Reduction: When the character is attacked, it takes only half damage
2. Power Strike: When the character attacks, it attacks with 50% more power
3. Second Wind: If an attack brings the character below 30 health, it heals itself by 5
You can either assign one ability at the start of the game that the character keeps throughout,
or assign a new random ability each round.

Combat Rules
1. It is selected randomly which character attacks first.
2. The attacking character deals damage equal to its attack power. The defending
character reduces the incoming damage by its defense power. The resulting value is
subtracted from the defender's health.
3. The roles are then reversed and the other character attacks.
4. The fight continues in alternating rounds until one character reaches 0 health.

Extension

1. Run the simulation 1,000 times and print win rates for each character configuration
2. Accept a command-line flag to toggle between fixed and per-round ability assignment
