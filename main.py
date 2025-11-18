import pygame, sys
from Charts.anamone import anamone
from button import Button
from Charts.TestLevel import TestLevel
from Charts.Snowy import snowy

pygame.init()

screen = pygame.display.set_mode((1680, 1050))
pygame.display.set_caption("Menu")

BackGround1 = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/background2.jpg")
LevelSelectBG = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/level-select-background.png")

# Sound generator
music_volume = 0.5
sound_effect_volume = 0.5

pygame.mixer_music.load("/Users/evaldsberzins/pygame/RayRhythm/sounds/main_menu_music.mp3")
pygame.mixer_music.set_volume(music_volume)
click_SFX = pygame.mixer.Sound("/Users/evaldsberzins/pygame/RayRhythm/sounds/click-sound.wav")
click_SFX.set_volume(sound_effect_volume)

def get_main_menu_font(size):
    return pygame.font.Font("/Users/evaldsberzins/pygame/RayRhythm/fonts/Blastge DEMO VERSION.ttf", size)

def get_level_name_font(size):
    return pygame.font.Font("/Users/evaldsberzins/pygame/RayRhythm/fonts/capitolcity.ttf", size)

def play():
    while True:
        pygame.mixer_music.stop()
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(LevelSelectBG, (0, 0))
        
        LEVEL_SNOWY = Button(image=pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/level-2.png"), pos=(840, 200),
                             text_input="Snowy", font=get_level_name_font(50), base_color="White", hovering_color="#D3DDF8")
        LEVEL_SNOWY.changeColor(LEVEL_MOUSE_POS)
        LEVEL_SNOWY.update(screen)

        TEST_LEVEL = Button(image=pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/test-level.png"), pos=(840, 700),
                             text_input="TEST LEVEL", font=get_level_name_font(50), base_color="White", hovering_color="#FFFBDA")
        TEST_LEVEL.changeColor(LEVEL_MOUSE_POS)
        TEST_LEVEL.update(screen)

        LEVEL_ANAMONE = Button(image=pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/level-1.png"), pos=(840, 450),
                             text_input="ANAMONE", font=get_level_name_font(50), base_color="White", hovering_color="#C2F1FF")
        LEVEL_ANAMONE.changeColor(LEVEL_MOUSE_POS)
        LEVEL_ANAMONE.update(screen)

        PLAY_BACK = Button(image=None, pos=(840, 900), text_input="BACK", font=get_main_menu_font(75), base_color="White", hovering_color="Orange")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    click_SFX.play()
                    main_menu()
                if LEVEL_ANAMONE.checkForInput(PLAY_MOUSE_POS):
                    anamone.start_anamone(screen)
                if TEST_LEVEL.checkForInput(PLAY_MOUSE_POS):
                    TestLevel.start_test_level(screen)
                if LEVEL_SNOWY.checkForInput(PLAY_MOUSE_POS):
                    snowy.start_snowy(screen)
        
        pygame.display.update()

def options():
    while True:
        events = pygame.event.get()
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    click_SFX.play()
                    main_menu()

        screen.fill("white")

        OPTIONS_TEXT = get_main_menu_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(840, 150))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None,pos=(840, 750),text_input="BACK",font=get_main_menu_font(75),base_color="Black",hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        pygame.display.update()

def main_menu():
    pygame.mixer_music.load("/Users/evaldsberzins/pygame/RayRhythm/sounds/main_menu_music.mp3")
    pygame.mixer_music.set_volume(music_volume)
    pygame.mixer_music.play()
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
        
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_SFX.play()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_SFX.play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        
        pygame.display.update()

main_menu()
