# Pong Game

A simple recreation of the classic Pong game using Python and the `turtle` module. This project includes the core features of Pong: paddle control, ball movement, collision detection, and score tracking. 

## Project Overview

This project implements a two-player Pong game using the `turtle` graphics library. Players control paddles to keep the ball in play, and score when the ball passes their opponent's paddle.

The game is run on a simple GUI window and is controlled using keyboard inputs.

## Features

- **Two Player Controls**: 
  - Player 1 controls the left paddle with the 'W' (up) and 'S' (down) keys.
  - Player 2 controls the right paddle with the 'Up Arrow' (up) and 'Down Arrow' (down) keys.
  
- **Ball Mechanics**:
  - The ball starts in a random direction.
  - The ball bounces off the top and bottom walls and rebounds when it hits the paddles.
  - The ball speeds up after each paddle collision.

- **Score Tracking**:
  - The game tracks points for both players and displays the score on the screen.
  - Points are awarded when the ball passes the opponent’s paddle.
