import pygame, sys, random
from button import Button
import time
from Charts.TestLevel import TestLevel_chart
import global_variables

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen_scale = global_variables.global_scaler

TestBackground = global_variables.test_background
GameplayOverlay = global_variables.gameplay_overlay
StartScreen = global_variables.start_screen

# Circle skin assets
PressedCircle = global_variables.pressed_circle
RegularCirlce = global_variables.regular_circle
PlayingCircle = global_variables.playing_circle
FallingNote = global_variables.regular_circle

# Rayman skin assets
PressedRaymanCircle = global_variables.pressed_rayman_circle
RegularRaymanCircle = global_variables.regular_rayman_circle
FallingRaymanCircle = global_variables.regular_rayman_circle

# Soprano skin assets
PressedSopranoCircle = global_variables.pressed_soprano_circle
RegularSopranoCircle = global_variables.regular_soprano_circle
FallingSopranoCircle = global_variables.regular_soprano_circle

# Result screen
ResultScreen = global_variables.result_screen

# Sound effects
HitSound = pygame.mixer.Sound("/RayRhythm/Charts/hit-sound.wav")
ComboBreak = pygame.mixer.Sound("/RayRhythm/Charts/combo-break.wav")
click_SFX = pygame.mixer.Sound("/RayRhythm/sounds/click-sound.wav")
click_SFX.set_volume(0.6)

chart_lanes = [890*screen_scale, 1070*screen_scale, 1250*screen_scale, 1430*screen_scale]
player_keys = [pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k]
note_speed = 20*screen_scale
target_y_coordinate = 880*screen_scale
score = 0
combo = 0
max_combo = 0
accuracy = 100.00 

# I got no clue why the delay differs (migh fix later)
if(screen_scale == 1):
    music_offset_ms = 2000
elif(screen_scale == 0.7):
    music_offset_ms = 1670
elif(screen_scale == 0.5):
    music_offset_ms = 1620

spawn_lead_ms = 0


skin_variant = 1

chart = TestLevel_chart.TestLevel_notes

def show_result_screen(screen, final_score, final_max_combo, play_accuracy):
    result_screen = True
    while result_screen:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(TestBackground, (0, 0))
        screen.blit(ResultScreen, (0, 0))

        Final_Score_Text = global_variables.result_screen_font(int(45*screen_scale)).render(f"Total score: {final_score}", True, "White")
        Final_Score_Rect = Final_Score_Text.get_rect(center=(840*screen_scale, 430*screen_scale))
        screen.blit(Final_Score_Text, Final_Score_Rect)

        Max_Combo = global_variables.result_screen_font(int(45*screen_scale)).render(f"Your max combo: {final_max_combo}", True, "White")
        Max_Combo_Rect = Max_Combo.get_rect(center=(840*screen_scale, 530*screen_scale))
        screen.blit(Max_Combo, Max_Combo_Rect)

        Final_acc = global_variables.result_screen_font(int(45*screen_scale)).render(f"Accuracy: {play_accuracy}%", True, "White")
        Final_acc_Rect = Final_acc.get_rect(center=(840*screen_scale, 630*screen_scale))
        screen.blit(Final_acc, Final_acc_Rect)

        EXIT_BUTTON = Button(image=global_variables.exit_button_results, pos=(840*screen_scale, 750*screen_scale), text_input="Exit level", font = pygame.font.Font (None, int(80*screen_scale)), base_color="White", hovering_color="#9FDAEE")
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

