#!/usr/bin/env python3
"""Snake game logic engine (no GUI)."""
import sys, random
from collections import deque

class SnakeGame:
    def __init__(self, width=20, height=15, seed=None):
        self.w, self.h = width, height
        self.rng = random.Random(seed)
        self.snake = deque([(height//2, width//2)])
        self.direction = (0, 1)  # right
        self.food = None
        self.score = 0
        self.game_over = False
        self._place_food()
    def _place_food(self):
        snake_set = set(self.snake)
        free = [(r,c) for r in range(self.h) for c in range(self.w) if (r,c) not in snake_set]
        self.food = self.rng.choice(free) if free else None
    def set_direction(self, dr, dc):
        if (dr + self.direction[0], dc + self.direction[1]) != (0, 0):
            self.direction = (dr, dc)
    def tick(self):
        if self.game_over: return
        hr, hc = self.snake[0]
        nr, nc = hr + self.direction[0], hc + self.direction[1]
        if nr < 0 or nr >= self.h or nc < 0 or nc >= self.w:
            self.game_over = True; return
        if (nr, nc) in set(list(self.snake)[1:]):
            self.game_over = True; return
        self.snake.appendleft((nr, nc))
        if (nr, nc) == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()
    def to_string(self):
        snake_set = set(self.snake)
        lines = []
        for r in range(self.h):
            row = ""
            for c in range(self.w):
                if (r, c) == self.snake[0]: row += "@"
                elif (r, c) in snake_set: row += "o"
                elif (r, c) == self.food: row += "*"
                else: row += "."
            lines.append(row)
        return chr(10).join(lines)

def test():
    g = SnakeGame(10, 10, seed=42)
    assert not g.game_over
    assert len(g.snake) == 1
    assert g.food is not None
    for _ in range(3):
        g.tick()
    assert not g.game_over
    assert len(g.snake) >= 1
    # Test wall collision
    g2 = SnakeGame(5, 5, seed=1)
    g2.set_direction(0, 1)  # right
    for _ in range(10):
        g2.tick()
    assert g2.game_over  # should hit wall
    s = g.to_string()
    assert "@" in s
    print("  snake_logic: ALL TESTS PASSED")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print("Snake game logic engine")
