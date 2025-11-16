import pygame, sys
from button import Button
import time
from Charts.anamone import anamone_chart

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
max_combo = 0

music_offset_ms = 2000
spawn_lead_ms = 0

chart = anamone_chart.chart_notes

def start_identity_part4(screen):
    global score
    score = 0
    global combo
    combo = 0
    max_combo = 0
    global skin_variant
    skin_variant = 0
    running = True
    chart_index = 0
    notes = []

    pygame.mixer.music.load("/Users/evaldsberzins/pygame/RayRhythm/Charts/anamone/anamone-chart.wav")
    pygame.mixer.music.set_volume(0.05)
    HitSound.set_volume(0.2)
    ComboBreak.set_volume(0.2)
    
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
                                if combo > max_combo:
                                    max_combo = combo
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

        for n in notes:
            if not n["hit"] and n["y"] > target_y_coordinate + 100:
                if combo >= 3:
                    ComboBreak.play()
                if combo > max_combo:
                    max_combo = combo
                combo = 0
                n["hit"] = True

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

            Max_Combo = result_screen_font(45).render(f"Your max combo: {max_combo}", True, "White")
            Max_Combo_Rect = Max_Combo.get_rect(center=(840, 550))
            screen.blit(Max_Combo, Max_Combo_Rect)

            EXIT_BUTTON = Button(image=None, pos=(840, 750), text_input="Exit level", font = pygame.font.Font(None, 80), base_color="White", hovering_color="White")
            EXIT_BUTTON.changeColor(PLAY_MOUSE_POS)
            EXIT_BUTTON.update(screen)

        pygame.display.flip()

        if keys[pygame.K_ESCAPE]:
            running = False