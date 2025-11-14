import pygame, sys
from button import Button
import time

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

AnamoneBG = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/Charts/anamone/IdentityBG.png")
GameplayOverlay = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/gameplay-field.png")

# Circle skin assets
PressedCircle = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/circle_pressed.png")
RegularCirlce = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/circle_regular.png")
FallingNote = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/circle_regular.png")

# Result screen
ResultScreen = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/result-screen.png")

# Fonts
def result_screen_font(size):
    return pygame.font.Font("/Users/evaldsberzins/pygame/RayRhythm/fonts/capitolcity.ttf", size)

# Rayman skin assets
PressedRaymanCircle = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/pressed-rayman-circle.png")
RegularRaymanCircle = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/regular-rayman-circle.png")
FallingRaymanCircle = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/regular-rayman-circle.png")

# Sound effects
HitSound = pygame.mixer.Sound("/Users/evaldsberzins/pygame/RayRhythm/Charts/hit-sound.wav")
ComboBreak = pygame.mixer.Sound("/Users/evaldsberzins/pygame/RayRhythm/Charts/combo-break.wav")
click_SFX = pygame.mixer.Sound("/Users/evaldsberzins/pygame/RayRhythm/sounds/click-sound.wav")
click_SFX.set_volume(0.6)

chart_lanes = [890, 1070, 1250, 1430]
player_keys = [pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k]
note_speed = 50
target_y_coordinate = 880
score = 0
combo = 0

music_offset_ms = 2000
spawn_lead_ms = 0

