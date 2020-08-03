# Tug of War

## Introduction
2-player Tug-of-War game implemented with LEDs and buttons, and managed by a Raspberry Pi 4 via GPIO.

Each round, players will battle to click their button before their opponent.
The rope (represented by LEDs) will nudge one step towards the person that clicked too slow.
A player wins when the rope has reached their opponent's side.

- Implements:

  - Startup sequence
  - Reset
  - Win sequence
  - Rounds starting randomly either 1s or 2s
  - Ability to play again

- Areas for improvements:

  - Currently left has the advantage because when a button is clicked, the left player's button is checked first. Game will still perform well as the script runs much faster than the players click, but it would be optimal if this was fixed so that both players have a fair chance. A listener would work.

  - Currently implements while loops to check player activity which is extremely resource-hungry - implement listeners instead.

## Motivation
Inspired from a Tug of War implementation I built for university using an FPGA.
The electrical implementation was an involved process - especially with analyzing timing diagrams when race conditions were ever-present, and it had a substantially large project base for a relatively simple game.

So, I wanted to see how a python script would compare in terms of size and performance building the same game on the Raspberry Pi with the GPIO module and a few LEDs.
