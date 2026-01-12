import pygame
pygame.init()
pygame.mixer.init()

global_scaler = 0.7

music_volume = 0.5
sound_effect_volume = 0.5

original_images = {}

images = {}

def load_assets():
    global original_images

    if original_images:
        return
    
    original_images = {
        # ------------------------ MENU ASSETS ------------------------
        "main_menu_bg": pygame.image.load("/RayRhythm/graphics/background2.jpg"),
        "options_menu_bg": pygame.image.load("/RayRhythm/graphics/options-menu-bg.png"),
        "level_select_bg": pygame.image.load("/RayRhythm/graphics/level-select-background.png"),

        "title_text_box": pygame.image.load("/RayRhythm/graphics/Title-Rect.png"),
        "play_button_box": pygame.image.load("/RayRhythm/graphics/Play-Rect.png"),
        "options_button_box": pygame.image.load("/RayRhythm/graphics/Options-Rect.png"),
        "quit_button_box": pygame.image.load("/RayRhythm/graphics/Quit-Rect.png"),

        "screen_scale_05": pygame.image.load("/RayRhythm/graphics/05_screen_scale.png"),
        "screen_scale_07": pygame.image.load("/RayRhythm/graphics/07_screen_scale.png"),
        "screen_scale_10": pygame.image.load("/RayRhythm/graphics/10_screen_scale.png"),

        # ------------------------ SKIN ASSETS ------------------------
        "circle_skin_selected": pygame.image.load("/RayRhythm/graphics/circle-skin-selected.png"),
        "circle_skin_unselected": pygame.image.load("/RayRhythm/graphics/circle-skin-button.png"),
        "rayman_skin_unselected": pygame.image.load("/RayRhythm/graphics/rayman-skin-button.png"),
        "rayman_skin_selected": pygame.image.load("/RayRhythm/graphics/rayman-skin-selected.png"),
        "sopranos_skin_unselected": pygame.image.load("/RayRhythm/graphics/soprano-skin-button.png"),
        "sopranos_skin_selected": pygame.image.load("/RayRhythm/graphics/soprano-skin-selected.png"),

        "pressed_circle": pygame.image.load("/RayRhythm/graphics/circle_pressed.png"),
        "regular_circle": pygame.image.load("/RayRhythm/graphics/circle_regular.png"), 
        "playing_circle": pygame.image.load("/RayRhythm/graphics/playing-circle.png"), 

        "pressed_rayman_circle": pygame.image.load("/RayRhythm/graphics/pressed-rayman-circle.png"),
        "regular_rayman_circle": pygame.image.load("/RayRhythm/graphics/regular-rayman-circle.png"), 

        "pressed_soprano_circle": pygame.image.load("/RayRhythm/graphics/pressed-soprano-circle.png"),
        "regular_soprano_circle": pygame.image.load("/RayRhythm/graphics/regular-soprano-circle.png"), 

        # ------------------------ LEVEL IMAGES ------------------------
        "snowy_box": pygame.image.load("/RayRhythm/graphics/level-2.png"), 
        "test_level_box": pygame.image.load("/RayRhythm/graphics/test-level.png"), 
        "anemone_box": pygame.image.load("/RayRhythm/graphics/level-1.png"), 

        # ------------------------ UNIVERSAL LEVEL ASSETS ------------------------
        "gameplay_overlay": pygame.image.load("/RayRhythm/graphics/gameplay-field.png"),
        "start_screen": pygame.image.load("/RayRhythm/graphics/level-start-screen.png"), 
        "result_screen": pygame.image.load("/RayRhythm/graphics/result-screen.png"),

        "exit_button_results": pygame.image.load("/RayRhythm/graphics/exit-result-button.png"),
        "ss_rank": pygame.image.load("/RayRhythm/graphics/ss_rank.png"), 
        "s_rank": pygame.image.load("/RayRhythm/graphics/s_rank.png"), 
        "a_rank": pygame.image.load("/RayRhythm/graphics/a_rank.png"),
        "b_rank": pygame.image.load("/RayRhythm/graphics/b_rank.png"), 
        "c_rank": pygame.image.load("/RayRhythm/graphics/c_rank.png"), 
        "d_rank": pygame.image.load("/RayRhythm/graphics/d_rank.png"),

        # ------------------------ LEVEL ASSETS ------------------------
        "test_background": pygame.image.load("/RayRhythm/Charts/TestLevel/test-level-background.png"), 
        "snowy_background": pygame.image.load("//RayRhythm/Charts/Snowy/SnowyBG.png"), 
        "anemone_background": pygame.image.load("/RayRhythm/Charts/anamone/IdentityBG.png")
    }
