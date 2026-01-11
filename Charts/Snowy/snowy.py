import pygame, sys
from button import Button
import time
from Charts.Snowy import snowy_chart
import global_variables

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen_scale = global_variables.global_scaler

played_result_screen_sound = False

# Sound effects
ComboBreak = global_variables.combo_braek
click_SFX = global_variables.click_sound
click_SFX.set_volume(0.6)

if(screen_scale == 1):
    music_offset_ms = 3360
if(screen_scale == 0.7):
    music_offset_ms = 3020
if(screen_scale == 0.5):
    music_offset_ms = 3040
spawn_lead_ms = 0

chart = snowy_chart.snowy_level_notes

def show_result_screen(screen, final_score, final_max_combo, play_accuracy):
    result_screen = True
    global played_result_screen_sound
    while result_screen:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(global_variables.images["snowy_background"], (0, 0))
        screen.blit(global_variables.images["result_screen"], (0, 0))

        Final_Score_Text = global_variables.result_screen_font(int(45*screen_scale)).render(f"Total score: {final_score}", True, "White")
        Final_Score_Rect = Final_Score_Text.get_rect(center=(840*screen_scale, 430*screen_scale))
        screen.blit(Final_Score_Text, Final_Score_Rect)

        Max_Combo = global_variables.result_screen_font(int(45*screen_scale)).render(f"Your max combo: {final_max_combo}", True, "White")
        Max_Combo_Rect = Max_Combo.get_rect(center=(840*screen_scale, 530*screen_scale))
        screen.blit(Max_Combo, Max_Combo_Rect)

        Final_acc = global_variables.result_screen_font(int(45*screen_scale)).render(f"Accuracy: {play_accuracy}%", True, "White")
        Final_acc_Rect = Final_acc.get_rect(center=(840*screen_scale, 630*screen_scale))
        screen.blit(Final_acc, Final_acc_Rect)

        if(play_accuracy == 100.00):
            ss_rank_image = global_variables.images["ss_rank"]
            screen.blit(ss_rank_image, (1075*screen_scale, 442*screen_scale))
            if not played_result_screen_sound:
                global_variables.ss_sound_effect.play()
                played_result_screen_sound = True

        elif(play_accuracy<100.00 and play_accuracy>=93.00):
            s_rank_image = global_variables.images["s_rank"]
            screen.blit(s_rank_image, (1085*screen_scale, 442*screen_scale))
            if not played_result_screen_sound:
                global_variables.s_sound_effect.play()
                played_result_screen_sound = True

        elif(play_accuracy<93.00 and play_accuracy>=80.00):
            a_rank_image = global_variables.images["a_rank"]
            screen.blit(a_rank_image, (1085*screen_scale, 442*screen_scale))
            if not played_result_screen_sound:
                global_variables.a_sound_effect.play()
                played_result_screen_sound = True

        elif(play_accuracy<80.00 and play_accuracy>=70.00):
            b_rank_image = global_variables.images["b_rank"]
            screen.blit(b_rank_image, (1085*screen_scale, 442*screen_scale))
            if not played_result_screen_sound:
                global_variables.b_sound_effect.play()
                played_result_screen_sound = True

        elif(play_accuracy<70.00 and play_accuracy>=50.00):
            c_rank_image = global_variables.images["c_rank"]
            screen.blit(c_rank_image, (1085*screen_scale, 442*screen_scale))
            if not played_result_screen_sound:
                global_variables.c_sound_effect.play()
                played_result_screen_sound = True

        elif(play_accuracy<50.00):
            d_rank_image = global_variables.images["d_rank"]
            screen.blit(d_rank_image, (1085*screen_scale, 442*screen_scale))
            if not played_result_screen_sound:
                global_variables.d_sound_effect.play()
                played_result_screen_sound = True

        EXIT_BUTTON = Button(image=global_variables.images["exit_button_results"], pos=(840*screen_scale, 750*screen_scale), text_input="Exit level", font = global_variables.get_level_name_font(int(50*screen_scale)), base_color="White", hovering_color="#9FDAEE")
        EXIT_BUTTON.changeColor(PLAY_MOUSE_POS)
        EXIT_BUTTON.update(screen)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EXIT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    click_SFX.play()
                    pygame.mixer_music.stop()
                    music_volume = 0.3
                    pygame.mixer_music.set_volume(music_volume)
                    pygame.mixer.music.load(global_variables.level_select_music)
                    pygame.mixer_music.play()
                    played_result_screen_sound = False
                    result_screen = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    result_screen = False  
                    played_result_screen_sound = False
        
        pygame.display.update()

