import pygame, sys
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from button import Button
from Charts import IdentityPart4

pygame.init()

screen = pygame.display.set_mode((1680, 1050))
pygame.display.set_caption("Menu")

BackGround1 = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/background2.jpg")
LevelSelectBG = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/level-select-background.png")

# Sound generator
music_volume = 0.5
sound_effect_volume = 0.5

Menu_Song = pygame.mixer_music.load("/Users/evaldsberzins/pygame/RayRhythm/sounds/main_menu_music.mp3")
Menu_Song = pygame.mixer_music.set_volume(music_volume)
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
        LEVEL_1_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(LevelSelectBG, (0, 0))

        PLAY_TEXT = get_main_menu_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(840, 280))
        screen.blit(PLAY_TEXT, PLAY_RECT)

        LEVEL_1 = Button(image=pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/level-1.png"), pos=(840, 500),
                             text_input="Identity Part 4", font=get_level_name_font(50), base_color="White", hovering_color="#B1D2EC")
        LEVEL_1.changeColor(LEVEL_1_MOUSE_POS)
        LEVEL_1.update(screen)

        PLAY_BACK = Button(image=None, pos=(840, 800), text_input="BACK", font=get_main_menu_font(75), base_color="White", hovering_color="White")

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
                if LEVEL_1.checkForInput(PLAY_MOUSE_POS):
                    IdentityPart4.start_identity_part4(screen)
        
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
