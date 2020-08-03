# Tug of War

## Introduction
2-player Tug-of-War game implemented with LEDs and buttons, and managed by a Raspberry Pi 4 via GPIO.

Each round, players will battle to click their button before their opponent.
The rope (represented by LEDs) will nudge one step towards the player that clicked too slow.
A player wins when the rope has reached their opponent's side (4 steps)

Requires:

  - Raspberry Pi
  - Breakout Expansion Board
  - Ribbon Cable
  - Assembled T Type GPIO Adapter
  - Breadboard
  - 7x LEDs
  - 2x buttons

- Implements:

  - 4-step tug-of-war game
  - Reset
  - Startup, win sequence
  - Rounds starting randomly either 1s or 2s
  - Ability to play again

- Areas for improvements:

  - Currently left has the advantage because the left player's button is checked first when a button is clicked. Game will still perform well as the script runs much faster than the players' clicks, but it would be optimal if this was fixed so that the game is completely fair. A listener would work.

  - Currently implements while loops to check player activity which is extremely resource-hungry - implement listeners instead.

## Motivation
Inspired from a Tug of War implementation I built for university using an FPGA.
The electrical implementation was an involved process - especially with analyzing timing diagrams when race conditions were ever-present, and it had a substantially large project base for a relatively simple game.

So, I wanted to see how a python script would compare in terms of size and performance building the same game on the Raspberry Pi with the GPIO module and a few LEDs.
