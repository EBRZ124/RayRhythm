import pygame, sys
from button import Button
import time
from Charts.anamone import anamone_chart

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

AnamoneBG = pygame.image.load("/RayRhythm/Charts/anamone/IdentityBG.png")
GameplayOverlay = pygame.image.load("/RayRhythm/graphics/gameplay-field.png")

# Circle skin assets
PressedCircle = pygame.image.load("/RayRhythm/graphics/circle_pressed.png")
RegularCirlce = pygame.image.load("/RayRhythm/graphics/circle_regular.png")
PlayingCircle = pygame.image.load("/RayRhythm/graphics/playing-circle.png")
FallingNote = pygame.image.load("/RayRhythm/graphics/circle_regular.png")

# Result screen
ResultScreen = pygame.image.load("/RayRhythm/graphics/result-screen.png")

# Fonts
def result_screen_font(size):
    return pygame.font.Font("/RayRhythm/fonts/capitolcity.ttf", size)

# Rayman skin assets
PressedRaymanCircle = pygame.image.load("/RayRhythm/graphics/pressed-rayman-circle.png")
RegularRaymanCircle = pygame.image.load("/RayRhythm/graphics/regular-rayman-circle.png")
FallingRaymanCircle = pygame.image.load("/RayRhythm/graphics/regular-rayman-circle.png")

# Sound effects
HitSound = pygame.mixer.Sound("/RayRhythm/Charts/hit-sound.wav")
ComboBreak = pygame.mixer.Sound("/RayRhythm/Charts/combo-break.wav")
click_SFX = pygame.mixer.Sound("/RayRhythm/sounds/click-sound.wav")
click_SFX.set_volume(0.6)

chart_lanes = [890, 1070, 1250, 1430]
player_keys = [pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k]
note_speed = 50
target_y_coordinate = 880
score = 0
combo = 0
max_combo = 0
accuracy = 100.00

music_offset_ms = 2000
spawn_lead_ms = 0

chart = anamone_chart.chart_notes

def show_result_screen(screen, final_score, final_max_combo, play_accuracy):
    result_screen = True
    while result_screen:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(AnamoneBG, (0, 0))
        screen.blit(ResultScreen, (0, 0))

        Final_Score_Text = result_screen_font(45).render(f"Total score: {final_score}", True, "White")
        Final_Score_Rect = Final_Score_Text.get_rect(center=(840, 430))
        screen.blit(Final_Score_Text, Final_Score_Rect)

        Max_Combo = result_screen_font(45).render(f"Your max combo: {final_max_combo}", True, "White")
        Max_Combo_Rect = Max_Combo.get_rect(center=(840, 530))
        screen.blit(Max_Combo, Max_Combo_Rect)

        Final_acc = result_screen_font(45).render(f"Accuracy: {play_accuracy}%", True, "White")
        Final_acc_Rect = Final_acc.get_rect(center=(840, 630))
        screen.blit(Final_acc, Final_acc_Rect)

        EXIT_BUTTON = Button(image=pygame.image.load("/RayRhythm/graphics/exit-result-button.png"), 
                             pos=(840, 750), text_input="Exit level", font = pygame.font.Font(None, 80), base_color="White", hovering_color="#9FDAEE")
        EXIT_BUTTON.changeColor(PLAY_MOUSE_POS)
        EXIT_BUTTON.update(screen)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EXIT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    click_SFX.play()
                    result_screen = False
        
        pygame.display.update()

def start_anamone(screen, skin_used):
    global score
    score = 0
    global combo
    global skin_variant
    global accuracy
    skin_variant = skin_used
    max_combo = 0
    running = True
    max_level_combo = 382
    chart_index = 0
    notes = []

    pygame.mixer.music.load("/RayRhythm/Charts/anamone/anamone-chart.wav")
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
                            if closest_dist <= 100:
                                combo += 1
                                score += 100 * combo
                                closest_note["hit"] = True
                            elif closest_dist <= 200:
                                combo += 1
                                score += 50 * combo
                                accuracy -= (25/max_level_combo)
                                closest_note["hit"] = True
                            elif closest_dist <= 300:
                                combo += 1
                                score += 25 * combo
                                accuracy -= (50/max_level_combo)
                                closest_note["hit"] = True
                            elif closest_dist <= 400:
                                if combo >= 3:
                                    ComboBreak.play()
                                if combo > max_combo:
                                    max_combo = combo
                                accuracy -= (100/max_level_combo)
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
                accuracy -= (100/max_level_combo)
                combo = 0
                n["hit"] = True

        notes = [n for n in notes if n["y"] < 1050 and not n["hit"]]

        screen.blit(AnamoneBG, (0, 0))
        screen.blit(GameplayOverlay, (0, 0)) 

        if skin_variant == 0:
            screen.blit(PlayingCircle, (890, 880))
            screen.blit(PlayingCircle, (1070, 880))
            screen.blit(PlayingCircle, (1250, 880))
            screen.blit(PlayingCircle, (1430, 880))
            for x in chart_lanes:
                screen.blit(PlayingCircle, (x, target_y_coordinate))
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

        combo_text = font.render(f"Combo: {combo}x", True, (255, 255, 255))
        screen.blit(combo_text, (100, 150))

        rounded_acc = round(accuracy, 2)
        combo_text = font.render(f"{rounded_acc}%", True, (255, 255, 255))
        screen.blit(combo_text, (100, 200))
        # ----------------LEVEL FINISHED----------------
        if combo > max_combo:
            max_combo = combo

        level_done = (
            chart_index >= len(chart) and
            len(notes) == 0 and
            music_started and
            not pygame.mixer.music.get_busy()
        )

        if level_done:
            show_result_screen(screen, score, max_combo, rounded_acc)
            running = False

        pygame.display.update()

        if keys[pygame.K_ESCAPE]:
            running = False
            pygame.mixer_music.stop()
            pygame.mixer_music.load("/RayRhythm/sounds/level_select_music.mp3")
            pygame.mixer_music.set_volume(0.3)
            pygame.mixer_music.play()