def start_snowy(screen, skin_used, screen_scale_passed):
    global skin_variant, screen_scale
    screen_scale = screen_scale_passed
    max_level_combo = 176
    circles_fallen = 0
    skin_variant = skin_used
    running = False
    ShowStartScreen = True
    chart_index = 0
    notes = []

    chart_lanes = [890*screen_scale, 1070*screen_scale, 1250*screen_scale, 1430*screen_scale]
    player_keys = [pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k]
    note_speed = 20*screen_scale
    target_y_coordinate = 880*screen_scale
    score = 0
    combo = 0
    max_combo = 0
    accuracy = 100.00 

    if (skin_variant==0):
        HitSound = global_variables.hit_sound
    elif(skin_variant==1):
        HitSound = global_variables.rayman_sound
    elif(skin_variant==2):
        HitSound = global_variables.gat_sound

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
                if event.key == pygame.K_ESCAPE:
                    ShowStartScreen = False
                    pygame.mixer_music.load(global_variables.level_select_music)
                    pygame.mixer_music.set_volume(0.3)
                    pygame.mixer_music.play()

        screen.blit(global_variables.images["snowy_background"], (0, 0))
        screen.blit(global_variables.images["gameplay_overlay"], (0, 0))
        screen.blit(global_variables.images["start_screen"], (0, 0))

        pygame.display.flip()
        clock.tick(60)

    pygame.mixer.music.load(global_variables.snowy_song)
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

        screen.blit(global_variables.images["snowy_background"], (0, 0))
        screen.blit(global_variables.images["gameplay_overlay"], (0, 0))

        if skin_variant == 0:
            screen.blit(global_variables.images["playing_circle"], (890*screen_scale, 880*screen_scale))
            screen.blit(global_variables.images["playing_circle"], (1070*screen_scale, 880*screen_scale))
            screen.blit(global_variables.images["playing_circle"], (1250*screen_scale, 880*screen_scale))
            screen.blit(global_variables.images["playing_circle"], (1430*screen_scale, 880*screen_scale))
            for x in chart_lanes:
                screen.blit(global_variables.images["playing_circle"], (x, target_y_coordinate))
            for n in notes:
                x = chart_lanes[n["lane"]]
                screen.blit(global_variables.images["regular_circle"], (x, n["y"]))
            keys = pygame.key.get_pressed()
            for lane, key in enumerate(player_keys):
                if keys[key]:
                    screen.blit(global_variables.images["pressed_circle"], (chart_lanes[lane], target_y_coordinate))

        if skin_variant == 1:
            screen.blit(global_variables.images["regular_rayman_circle"], (890*screen_scale, 880*screen_scale))
            screen.blit(global_variables.images["regular_rayman_circle"], (1070*screen_scale, 880*screen_scale))
            screen.blit(global_variables.images["regular_rayman_circle"], (1250*screen_scale, 880*screen_scale))
            screen.blit(global_variables.images["regular_rayman_circle"], (1430*screen_scale, 880*screen_scale))
            for x in chart_lanes:
                screen.blit(global_variables.images["regular_rayman_circle"], (x, target_y_coordinate))
            for n in notes:
                x = chart_lanes[n["lane"]]
                screen.blit(global_variables.images["regular_rayman_circle"], (x, n["y"]))
            keys = pygame.key.get_pressed()
            for lane, key in enumerate(player_keys):
                if keys[key]:
                    screen.blit(global_variables.images["pressed_rayman_circle"], (chart_lanes[lane], target_y_coordinate))

        if skin_variant == 2:
            screen.blit(global_variables.images["regular_soprano_circle"], (890*screen_scale, 880*screen_scale))
            screen.blit(global_variables.images["regular_soprano_circle"], (1070*screen_scale, 880*screen_scale))
            screen.blit(global_variables.images["regular_soprano_circle"], (1250*screen_scale, 880*screen_scale))
            screen.blit(global_variables.images["regular_soprano_circle"], (1430*screen_scale, 880*screen_scale))
            for x in chart_lanes:
                screen.blit(global_variables.images["regular_soprano_circle"], (x, target_y_coordinate))
            for n in notes:
                x = chart_lanes[n["lane"]]
                screen.blit(global_variables.images["regular_soprano_circle"], (x, n["y"]))
            keys = pygame.key.get_pressed()
            for lane, key in enumerate(player_keys):
                if keys[key]:
                    screen.blit(global_variables.images["pressed_soprano_circle"], (chart_lanes[lane], target_y_coordinate))

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
            pygame.mixer_music.stop()
            pygame.mixer_music.load(global_variables.level_select_music)
            pygame.mixer_music.set_volume(0.3)
            pygame.mixer_music.play()
            running = False