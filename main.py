import pygame, sys
from Charts.anamone import anamone
from Charts.TestLevel import TestLevel
from Charts.Snowy import snowy
from button import Button
import global_variables

pygame.init()
resolutions_16_10 = [ # 16:10
    (840, 525), # scale = 0.5
    (1176, 735), # scale = 0.7
    (1680, 1050), # scale = 1
]
current_resolution = 1
screen_scaler = global_variables.global_scaler
screen = pygame.display.set_mode(resolutions_16_10[current_resolution])
pygame.display.set_caption("RayRhythm")
global_variables.load_assets()
global_variables.apply_scaling()

music_volume = global_variables.music_volume
sound_effect_volume = global_variables.sound_effect_volume

pygame.mixer_music.set_volume(music_volume)
click_SFX = global_variables.click_sound
click_SFX.set_volume(sound_effect_volume)

selected_skin = 1

def main_menu():
    pygame.mixer_music.set_volume(music_volume)
    pygame.mixer_music.load(global_variables.main_menu_song)
    pygame.mixer.music.play(-1)

    while True:
        screen.blit(global_variables.images["main_menu_bg"], (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = global_variables.get_main_menu_font(int(100*screen_scaler)).render("RayRhythm", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center=(840*screen_scaler, 200*screen_scaler))
        TEXT_BG = global_variables.images["title_text_box"]
        TEXT_BG = pygame.transform.scale(TEXT_BG, ((MENU_RECT.width + 200*screen_scaler), (MENU_RECT.height + 100*screen_scaler)))
        BG_RECT = TEXT_BG.get_rect(center=MENU_RECT.center)

        PLAY_BUTTON = Button(image=global_variables.images["play_button_box"], pos=(840*screen_scaler, 400*screen_scaler),
                             text_input="PLAY", font=global_variables.get_main_menu_font(int(75*screen_scaler)), base_color="#E57B1E", hovering_color="White")
        OPTIONS_BUTTON = Button(image=global_variables.images["options_button_box"], pos=(840*screen_scaler, 550*screen_scaler),
                             text_input="OPTIONS", font=global_variables.get_main_menu_font(int(75*screen_scaler)), base_color="#E57B1E", hovering_color="White")
        QUIT_BUTTON = Button(image=global_variables.images["quit_button_box"], pos=(840*screen_scaler, 700*screen_scaler),
                             text_input="QUIT", font=global_variables.get_main_menu_font(int(75*screen_scaler)), base_color="#E57B1E", hovering_color="White")
        
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
    
def play():
    pygame.mixer_music.stop()
    music_volume = 0.3
    pygame.mixer_music.set_volume(music_volume)
    pygame.mixer.music.load(global_variables.level_select_music)
    pygame.mixer_music.play()

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(global_variables.images["level_select_bg"], (0, 0))
        
        select_stage_skin = global_variables.get_main_menu_font(int(75*screen_scaler)).render("Select a stage", True, "White")
        stage_rect = select_stage_skin.get_rect(center=(840*screen_scaler, 90*screen_scaler))
        screen.blit(select_stage_skin, stage_rect)

        LEVEL_SNOWY = Button(image=global_variables.images["snowy_box"], pos=(840*screen_scaler, 270*screen_scaler),
                            text_input="Snowy", font=global_variables.get_level_name_font(int(60*screen_scaler)), base_color="White", hovering_color="#D3DDF8")
        LEVEL_SNOWY.changeColor(LEVEL_MOUSE_POS)
        LEVEL_SNOWY.update(screen)

        TEST_LEVEL = Button(image=global_variables.images["test_level_box"], pos=(840*screen_scaler, 770*screen_scaler),
                            text_input="TEST LEVEL", font=global_variables.get_level_name_font(int(60*screen_scaler)), base_color="White", hovering_color="#FFFBDA")
        TEST_LEVEL.changeColor(LEVEL_MOUSE_POS)
        TEST_LEVEL.update(screen)

        LEVEL_ANEMONE = Button(image=global_variables.images["anemone_box"], pos=(840*screen_scaler, 520*screen_scaler),
                              text_input="ANEMONE", font=global_variables.get_level_name_font(int(60*screen_scaler)), base_color="White", hovering_color="#C2F1FF")
        LEVEL_ANEMONE.changeColor(LEVEL_MOUSE_POS)
        LEVEL_ANEMONE.update(screen)

        PLAY_BACK = Button(image=None, pos=(840*screen_scaler, 950*screen_scaler), text_input="BACK", font=global_variables.get_main_menu_font(int(75*screen_scaler)), base_color="White", hovering_color="#F4CCFC")

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
                if LEVEL_ANEMONE.checkForInput(PLAY_MOUSE_POS):
                    anamone.start_anamone(screen, selected_skin, screen_scaler)
                if TEST_LEVEL.checkForInput(PLAY_MOUSE_POS):
                    TestLevel.start_test_level(screen, selected_skin, screen_scaler)
                if LEVEL_SNOWY.checkForInput(PLAY_MOUSE_POS):
                    snowy.start_snowy(screen, selected_skin, screen_scaler)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
  
        pygame.display.update()

def options():
    pygame.mixer_music.load(global_variables.settings_menu_music)
    pygame.mixer_music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    global current_resolution, screen, screen_scaler, selected_skin

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

                if SKIN_CIRCLE.checkForInput(OPTIONS_MOUSE_POS):
                    selected_skin = 0
                    click_SFX.play()

                if SKIN_RAYMAN.checkForInput(OPTIONS_MOUSE_POS):
                    selected_skin = 1
                    click_SFX.play()

                if SKIN_SOPRANO.checkForInput(OPTIONS_MOUSE_POS):
                    selected_skin = 2
                    click_SFX.play()

                if resolution_10.checkForInput(OPTIONS_MOUSE_POS):
                    current_resolution = 2
                    screen_scaler = 1
                    global_variables.set_global_scaler(screen_scaler)
                    width, heigth = resolutions_16_10[current_resolution]
                    screen = pygame.display.set_mode((width, heigth))
                    click_SFX.play()
                
                if resolution_07.checkForInput(OPTIONS_MOUSE_POS):
                    current_resolution = 1
                    screen_scaler = 0.7
                    global_variables.set_global_scaler(screen_scaler)
                    width, heigth = resolutions_16_10[current_resolution]
                    screen = pygame.display.set_mode((width, heigth))
                    click_SFX.play()

                if resolution_05.checkForInput(OPTIONS_MOUSE_POS):
                    current_resolution = 0
                    screen_scaler = 0.5
                    global_variables.set_global_scaler(screen_scaler)
                    width, heigth = resolutions_16_10[current_resolution]
                    screen = pygame.display.set_mode((width, heigth))
                    click_SFX.play()                    

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        screen.blit(global_variables.images["options_menu_bg"], (0, 0))

        OPTIONS_TEXT = global_variables.get_main_menu_font(int(75*screen_scaler)).render("Settings Menu", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(840*screen_scaler, 100*screen_scaler))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        SKINS_TEXT = global_variables.get_main_menu_font(int(60*screen_scaler)).render("Resolutions", True, "White")
        SKINS_RECT = SKINS_TEXT.get_rect(center=(840*screen_scaler, 200*screen_scaler))
        screen.blit(SKINS_TEXT, SKINS_RECT)

        resolution_05 = Button(image=global_variables.images["screen_scale_05"], pos=(530*screen_scaler, 320*screen_scaler), text_input=" ", font=global_variables.get_level_name_font(75), base_color="White", hovering_color="White")
        resolution_05.changeColor(OPTIONS_MOUSE_POS)
        resolution_05.update(screen)

        resolution_07 = Button(image=global_variables.images["screen_scale_07"], pos=(840*screen_scaler, 320*screen_scaler), text_input=" ", font=global_variables.get_level_name_font(75), base_color="White", hovering_color="White")
        resolution_07.changeColor(OPTIONS_MOUSE_POS)
        resolution_07.update(screen)

        resolution_10 = Button(image=global_variables.images["screen_scale_10"], pos=(1150*screen_scaler, 320*screen_scaler), text_input=" ", font=global_variables.get_level_name_font(75), base_color="White", hovering_color="White")
        resolution_10.changeColor(OPTIONS_MOUSE_POS)
        resolution_10.update(screen)

        SKINS_TEXT = global_variables.get_main_menu_font(int(60*screen_scaler)).render("SKINS", True, "White")
        SKINS_RECT = SKINS_TEXT.get_rect(center=(840*screen_scaler, 640*screen_scaler))
        screen.blit(SKINS_TEXT, SKINS_RECT)


        OPTIONS_TEXT = global_variables.get_main_menu_font(int(75*screen_scaler)).render("Settings Menu", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(840*screen_scaler, 100*screen_scaler))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        if selected_skin == 0:
            SKIN_CIRCLE = Button(image=global_variables.images["circle_skin_selected"], pos=(840*screen_scaler, 775*screen_scaler), text_input=" ", font=global_variables.get_level_name_font(75), base_color="White", hovering_color="White")
            SKIN_CIRCLE.changeColor(OPTIONS_MOUSE_POS)
            SKIN_CIRCLE.update(screen)

            SKIN_RAYMAN = Button(image=global_variables.images["rayman_skin_unselected"], pos=(1150*screen_scaler, 775*screen_scaler), text_input=" ", font=global_variables.get_level_name_font(75), base_color="White", hovering_color="White")
            SKIN_RAYMAN.changeColor(OPTIONS_MOUSE_POS)
            SKIN_RAYMAN.update(screen)

            SKIN_SOPRANO = Button(image=global_variables.images["sopranos_skin_unselected"], pos=(530*screen_scaler, 775*screen_scaler), text_input=" ", font=global_variables.get_level_name_font(75), base_color="White", hovering_color="White")
            SKIN_SOPRANO.changeColor(OPTIONS_MOUSE_POS)
            SKIN_SOPRANO.update(screen)

        if selected_skin == 1:
            SKIN_CIRCLE = Button(image=global_variables.images["circle_skin_unselected"], pos=(840*screen_scaler, 775*screen_scaler), text_input=" ", font=global_variables.get_level_name_font(75), base_color="White", hovering_color="White")
            SKIN_CIRCLE.changeColor(OPTIONS_MOUSE_POS)
            SKIN_CIRCLE.update(screen)

            SKIN_RAYMAN = Button(image=global_variables.images["rayman_skin_selected"], pos=(1150*screen_scaler, 775*screen_scaler), text_input=" ", font=global_variables.get_level_name_font(75), base_color="White", hovering_color="White")
            SKIN_RAYMAN.changeColor(OPTIONS_MOUSE_POS)
            SKIN_RAYMAN.update(screen)

            SKIN_SOPRANO = Button(image=global_variables.images["sopranos_skin_unselected"], pos=(530*screen_scaler, 775*screen_scaler), text_input=" ", font=global_variables.get_level_name_font(75), base_color="White", hovering_color="White")
            SKIN_SOPRANO.changeColor(OPTIONS_MOUSE_POS)
            SKIN_SOPRANO.update(screen)

        if selected_skin == 2:
            SKIN_CIRCLE = Button(image=global_variables.images["circle_skin_unselected"], pos=(840*screen_scaler, 775*screen_scaler), text_input=" ", font=global_variables.get_level_name_font(75), base_color="White", hovering_color="White")
            SKIN_CIRCLE.changeColor(OPTIONS_MOUSE_POS)
            SKIN_CIRCLE.update(screen)

            SKIN_RAYMAN = Button(image=global_variables.images["rayman_skin_unselected"], pos=(1150*screen_scaler, 775*screen_scaler), text_input=" ", font=global_variables.get_level_name_font(75), base_color="White", hovering_color="White")
            SKIN_RAYMAN.changeColor(OPTIONS_MOUSE_POS)
            SKIN_RAYMAN.update(screen)

            SKIN_SOPRANO = Button(image=global_variables.images["sopranos_skin_selected"], pos=(530*screen_scaler, 775*screen_scaler), text_input=" ", font=global_variables.get_level_name_font(75), base_color="White", hovering_color="White")
            SKIN_SOPRANO.changeColor(OPTIONS_MOUSE_POS)
            SKIN_SOPRANO.update(screen)

        OPTIONS_BACK = Button(image=None,pos=(840*screen_scaler, 970*screen_scaler),text_input="BACK",font=global_variables.get_main_menu_font(int(75*screen_scaler)),base_color="White",hovering_color="#F4CCFC")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        pygame.display.update()


main_menu()