#!/usr/bin/env python3
"""Snake game logic."""
import random
from collections import deque
class Snake:
    def __init__(self,w=20,h=15):
        self.w=w;self.h=h;self.snake=deque([(h//2,w//2)])
        self.direction=(0,1);self.food=None;self.score=0;self.game_over=False;self._place_food()
    def _place_food(self):
        free=[(r,c) for r in range(self.h) for c in range(self.w) if (r,c) not in self.snake]
        self.food=random.choice(free) if free else None
    def set_direction(self,dr,dc):
        if (dr,dc)!=(-self.direction[0],-self.direction[1]): self.direction=(dr,dc)
    def step(self):
        if self.game_over: return
        hr,hc=self.snake[-1];nr,nc=hr+self.direction[0],hc+self.direction[1]
        if nr<0 or nr>=self.h or nc<0 or nc>=self.w or (nr,nc) in self.snake:
            self.game_over=True;return
        self.snake.append((nr,nc))
        if (nr,nc)==self.food: self.score+=1;self._place_food()
        else: self.snake.popleft()
if __name__=="__main__":
    random.seed(42);s=Snake(10,10)
    dirs=[(0,1),(1,0),(0,-1),(-1,0)]
    for i in range(100):
        if s.game_over: break
        if i%5==0: s.set_direction(*dirs[(i//5)%4])
        s.step()
    print(f"Snake: score={s.score}, length={len(s.snake)}, steps={i}")
    print("Snake OK")
