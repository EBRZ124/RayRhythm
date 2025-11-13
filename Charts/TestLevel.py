import pygame, sys
from button import Button
import time

pygame.init()
pygame.mixer.init()

TestBackground = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/Charts/test-level-background.png")
GameplayOverlay = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/gameplay-field.png")
PressedCircle = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/circle_pressed.png")
RegularCirlce = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/circle_regular.png")

def start_test_level(screen):
    pygame.mixer.music.load("/Users/evaldsberzins/pygame/RayRhythm/Charts/test-level.wav")
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
        screen.blit(TestBackground, (0, 0))
        screen.blit(GameplayOverlay, (0, 0))
        screen.blit(RegularCirlce, (890, 880))
        screen.blit(RegularCirlce, (1070, 880))
        screen.blit(RegularCirlce, (1250, 880))
        screen.blit(RegularCirlce, (1430, 880))

        if keys[pygame.K_d]:
            screen.blit(PressedCircle, (890, 880))
        if keys[pygame.K_f]:
            screen.blit(PressedCircle, (1070, 880))
        if keys[pygame.K_j]:
            screen.blit(PressedCircle, (1250, 880))
        if keys[pygame.K_k]:
            screen.blit(PressedCircle, (1430, 880))


        pygame.display.flip()