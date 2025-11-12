import pygame, sys
from button import Button
import time

pygame.init()
pygame.mixer.init()

IdentityBackground = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/Charts/IdentityBG.png")
GameplayOverlay = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/gameplay-field.png")
PressedCircle = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/circle_pressed.png")

def start_identity_part4(screen):
    pygame.mixer.music.load("/Users/evaldsberzins/pygame/RayRhythm/Charts/Identity-Part-4.wav")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer_music.play()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        screen.blit(IdentityBackground, (0, 0))
        screen.blit(GameplayOverlay, (0, 0))
        
        if keys[pygame.K_d]:
            screen.blit(PressedCircle, (903.5, 882.2))
        if keys[pygame.K_f]:
            screen.blit(PressedCircle, (1079.2, 882.2))
        if keys[pygame.K_j]:
            screen.blit(PressedCircle, (1251.6, 882.2))
        if keys[pygame.K_k]:
            screen.blit(PressedCircle, (1424, 882.2))


        pygame.display.flip()
