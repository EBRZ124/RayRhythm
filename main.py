import pygame, sys
from button import Button

pygame.init()

screen = pygame.display.set_mode((1680, 1050))
pygame.display.set_caption("Menu")

BackGround1 = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/background2.jpg")

# Music generator
pygame.mixer_music.load("/Users/evaldsberzins/pygame/RayRhythm/sounds/main_menu_music.mp3")

def get_main_menu_font(size):
    return pygame.font.Font("/Users/evaldsberzins/pygame/RayRhythm/fonts/Blastge DEMO VERSION.ttf", size)

def play():
    while True:
        pygame.mixer_music.stop()
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_TEXT = get_main_menu_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(840, 360))
        screen.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(840, 560), text_input="BACK", font=get_main_menu_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        
        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_main_menu_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(840, 360))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(840, 540), 
                            text_input="BACK", font=get_main_menu_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.mixer_music.play()
    pygame.mixer_music.set_volume(0.2)
    while True:
        screen.blit(BackGround1, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_main_menu_font(100).render("RayRhythm", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center=(840, 200))
        TEXT_BG = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/Title-Rect.png").convert_alpha()
        TEXT_BG = pygame.transform.scale(TEXT_BG, (MENU_RECT.width + 200, MENU_RECT.height + 100))
        BG_RECT = TEXT_BG.get_rect(center=MENU_RECT.center)
        BG_RECT.y -= 10

        PLAY_BUTTON = Button(image=pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/Play-Rect.png"), pos=(840, 400),
                             text_input="PLAY", font=get_main_menu_font(75), base_color="#E57B1E", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/Options-Rect.png"), pos=(840, 550),
                             text_input="OPTIONS", font=get_main_menu_font(75), base_color="#E57B1E", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/Quit-Rect.png"), pos=(840, 700),
                             text_input="QUIT", font=get_main_menu_font(75), base_color="#E57B1E", hovering_color="White")
        
        screen.blit(TEXT_BG, BG_RECT)
        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()

main_menu()
