import sys
import pygame
import time
from random import randint
from pygame.locals import QUIT, Rect


pygame.init()
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()
fps = 60.0


def main():
    sysfont = pygame.font.SysFont(None, 36)

    y = 20.0
    spd = 0.0
    acc = 1500.0

    x = 800.0
    mv = -300.0

    stat = 0

    l = Rect(100, 20, 50, 50)
    r = Rect(800, -300, 30, 600)
    q = Rect(800, 500, 30, 600)

    upper = Rect(0, -20, 800, 20)
    lower = Rect(0, 600, 800, 20)
    vert = Rect(-220, 0, 20, 600)

    begin = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    spd = -750.0
                elif event.key == pygame.K_r:
                    stat = 0
                    r = Rect(800, -300, 30, 600)
                    q = Rect(800, 500, 30, 600)

                    y = 20.0
                    spd = 0.0
                    acc = 1500.0

                    x = 800.0
                    mv = -300.0

                    stat = 0

                    begin = time.time()

        if stat == 0:
            SURFACE.fill((0, 0, 0))

            spd += acc / fps
            y += spd / fps
            l.y = int(y)

            if r.colliderect(vert):
                x = 800.0
                nh = randint(-600, -200)
                r.y = nh
                q.y = nh+800

            x += mv / fps
            r.x = int(x)
            q.x = int(x)

            if l.colliderect(r) or l.colliderect(q) or l.colliderect(upper) or l.colliderect(lower):
                stat = 1

            pygame.draw.rect(SURFACE, (255, 0, 0), l)
            pygame.draw.rect(SURFACE, (255, 255, 0), r)
            pygame.draw.rect(SURFACE, (255, 255, 0), q)

            current = time.time()
            elapsedtime = sysfont.render("%.2f" % (current-begin), True, (255,255,255))
            SURFACE.blit(elapsedtime, (10,10))

            pygame.display.update()

        FPSCLOCK.tick(fps)


if __name__ == '__main__':
    main()