def start_test_level(screen, skin_used, screen_scale):
    global score
    global combo
    global accuracy
    accuracy = 100
    combo = 0
    score = 0
    max_combo = 0
    max_level_combo = 38
    circles_fallen = 0
    global skin_variant
    skin_variant = skin_used
    running = False
    ShowStartScreen = True
    chart_index = 0
    notes = []

    while ShowStartScreen:
        pygame.mixer_music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ShowStartScreen = False
                    running = True

        screen.blit(TestBackground, (0, 0))
        screen.blit(GameplayOverlay, (0, 0))
        screen.blit(StartScreen, (0, 0))

        pygame.display.flip()
        clock.tick(60)


    pygame.mixer.music.load("/RayRhythm/Charts/TestLevel/test-level.wav")
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
            circles_fallen += 1

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
                            if closest_dist <= 100*screen_scale:
                                combo += 1
                                score += 100 * combo
                                closest_note["hit"] = True
                            elif closest_dist <= 200*screen_scale:
                                combo += 1
                                score += 50 * combo
                                accuracy -= (25/max_level_combo)
                                closest_note["hit"] = True
                            elif closest_dist <= 300*screen_scale:
                                combo += 1
                                score += 25 * combo
                                accuracy -= (50/max_level_combo)
                                closest_note["hit"] = True
                            elif closest_dist <= 400*screen_scale:
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

        # If notes fall past the pressing area by 50px, it also counts as a miss
        for n in notes:
            if not n["hit"] and n["y"] > target_y_coordinate + 50:
                if combo >= 3:
                    ComboBreak.play()
                if combo > max_combo:
                    max_combo = combo
                accuracy -= (100/max_level_combo)
                combo = 0
                n["hit"] = True

        notes = [n for n in notes if n["y"] < 1050 and not n["hit"]]

        screen.blit(TestBackground, (0, 0))
        screen.blit(GameplayOverlay, (0, 0)) 

        if skin_variant == 0:
            screen.blit(PlayingCircle, (890*screen_scale, 880*screen_scale))
            screen.blit(PlayingCircle, (1070*screen_scale, 880*screen_scale))
            screen.blit(PlayingCircle, (1250*screen_scale, 880*screen_scale))
            screen.blit(PlayingCircle, (1430*screen_scale, 880*screen_scale))
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
            screen.blit(RegularRaymanCircle, (890*screen_scale, 880*screen_scale))
            screen.blit(RegularRaymanCircle, (1070*screen_scale, 880*screen_scale))
            screen.blit(RegularRaymanCircle, (1250*screen_scale, 880*screen_scale))
            screen.blit(RegularRaymanCircle, (1430*screen_scale, 880*screen_scale))
            for x in chart_lanes:
                screen.blit(RegularRaymanCircle, (x, target_y_coordinate))
            for n in notes:
                x = chart_lanes[n["lane"]]
                screen.blit(FallingRaymanCircle, (x, n["y"]))
            keys = pygame.key.get_pressed()
            for lane, key in enumerate(player_keys):
                if keys[key]:
                    screen.blit(PressedRaymanCircle, (chart_lanes[lane], target_y_coordinate))

        if skin_variant == 2:
            screen.blit(RegularSopranoCircle, (890*screen_scale, 880*screen_scale))
            screen.blit(RegularSopranoCircle, (1070*screen_scale, 880*screen_scale))
            screen.blit(RegularSopranoCircle, (1250*screen_scale, 880*screen_scale))
            screen.blit(RegularSopranoCircle, (1430*screen_scale, 880*screen_scale))
            for x in chart_lanes:
                screen.blit(RegularSopranoCircle, (x, target_y_coordinate))
            for n in notes:
                x = chart_lanes[n["lane"]]
                screen.blit(FallingSopranoCircle, (x, n["y"]))
            keys = pygame.key.get_pressed()
            for lane, key in enumerate(player_keys):
                if keys[key]:
                    screen.blit(PressedSopranoCircle, (chart_lanes[lane], target_y_coordinate))

        font = pygame.font.Font(None, int(60*screen_scale))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (100*screen_scale, 100*screen_scale))

        combo_text = font.render(f"Combo: {combo}x", True, (255, 255, 255))
        screen.blit(combo_text, (100*screen_scale, 150*screen_scale))

        rounded_acc = round(accuracy, 2)
        combo_text = font.render(f"{rounded_acc}%", True, (255, 255, 255))
        screen.blit(combo_text, (100*screen_scale, 200*screen_scale))
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