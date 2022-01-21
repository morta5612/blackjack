import pygame
pygame.init()

width = 600
height = 600
white = (255, 255, 255)
black = (0, 0, 0)

display = pygame.display.set_mode((width, height))
iconimg = pygame.image.load("cards.png")
pygame.display.set_icon(iconimg)
pygame.display.set_caption("Blackjack")

clock = pygame.time.Clock()
crashed = False
titleimg = pygame.image.load("titlecards.png")


def titlecards(xcord, ycord):
    display.blit(titleimg, (xcord, ycord))


x = (width * 0.3)
y = (height * 0.3)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

    display.fill(white)
    titlecards(x, y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