# ------------------------ Scaling ------------------------
def apply_scaling():
    global images, global_scaler

    images = {}
    for key, img in original_images.items():
        images[key] = pygame.transform.scale_by(img, global_scaler)

def set_global_scaler(value: float):
    global global_scaler
    global_scaler = value
    apply_scaling()

# ------------------------ FONTS ------------------------
def get_main_menu_font(size):
    return pygame.font.Font("/RayRhythm/fonts/Blastge DEMO VERSION.ttf", size)

def get_level_name_font(size):
    return pygame.font.Font("/RayRhythm/fonts/Heavitas.ttf", size)

def result_screen_font(size):
    return pygame.font.Font("/RayRhythm/fonts/capitolcity.ttf", size)

# ------------------------ SOUND ASSETS ------------------------
ss_sound_effect = pygame.mixer.Sound("/RayRhythm/sounds/ss_clap_sound.wav")
s_sound_effect = pygame.mixer.Sound("/RayRhythm/sounds/s_clap_sound.wav")
a_sound_effect = pygame.mixer.Sound("/RayRhythm/sounds/a_sound_clap.wav")
b_sound_effect = pygame.mixer.Sound("/RayRhythm/sounds/b_clap_sound.wav")
c_sound_effect = pygame.mixer.Sound("/RayRhythm/sounds/c_clap_sound.wav")
d_sound_effect = pygame.mixer.Sound("/RayRhythm/sounds/d_clap_sound.wav")

anemone_song = "/RayRhythm/Charts/anamone/anamone-chart.wav"
test_level_song = "/RayRhythm/Charts/TestLevel/test-level.wav"
snowy_song = "/RayRhythm/Charts/Snowy/audio.wav"

click_sound = pygame.mixer.Sound("/RayRhythm/sounds/click-sound.wav")
gat_sound = pygame.mixer.Sound("/RayRhythm/sounds/gat_sount.wav")
hit_sound = pygame.mixer.Sound("/RayRhythm/Charts/hit-sound.wav")
rayman_sound = pygame.mixer.Sound("/RayRhythm/sounds/rayman_sound.wav")
combo_braek = pygame.mixer.Sound("/RayRhythm/Charts/combo-break.wav")

main_menu_song = "/RayRhythm/sounds/main_menu_music.mp3"
level_select_music = "/RayRhythm/sounds/level_select_music.mp3"
settings_menu_music = "/RayRhythm/sounds/settings_menu_music.mp3"

# Old assets, just in case
"""
# ------------------------ MAIN MENU ASSETS ------------------------
main_menu_bg =  pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/background2.jpg"), global_scaler)
level_select_bg = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/level-select-background.png"), global_scaler)
options_menu_bg = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/options-menu-bg.png"), global_scaler)

tite_text_box = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/Title-Rect.png"), global_scaler)
play_button_box = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/Play-Rect.png"), global_scaler)
options_button_box = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/Options-Rect.png"), global_scaler)
quit_button_box = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/Quit-Rect.png"),global_scaler)

screen_scale_05 = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/05_screen_scale.png"), global_scaler)
screen_scale_07 = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/07_screen_scale.png"), global_scaler)
screen_scale_10 = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/10_screen_scale.png"), global_scaler)

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
snowy_box = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/level-2.png"), global_scaler*0.95)
test_level_box = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/test-level.png"), global_scaler*0.95)
anemone_box = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/level-1.png"), global_scaler*0.95)

# ------------------------ UNIVERSAL LEVEL ASSETS ------------------------
gameplay_overlay = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/gameplay-field.png"), global_scaler)
start_screen = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/level-start-screen.png"), global_scaler)
result_screen = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/result-screen.png"), global_scaler)

exit_button_results = pygame.transform.scale_by(pygame.image.load("/RayRhythm/graphics/exit-result-button.png"), global_scaler)
"""