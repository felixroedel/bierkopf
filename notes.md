# Game

- partially observable (hidden cards)
- multiagent
- deterministic
- static (round based but cards never change in one playout)
- discrete

# Game Rules

## How to make a "Stich"

1. Highest trump card wins
2. If no trump card is played, the highest card of the same suit wins

## Definition of the game structure

- Stich: each player plays one card
- Round: all cards in a hand are played, round can either be won or lost (60> points needed to win) <- AI is trained
  here
- Game: rounds are played until a team reached >= 21 points

# Strategy analysis

## What can a player certainly know?

- Their hand
- The cards that have been played
- The cards that are left in the deck
- The points they/their opponents have scored
- The number of trumps left in the deck
- The suits that have been played
- The suits that have not been played
- If their teammate/opponents still don't have trumps left
- If their teammate/opponents still don't have cards of a certain suit left

## What can a player speculate about?

- The cards in their teammate's/opponents' hand

# Todo

- [] Implement game logic
- [] Implement MCTS
- [] Implement MCTS with Reinforcement Learning
- [] Make network make decisions on real hands and game states
- [] Implement computer vision to detect real hands
