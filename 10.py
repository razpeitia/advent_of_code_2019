from itertools import combinations, cycle
from collections import defaultdict
import math
import pygame, sys
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BOX = (20, 20, WHITE)

def translate(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1 - x2), (y1 - y2)

def polar(p1, p2):
    y, x = translate(p1, p2)
    t = math.atan2(y, x)
    t += math.pi / 2
    if t < 0:
        t += 2 * math.pi
    t = round(t, 3)
    return (math.hypot(x, y), t, p1)

def render_map(window, M, BOX, best, target, destroyed):
    W, H, C = BOX
    m = len(M)
    n = len(M[0])
    for i in range(m):
        for j in range(n):
            if M[i][j] == '#' and (i, j) not in destroyed:
                c = RED if (i, j) == best else C
                pygame.draw.rect(window, c, ((j * W * 1.5 + 10, i * H * 1.5 + 10), (W, H)))
    if target is not None:
        x1 = best[1] * W * 1.5 + 10
        y1 = best[0] * H * 1.5 + 10
        x2 = target[2][1] * W * 1.5 + 10
        y2 = target[2][0] * H * 1.5 + 10
        pygame.draw.rect(window, RED, ((x2, y2), (W, H)))
        pygame.draw.line(window, RED, (x1, y1), (x2, y2))


def main():
    with open("input10.txt") as f:
        M = [list(line.strip()) for line in f]
    m = len(M)
    n = len(M[0])
    asteroids = [(i, j) for i in range(m) for j in range(n) if M[i][j] == '#']
    best = (11, 11)
    asteroids = [a for a in asteroids if a != best]
    pp = [polar(p, best) for p in asteroids]
    d = defaultdict(list)
    for p in pp:
        d[p[1]].append(p)
    
    angles = cycle(sorted(set([p[1] for p in pp])))
    destroyed = set()

    pygame.init()
    window = pygame.display.set_mode((1024, 768), 0, 32)
    pygame.display.set_caption('Day 10; Part 2')

    clock = pygame.time.Clock()
    target = None
    pygame.key.set_repeat(32, 64)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key in (K_q, K_ESCAPE):
                    pygame.quit()
                    return
                if event.key == K_SPACE:
                    while len(destroyed) < len(asteroids):
                        a = next(angles)
                        if not d[a]: continue
                        target = min(d[a], key=lambda p: p[0])
                        destroyed.add(target[2])
                        d[a].remove(target)
                        print(len(destroyed), target[2][::-1])
                        break
        window.fill(BLACK)
        render_map(window, M, BOX, best, target, destroyed)
        pygame.display.update()
        clock.tick(60)


main()