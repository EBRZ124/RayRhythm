import pygame

global_scaler = 0.5

# ------------------------ MAIN MENU ASSETS ------------------------
main_menu_bg =  pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/background2.jpg"), global_scaler)
level_select_bg = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/level-select-background.png"), global_scaler)
options_menu_bg = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/options-menu-bg.png"), global_scaler)

tite_text_box = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/Title-Rect.png"), global_scaler)
play_button_box = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/Play-Rect.png"), global_scaler)
options_button_box = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/Options-Rect.png"), global_scaler)
quit_button_box = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/Quit-Rect.png"),global_scaler)

# ------------------------ SKIN ASSETS ------------------------
circle_skin_selected = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/circle-skin-selected.png"), global_scaler)
circle_skin_unselected = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/circle-skin-button.png"), global_scaler)
rayman_skin_unselected = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/rayman-skin-button.png"), global_scaler)
rayman_skin_selected = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/rayman-skin-selected.png"), global_scaler)
sopranos_skin_unselected = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/soprano-skin-button.png"), global_scaler)
sopranos_skin_selected = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/soprano-skin-selected.png"), global_scaler)

pressed_circle = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/circle_pressed.png"), global_scaler)
regular_circle = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/circle_regular.png"), global_scaler)
playing_circle = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/playing-circle.png"), global_scaler)

pressed_rayman_circle = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/pressed-rayman-circle.png"), global_scaler)
regular_rayman_circle = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/regular-rayman-circle.png"), global_scaler)

pressed_soprano_circle = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/pressed-soprano-circle.png"), global_scaler)
regular_soprano_circle = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/regular-soprano-circle.png"), global_scaler)

# ------------------------ LEVEL IMAGES ------------------------
snowy_box = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/level-2.png"), global_scaler)
test_level_box = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/test-level.png"), global_scaler)
anemone_box = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/level-1.png"), global_scaler)

# ------------------------ FONTS ------------------------
def get_main_menu_font(size):
    return pygame.font.Font("/RayRhythm/fonts/Blastge DEMO VERSION.ttf", size)

def get_level_name_font(size):
    return pygame.font.Font("/RayRhythm/fonts/Heavitas.ttf", size)

def result_screen_font(size):
    return pygame.font.Font("/RayRhythm/fonts/capitolcity.ttf", size)

# ------------------------ UNIVERSAL LEVEL ASSETS ------------------------
gameplay_overlay = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/gameplay-field.png"), global_scaler)
start_screen = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/level-start-screen.png"), global_scaler)
result_screen = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/result-screen.png"), global_scaler)

exit_button_results = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/exit-result-button.png"), global_scaler)

# ------------------------ LEVEL BGS ------------------------
test_background = pygame.transform.scale_by(pygame.image.load("/RayRhythm/Charts/TestLevel/test-level-background.png"), global_scaler)
snowy_background = pygame.transform.scale_by(pygame.image.load("//RayRhythm/Charts/Snowy/SnowyBG.png"), global_scaler)
anemone_background = pygame.transform.scale_by(pygame.image.load("/RayRhythm/Charts/anamone/IdentityBG.png"), global_scaler)