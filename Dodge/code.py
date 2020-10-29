import sys
import pygame
from random import randint
from pygame.locals import QUIT, Rect


pygame.init()
SURFACE = pygame.display.set_mode((400, 600))
FPSCLOCK = pygame.time.Clock()
fps = 60.0


def main():
    regen = 0.1
    count = regen

    dirts = []
    acc = 500.0
    lower = Rect(0, 620, 400, 100)

    px = 200.0
    lmv = -300.0
    rmv = -lmv

    lb = 0
    rb = 0

    pr = Rect(int(px), 560, 20, 40)

    sysfont = pygame.font.SysFont(None, 36)

    stat = 0
    dodged = [0]

    def addDirt(dirts):
        dx = randint(0, 380)
        dy = 0.0

        r = Rect(dx, int(dy), 20, 20)
        n = [r, dy, dy]
        dirts.append(n)

    def moveDirts(dirts, dodged):
        for i in dirts:
            i[2] += acc / fps
            i[1] += i[2] / fps
            i[0].y = int(i[1])

            if i[0].colliderect(lower):
                dodged[0] += 1

        return [i for i in dirts if not i[0].colliderect(lower)]

    def isDead(dirts, pr):
        for i in dirts:
            if pr.colliderect(i[0]):
                return True
        return False


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    lb = 1 if event.type == pygame.KEYDOWN else 0
                elif event.key == pygame.K_RIGHT:
                    rb = 1 if event.type == pygame.KEYDOWN else 0
                elif event.key == pygame.K_r and event.type == pygame.KEYDOWN:
                    count = regen
                    dirts = []
                    px = 200.0
                    pr = Rect(int(px), 560, 20, 40)
                    stat = 0
                    dodged[0] = 0

        SURFACE.fill((0, 0, 0))

        if 0 == stat:
            count -= 1.0 / fps

            if count <= 0.0:
                count = regen
                addDirt(dirts)

            dirts = moveDirts(dirts, dodged)

            px += (lb * lmv + rb * rmv) / fps
            px = min(380.0, max(0.0, px))
            pr.x = int(px)

            if isDead(dirts, pr):
                stat = 1

            pygame.draw.rect(SURFACE, (255, 0, 0), pr)
            for i in dirts:
                pygame.draw.rect(SURFACE, (255, 255, 0), i[0])
            txt = sysfont.render(f"{dodged[0]}", True, (255, 255, 255))
            SURFACE.blit(txt, (10, 10))

            pygame.display.update()

        FPSCLOCK.tick(fps)


if __name__ == '__main__':
    main()
