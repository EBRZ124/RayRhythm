import pygame

global_scaler = 0.5

# ------------------------ MAIN MENU ASSETS ------------------------
main_menu_bg =  pygame.transform.scale_by(pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/background2.jpg"), global_scaler)
level_select_bg = pygame.transform.scale_by(pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/level-select-background.png"), global_scaler)
options_menu_bg = pygame.transform.scale_by(pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/options-menu-bg.png"), global_scaler)

tite_text_box = pygame.transform.scale_by(pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/Title-Rect.png"), global_scaler)
play_button_box = pygame.transform.scale_by(pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/Play-Rect.png"), global_scaler)
options_button_box = pygame.transform.scale_by(pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/Options-Rect.png"), global_scaler)
quit_button_box = pygame.transform.scale_by(pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/Quit-Rect.png"),global_scaler)

# ------------------------ SKIN ASSETS ------------------------
circle_skin_selected = pygame.transform.scale_by(pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/circle-skin-selected.png"), global_scaler)
circle_skin_unselected = pygame.transform.scale_by(pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/circle-skin-button.png"), global_scaler)
rayman_skin_unselected = pygame.transform.scale_by(pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/rayman-skin-button.png"), global_scaler)
rayman_skin_selected = pygame.transform.scale_by(pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/rayman-skin-selected.png"), global_scaler)

# ------------------------ LEVEL IMAGES ------------------------
snowy_box = pygame.transform.scale_by(pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/level-2.png"), global_scaler)
test_level_box = pygame.transform.scale_by(pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/test-level.png"), global_scaler)
anemone_box = pygame.transform.scale_by(pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/level-1.png"), global_scaler)

# ------------------------ LEVEL IMAGES ------------------------
def get_main_menu_font(size):
    return pygame.font.Font("/Users/evaldsberzins/pygame/RayRhythm/fonts/Blastge DEMO VERSION.ttf", size)

def get_level_name_font(size):
    return pygame.font.Font("/Users/evaldsberzins/pygame/RayRhythm/fonts/Heavitas.ttf", size)