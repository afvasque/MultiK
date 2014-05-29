import pygame
import sys
import random

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Basic Pygame program')

    # Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

    # Display some text
font = pygame.font.Font(None, 36)


    # Blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()

    # Event loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            for i in event.dict:
                print(i, event.dict[i])
            letra = pygame.key.name(event.key)
            text = font.render(letra, 1, (10, 10, 10))
            textpos = text.get_rect()
            textpos.centerx = random.randint(0,800)
            textpos.centery = random.randint(0,600)
            background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()
