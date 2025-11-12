import pygame, sys
from button import Button

pygame.init()
pygame.mixer.init()

IdentityBackground = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/Charts/IdentityBG.png")
GameplayOverlay = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/gameplay-field.png")

def start_identity_part4(screen):
    pygame.mixer.music.load("/Users/evaldsberzins/pygame/RayRhythm/Charts/Identity-Part-4.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer_music.play()

    running = True
    player = pygame.Rect(100, 100, 50, 50)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_RIGHT]:
            player.x += 5
        if keys[pygame.K_LEFT]:
            player.x -= 5

        screen.blit(IdentityBackground, (0, 0))
        screen.blit(GameplayOverlay, (0, 0))
        pygame.draw.rect(screen, "red", player)

        pygame.display.flip()