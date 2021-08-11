import pygame
# colors
WHITE = (255, 255, 255)
GREY = (82, 80, 87)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill(GREY)
pygame.display.set_caption("Blackjack :)")
icon = pygame.image.load("download.jpg")
pygame.display.set_icon(icon)

# fonts
text_font = pygame.font.Font(None, 30)
title_font = pygame.font.Font(None, 50)

# button time
hit_button = title_font.render("Hit", True, BLACK)
hit_button_rect = hit_button.get_rect()
hit_button_rect.center = (280, 400)

stand_button = title_font.render("Stand", True, BLACK)
stand_button_rect = stand_button.get_rect()
stand_button_rect.center = (520, 400)
