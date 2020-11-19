import sys
import pygame
import time
from random import randint
from pygame.locals import QUIT, Rect


pygame.init()
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()
fps = 60.0


class Target:
    def __init__(self, x, y, radius, spd, duration):
        self.x = x
        self.y = y
        self.r = radius
        self.spd = spd
        self.t = duration
        self.color = (randint(30, 255), randint(30, 255), randint(30, 255))

    def tick(self):
        self.r += self.spd / fps

    def checkHit(self, x, y):
        return ((self.x-x) ** 2 + (self.y-y) ** 2) ** 0.5 <= self.r

    def draw(self, SURFACE):
        pygame.draw.circle(SURFACE, self.color, (self.x, self.y), int(self.r))


def main():
    sysfont = pygame.font.SysFont(None, 36)

    regendelay = 0.8
    r = 10
    nextregen = time.time()
    stat = 0
    score = 0

    tl = []
    shoot = None

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    shoot = pygame.mouse.get_pos()

        SURFACE.fill((0, 0, 0))

        currenttime = time.time()

        if nextregen <= currenttime:
            tl.append(Target(randint(200, 600), randint(200, 600), 20, randint(10, 30), currenttime+3.0))
            nextregen = currenttime + regendelay

        if 0 == stat:
            for tg in tl:
                tg.tick()
                if shoot and tg.checkHit(shoot[0], shoot[1]):
                    score += 1
                    shoot = None
                    tg.t = 0

            tl = [t for t in tl if t.t > currenttime]
            for tg in tl[::-1]:
                tg.draw(SURFACE)

            scoretext = sysfont.render(f"{score}", True, (255, 255, 255))
            SURFACE.blit(scoretext, (10, 10))
            pygame.display.update()

        FPSCLOCK.tick(fps)


if __name__ == '__main__':
    main()