chart = [
    {"time": 330+1600, "lane": 0}, 
    {"time": 480+1600, "lane": 1}, 
    {"time": 630+1600, "lane": 2}, 
    {"time": 930+1600, "lane": 3}, 
    {"time": 1080+1600, "lane": 0}, 
    {"time": 1380+1600, "lane": 3}, 
    {"time": 1830+1600, "lane": 0}, 
    {"time": 1980+1600, "lane": 3}, 
    {"time": 2280+1600, "lane": 0}, 
    {"time": 2430+1600, "lane": 3}, 
    {"time": 2580+1600, "lane": 3}, 
    {"time": 5130+1600, "lane": 0}, 
    {"time": 5280+1600, "lane": 1}, 
    {"time": 5430+1600, "lane": 2}, 
    {"time": 5730+1600, "lane": 3}, 
    {"time": 7530+1600, "lane": 0}, 
    {"time": 7530+1600, "lane": 3}, 
    {"time": 7980+1600, "lane": 0}, 
    {"time": 7980+1600, "lane": 3}, 
    {"time": 8430+1600, "lane": 0}, 
    {"time": 8430+1600, "lane": 3}, 
    {"time": 8880+1600, "lane": 3}, 
    {"time": 8880+1600, "lane": 0}, 
    {"time": 9180+1600, "lane": 1}, 
    {"time": 9330+1600, "lane": 2}, 
    {"time": 9480+1600, "lane": 3}, 
    {"time": 9630+1600, "lane": 0}, 
    {"time": 9930+1600, "lane": 3}, 
    {"time": 9930+1600, "lane": 0}, 
    {"time": 10080+1600, "lane": 3}, 
    {"time": 10230+1600, "lane": 0}, 
    {"time": 10530+1600, "lane": 3}, 
    {"time": 10680+1600, "lane": 3}, 
    {"time": 10980+1600, "lane": 0}, 
    {"time": 11280+1600, "lane": 1}, 
    {"time": 11430+1600, "lane": 2}, 
    {"time": 11580+1600, "lane": 3}, 
    {"time": 11880+1600, "lane": 0}, 
    {"time": 12030+1600, "lane": 3}, 
    {"time": 12180+1600, "lane": 0}, 
    {"time": 12330+1600, "lane": 3}, 
    {"time": 12480+1600, "lane": 0}, 
    {"time": 12630+1600, "lane": 3}, 
    {"time": 12930+1600, "lane": 3}, 
    {"time": 13080+1600, "lane": 0}, 
    {"time": 13230+1600, "lane": 1}, 
    {"time": 13380+1600, "lane": 2}, 
    {"time": 13680+1600, "lane": 3}, 
    {"time": 13830+1600, "lane": 0}, 
    {"time": 13980+1600, "lane": 3}, 
    {"time": 14280+1600, "lane": 0}, 
    {"time": 14430+1600, "lane": 3}, 
    {"time": 14580+1600, "lane": 0}, 
    {"time": 14730+1600, "lane": 3}, 
    {"time": 14880+1600, "lane": 3}, 
    {"time": 15030+1600, "lane": 0}, 
    {"time": 15180+1600, "lane": 1}, 
    {"time": 15480+1600, "lane": 2}, 
    {"time": 15780+1600, "lane": 3}, 
    {"time": 16080+1600, "lane": 0}, 
    {"time": 16230+1600, "lane": 3}, 
    {"time": 16530+1600, "lane": 0}, 
    {"time": 16830+1600, "lane": 3}, 
    {"time": 17130+1600, "lane": 0}, 
    {"time": 17580+1600, "lane": 3}, 
    {"time": 18030+1600, "lane": 3}, 
    {"time": 18480+1600, "lane": 0}, 
    {"time": 18780+1600, "lane": 1}, 
    {"time": 18930+1600, "lane": 2}, 
    {"time": 19080+1600, "lane": 3}, 
    {"time": 19230+1600, "lane": 0}, 
    {"time": 19530+1600, "lane": 3}, 
    {"time": 19530+1600, "lane": 0}, 
    {"time": 19830+1600, "lane": 3}, 
    {"time": 20130+1600, "lane": 0}, 
    {"time": 20280+1600, "lane": 3}, 
    {"time": 20580+1600, "lane": 3}, 
    {"time": 20880+1600, "lane": 0}, 
    {"time": 21180+1600, "lane": 1}, 
    {"time": 21480+1600, "lane": 2}, 
    {"time": 21630+1600, "lane": 3}, 
    {"time": 21780+1600, "lane": 0}, 
    {"time": 22230+1600, "lane": 3}, 
    {"time": 22530+1600, "lane": 0}, 
    {"time": 22680+1600, "lane": 3}, 
    {"time": 22980+1600, "lane": 0}, 
    {"time": 23280+1600, "lane": 3}, 
    {"time": 23580+1600, "lane": 3}, 
    {"time": 23730+1600, "lane": 0}, 
    {"time": 23880+1600, "lane": 1}, 
    {"time": 24030+1600, "lane": 2}, 
    {"time": 24180+1600, "lane": 3}, 
    {"time": 24630+1600, "lane": 0}, 
    {"time": 24930+1600, "lane": 3}, 
    {"time": 25080+1600, "lane": 0}, 
    {"time": 25380+1600, "lane": 3}, 
    {"time": 25680+1600, "lane": 0}, 
    {"time": 25980+1600, "lane": 3}, 
    {"time": 26280+1600, "lane": 3}, 
    {"time": 26430+1600, "lane": 0}, 
    {"time": 26580+1600, "lane": 1}, 
    {"time": 26880+1600, "lane": 2}, 
    {"time": 27030+1600, "lane": 3}, 
    {"time": 27330+1600, "lane": 0}, 
    {"time": 27480+1600, "lane": 3}, 
    {"time": 27780+1600, "lane": 0}, 
    {"time": 27930+1600, "lane": 3}, 
    {"time": 28230+1600, "lane": 0}, 
    {"time": 28380+1600, "lane": 3}, 
    {"time": 28530+1600, "lane": 3}, 
    {"time": 28830+1600, "lane": 0}, 
    {"time": 29130+1600, "lane": 1}, 
    {"time": 29430+1600, "lane": 2}, 
    {"time": 29730+1600, "lane": 3}, 
    {"time": 29880+1600, "lane": 0}, 
    {"time": 30180+1600, "lane": 3}, 
    {"time": 30480+1600, "lane": 0}, 
    {"time": 30780+1600, "lane": 3}, 
    {"time": 30930+1600, "lane": 0}, 
    {"time": 31080+1600, "lane": 3}, 
    {"time": 31230+1600, "lane": 3}, 
    {"time": 31380+1600, "lane": 0}, 
    {"time": 31830+1600, "lane": 1}, 
    {"time": 32130+1600, "lane": 2}, 
    {"time": 32280+1600, "lane": 3}, 
    {"time": 32580+1600, "lane": 0}, 
    {"time": 32880+1600, "lane": 3}, 
    {"time": 33180+1600, "lane": 0}, 
    {"time": 33480+1600, "lane": 3}, 
    {"time": 33630+1600, "lane": 0}, 
    {"time": 33780+1600, "lane": 3}, 
    {"time": 33930+1600, "lane": 3}, 
    {"time": 34230+1600, "lane": 0}, 
    {"time": 34380+1600, "lane": 1}, 
    {"time": 34530+1600, "lane": 2}, 
    {"time": 34830+1600, "lane": 3}, 
    {"time": 34980+1600, "lane": 0}, 
    {"time": 35130+1600, "lane": 3}, 
    {"time": 35430+1600, "lane": 0}, 
    {"time": 35580+1600, "lane": 3}, 
    {"time": 35730+1600, "lane": 0}, 
    {"time": 36030+1600, "lane": 3}, 
    {"time": 36180+1600, "lane": 3}, 
    {"time": 36330+1600, "lane": 0}, 
    {"time": 36480+1600, "lane": 1}, 
    {"time": 36930+1600, "lane": 2}, 
    {"time": 37080+1600, "lane": 3}, 
    {"time": 37530+1600, "lane": 0}, 
    {"time": 37680+1600, "lane": 3}, 
    {"time": 38130+1600, "lane": 0}, 
    {"time": 38130+1600, "lane": 3}, 
    {"time": 38280+1600, "lane": 0}, 
    {"time": 38280+1600, "lane": 3}, 
    {"time": 38730+1600, "lane": 3}, 
    {"time": 38730+1600, "lane": 0}, 
    {"time": 39030+1600, "lane": 1}, 
    {"time": 39180+1600, "lane": 2}, 
    {"time": 39330+1600, "lane": 3}, 
    {"time": 39480+1600, "lane": 0}, 
    {"time": 39780+1600, "lane": 3}, 
    {"time": 40080+1600, "lane": 0}, 
    {"time": 40380+1600, "lane": 3}, 
    {"time": 40680+1600, "lane": 0}, 
    {"time": 40830+1600, "lane": 3}, 
    {"time": 40980+1600, "lane": 3}, 
    {"time": 41130+1600, "lane": 0}, 
    {"time": 41430+1600, "lane": 1}, 
    {"time": 41580+1600, "lane": 2}, 
    {"time": 41730+1600, "lane": 3}, 
    {"time": 41880+1600, "lane": 0}, 
    {"time": 42180+1600, "lane": 3}, 
    {"time": 42480+1600, "lane": 0}, 
    {"time": 42780+1600, "lane": 3}, 
    {"time": 43080+1600, "lane": 0}, 
    {"time": 43230+1600, "lane": 3}, 
    {"time": 43380+1600, "lane": 3}, 
    {"time": 43530+1600, "lane": 0}, 
    {"time": 43830+1600, "lane": 1}, 
    {"time": 43980+1600, "lane": 2}, 
    {"time": 44130+1600, "lane": 3}, 
    {"time": 44280+1600, "lane": 0}, 
    {"time": 44580+1600, "lane": 3}, 
    {"time": 44880+1600, "lane": 0}, 
    {"time": 45180+1600, "lane": 3}, 
    {"time": 45480+1600, "lane": 0}, 
    {"time": 45630+1600, "lane": 3}, 
    {"time": 45780+1600, "lane": 3}, 
    {"time": 45930+1600, "lane": 0}, 
    {"time": 46230+1600, "lane": 1}, 
    {"time": 46380+1600, "lane": 2}, 
    {"time": 46530+1600, "lane": 3}, 
    {"time": 46680+1600, "lane": 0}, 
    {"time": 46980+1600, "lane": 3}, 
    {"time": 47280+1600, "lane": 0}, 
    {"time": 47580+1600, "lane": 3}, 
    {"time": 47880+1600, "lane": 0}, 
    {"time": 48030+1600, "lane": 3}, 
    {"time": 48180+1600, "lane": 3}, 
    {"time": 48330+1600, "lane": 0}, 
    {"time": 48330+1600, "lane": 1}, 
    {"time": 48930+1600, "lane": 2}, 
    {"time": 49530+1600, "lane": 3}, 
    {"time": 50130+1600, "lane": 0}, 
    {"time": 50280+1600, "lane": 3}, 
    {"time": 50430+1600, "lane": 0}, 
    {"time": 50580+1600, "lane": 3}, 
    {"time": 50730+1600, "lane": 0}, 
    {"time": 51330+1600, "lane": 3}, 
    {"time": 51930+1600, "lane": 3}, 
    {"time": 52530+1600, "lane": 0}, 
    {"time": 52680+1600, "lane": 1}, 
    {"time": 52830+1600, "lane": 2}, 
    {"time": 52980+1600, "lane": 3}, 
    {"time": 53130+1600, "lane": 0}, 
    {"time": 53130+1600, "lane": 3}, 
    {"time": 53730+1600, "lane": 0}, 
    {"time": 54330+1600, "lane": 3}, 
    {"time": 54930+1600, "lane": 0}, 
    {"time": 55530+1600, "lane": 3}, 
    {"time": 55680+1600, "lane": 3}, 
    {"time": 55830+1600, "lane": 0}, 
    {"time": 55980+1600, "lane": 1}, 
    {"time": 56280+1600, "lane": 2}, 
    {"time": 56580+1600, "lane": 3}, 
    {"time": 56730+1600, "lane": 0}, 
    {"time": 57330+1600, "lane": 3}, 
    {"time": 57630+1600, "lane": 0}, 
    {"time": 57930+1600, "lane": 3}, 
    {"time": 58380+1600, "lane": 0}, 
    {"time": 58830+1600, "lane": 3}, 
    {"time": 59280+1600, "lane": 3}, 
    {"time": 59730+1600, "lane": 0}, 
    {"time": 60180+1600, "lane": 1}, 
    {"time": 60630+1600, "lane": 2}, 
    {"time": 61080+1600, "lane": 3}, 
    {"time": 61530+1600, "lane": 0}, 
    {"time": 61980+1600, "lane": 3}, 
    {"time": 62430+1600, "lane": 0}, 
    {"time": 62730+1600, "lane": 3}, 
    {"time": 63180+1600, "lane": 0}, 
    {"time": 63630+1600, "lane": 3}, 
    {"time": 64080+1600, "lane": 3}, 
    {"time": 64530+1600, "lane": 0}, 
    {"time": 65430+1600, "lane": 1}, 
    {"time": 65880+1600, "lane": 2}, 
    {"time": 66330+1600, "lane": 3}, 
    {"time": 66780+1600, "lane": 0}, 
    {"time": 67230+1600, "lane": 3}, 
    {"time": 67530+1600, "lane": 0}, 
    {"time": 67530+1600, "lane": 3}, 
    {"time": 68880+1600, "lane": 0}, 
    {"time": 69030+1600, "lane": 3}, 
    {"time": 69330+1600, "lane": 3}, 
    {"time": 69480+1600, "lane": 0}, 
    {"time": 69780+1600, "lane": 1}, 
    {"time": 70080+1600, "lane": 2}, 
    {"time": 70230+1600, "lane": 3}, 
    {"time": 70380+1600, "lane": 0}, 
    {"time": 70680+1600, "lane": 3}, 
    {"time": 70830+1600, "lane": 0}, 
    {"time": 70980+1600, "lane": 3}, 
    {"time": 71130+1600, "lane": 0}, 
    {"time": 71280+1600, "lane": 3}, 
    {"time": 71430+1600, "lane": 3}, 
    {"time": 71730+1600, "lane": 0}, 
    {"time": 71880+1600, "lane": 1}, 
    {"time": 72030+1600, "lane": 2}, 
    {"time": 72180+1600, "lane": 3}, 
    {"time": 72480+1600, "lane": 0}, 
    {"time": 72630+1600, "lane": 3}, 
    {"time": 72780+1600, "lane": 0}, 
    {"time": 73080+1600, "lane": 3}, 
    {"time": 73230+1600, "lane": 0}, 
    {"time": 73380+1600, "lane": 3}, 
    {"time": 73530+1600, "lane": 3}, 
    {"time": 73680+1600, "lane": 0}, 
    {"time": 73830+1600, "lane": 1}, 
    {"time": 73980+1600, "lane": 2}, 
    {"time": 74280+1600, "lane": 3}, 
    {"time": 74580+1600, "lane": 0}, 
    {"time": 74880+1600, "lane": 3}, 
    {"time": 75030+1600, "lane": 0}, 
    {"time": 75330+1600, "lane": 3}, 
    {"time": 75630+1600, "lane": 0}, 
    {"time": 75930+1600, "lane": 3}, 
    {"time": 76380+1600, "lane": 3}, 
    {"time": 76380+1600, "lane": 0}, 
    {"time": 76830+1600, "lane": 1}, 
    {"time": 77280+1600, "lane": 2}, 
    {"time": 77280+1600, "lane": 3}, 
    {"time": 77580+1600, "lane": 0}, 
    {"time": 77730+1600, "lane": 3}, 
    {"time": 77880+1600, "lane": 0}, 
    {"time": 78030+1600, "lane": 3}, 
    {"time": 78330+1600, "lane": 0}, 
    {"time": 78330+1600, "lane": 3}, 
    {"time": 78480+1600, "lane": 3}, 
    {"time": 78630+1600, "lane": 0}, 
    {"time": 78930+1600, "lane": 1}, 
    {"time": 79080+1600, "lane": 2}, 
    {"time": 79380+1600, "lane": 3}, 
    {"time": 79680+1600, "lane": 0}, 
    {"time": 79830+1600, "lane": 3}, 
    {"time": 79980+1600, "lane": 0}, 
    {"time": 80280+1600, "lane": 3}, 
    {"time": 80430+1600, "lane": 0}, 
    {"time": 80580+1600, "lane": 3}, 
    {"time": 80730+1600, "lane": 3}, 
    {"time": 80880+1600, "lane": 0}, 
    {"time": 81030+1600, "lane": 1}, 
    {"time": 81330+1600, "lane": 2}, 
    {"time": 81480+1600, "lane": 3}, 
    {"time": 81630+1600, "lane": 0}, 
    {"time": 81780+1600, "lane": 3}, 
    {"time": 82080+1600, "lane": 0}, 
    {"time": 82230+1600, "lane": 3}, 
    {"time": 82380+1600, "lane": 0}, 
    {"time": 82680+1600, "lane": 3}, 
    {"time": 82830+1600, "lane": 3}, 
    {"time": 82980+1600, "lane": 0}, 
    {"time": 83130+1600, "lane": 1}, 
    {"time": 83280+1600, "lane": 2}, 
    {"time": 83430+1600, "lane": 3}, 
    {"time": 83580+1600, "lane": 0}, 
    {"time": 83880+1600, "lane": 3}, 
    {"time": 84180+1600, "lane": 0}, 
    {"time": 84480+1600, "lane": 3}, 
    {"time": 84630+1600, "lane": 0}, 
    {"time": 84930+1600, "lane": 3}, 
    {"time": 85230+1600, "lane": 3}, 
    {"time": 85530+1600, "lane": 0}, 
    {"time": 85530+1600, "lane": 1}, 
    {"time": 85980+1600, "lane": 2}, 
    {"time": 85980+1600, "lane": 3}, 
    {"time": 86430+1600, "lane": 0}, 
    {"time": 86430+1600, "lane": 3}, 
    {"time": 86880+1600, "lane": 0}, 
    {"time": 86880+1600, "lane": 3}, 
    {"time": 87180+1600, "lane": 0}, 
    {"time": 87330+1600, "lane": 3}, 
    {"time": 87480+1600, "lane": 3}, 
    {"time": 87630+1600, "lane": 0}, 
    {"time": 87930+1600, "lane": 1}, 
    {"time": 87930+1600, "lane": 2}, 
    {"time": 88380+1600, "lane": 3}, 
    {"time": 88380+1600, "lane": 0}, 
    {"time": 88830+1600, "lane": 3}, 
    {"time": 88830+1600, "lane": 0}, 
    {"time": 89280+1600, "lane": 3}, 
    {"time": 89280+1600, "lane": 0}, 
    {"time": 89580+1600, "lane": 3}, 
    {"time": 89730+1600, "lane": 3}, 
    {"time": 89880+1600, "lane": 0}, 
    {"time": 90030+1600, "lane": 1}, 
    {"time": 90330+1600, "lane": 2}, 
    {"time": 90330+1600, "lane": 3}, 
    {"time": 90780+1600, "lane": 0}, 
    {"time": 90780+1600, "lane": 3}, 
    {"time": 91230+1600, "lane": 0}, 
    {"time": 91230+1600, "lane": 3}, 
    {"time": 91680+1600, "lane": 0}, 
    {"time": 91680+1600, "lane": 3}, 
    {"time": 91980+1600, "lane": 3}, 
    {"time": 92130+1600, "lane": 0}, 
    {"time": 92280+1600, "lane": 1}, 
    {"time": 92430+1600, "lane": 2}, 
    {"time": 92730+1600, "lane": 3}, 
    {"time": 92730+1600, "lane": 0}, 
    {"time": 93180+1600, "lane": 3}, 
    {"time": 93180+1600, "lane": 0}, 
    {"time": 93630+1600, "lane": 3}, 
    {"time": 93630+1600, "lane": 0}, 
    {"time": 94080+1600, "lane": 3}, 
    {"time": 94080+1600, "lane": 3}, 
    {"time": 94530+1600, "lane": 0}, 
    {"time": 94530+1600, "lane": 1}, 
    {"time": 94980+1600, "lane": 2}, 
    {"time": 94980+1600, "lane": 3}, 
    {"time": 95430+1600, "lane": 0}, 
    {"time": 95430+1600, "lane": 3}, 
    {"time": 95880+1600, "lane": 0}, 
    {"time": 95880+1600, "lane": 3}, 
]

def start_identity_part4(screen):
    global score
    score = 0
    global combo
    combo = 0
    global skin_variant
    skin_variant = 0
    running = True
    chart_index = 0
    notes = []

    pygame.mixer.music.load("/Users/evaldsberzins/pygame/RayRhythm/Charts/anamone/anamone-chart.wav")
    pygame.mixer.music.set_volume(0.2)
    HitSound.set_volume(0.1)
    ComboBreak.set_volume(0.1)
    
    music_started = False
    music_start_time = None
    level_start_time = pygame.time.get_ticks()

    while running:
        dt = clock.tick(60)
        now = pygame.time.get_ticks() - level_start_time

        if not music_started and now >= music_offset_ms:
            pygame.mixer.music.play()
            music_started = True
            music_start_time = pygame.time.get_ticks()

        music_time = (pygame.mixer.music.get_pos() if music_started else 0) - music_offset_ms

        # Music offset logic
        while chart_index < len(chart) and chart[chart_index]["time"] - spawn_lead_ms <= now:
            n = chart[chart_index]
            notes.append({"lane": n["lane"], "y": -50, "hit": False, "time": n["time"]})
            chart_index += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EXIT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    click_SFX.play()
                    running = False

            if event.type == pygame.KEYDOWN:
                for lane, key in enumerate(player_keys):
                    if event.key == key:
                        closest_note = None
                        closest_dist = float("inf")
                        for n in notes:
                            if n["lane"] == lane and not n["hit"]:
                                dist = abs(n["y"] - target_y_coordinate)
                                if dist < closest_dist:
                                    closest_note = n
                                    closest_dist = dist
                        
                        if closest_note:
                            if closest_dist <= 50:
                                score += 100
                                combo += 1
                                closest_note["hit"] = True
                            elif closest_dist <= 100:
                                score += 50
                                combo += 1
                                closest_note["hit"] = True
                            elif closest_dist <= 200:
                                score += 25
                                combo += 1
                                closest_note["hit"] = True
                            elif closest_dist <= 400:
                                if combo >= 3:
                                    ComboBreak.play()
                                combo = 0
                                closest_note["hit"] = True

                if event.key == pygame.K_d:
                        HitSound.play()
                if event.key == pygame.K_f:
                        HitSound.play()
                if event.key == pygame.K_j:
                        HitSound.play()
                if event.key == pygame.K_k:
                        HitSound.play()        
        for n in notes:
            n["y"] += note_speed

        notes = [n for n in notes if n["y"] < 1050 and not n["hit"]]

        screen.blit(AnamoneBG, (0, 0))
        screen.blit(GameplayOverlay, (0, 0)) 

        if skin_variant == 0:
            screen.blit(RegularCirlce, (890, 880))
            screen.blit(RegularCirlce, (1070, 880))
            screen.blit(RegularCirlce, (1250, 880))
            screen.blit(RegularCirlce, (1430, 880))
            for x in chart_lanes:
                screen.blit(RegularCirlce, (x, target_y_coordinate))
            for n in notes:
                x = chart_lanes[n["lane"]]
                screen.blit(FallingNote, (x, n["y"]))
            keys = pygame.key.get_pressed()
            for lane, key in enumerate(player_keys):
                if keys[key]:
                    screen.blit(PressedCircle, (chart_lanes[lane], target_y_coordinate))

        if skin_variant == 1:
            screen.blit(RegularRaymanCircle, (890, 880))
            screen.blit(RegularRaymanCircle, (1070, 880))
            screen.blit(RegularRaymanCircle, (1250, 880))
            screen.blit(RegularRaymanCircle, (1430, 880))
            for x in chart_lanes:
                screen.blit(RegularRaymanCircle, (x, target_y_coordinate))
            for n in notes:
                x = chart_lanes[n["lane"]]
                screen.blit(FallingRaymanCircle, (x, n["y"]))
            keys = pygame.key.get_pressed()
            for lane, key in enumerate(player_keys):
                if keys[key]:
                    screen.blit(PressedRaymanCircle, (chart_lanes[lane], target_y_coordinate))

        font = pygame.font.Font(None, 60)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (100, 100))

        combo_text = font.render(f"Combo: {combo}", True, (255, 255, 255))
        screen.blit(combo_text, (100, 150))

        # ----------------LEVEL FINISHED----------------
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        level_done = (
            chart_index >= len(chart) and
            len(notes) == 0 and
            music_started and
            not pygame.mixer.music.get_busy()
        )

        if level_done:
            screen.blit(ResultScreen, (0, 0))
            pygame.display.flip()

            Final_Score_Text = result_screen_font(45).render(f"Total score: {score}", True, "White")
            Final_Score_Rect = Final_Score_Text.get_rect(center=(840, 450))
            screen.blit(Final_Score_Text, Final_Score_Rect)

            Max_Combo = result_screen_font(45).render(f"Your max combo: {combo}", True, "White")
            Max_Combo_Rect = Max_Combo.get_rect(center=(840, 550))
            screen.blit(Max_Combo, Max_Combo_Rect)

            EXIT_BUTTON = Button(image=None, pos=(840, 750), text_input="Exit level", font = pygame.font.Font(None, 80), base_color="White", hovering_color="White")
            EXIT_BUTTON.changeColor(PLAY_MOUSE_POS)
            EXIT_BUTTON.update(screen)

        pygame.display.flip()

        if keys[pygame.K_ESCAPE]:
            running = False
