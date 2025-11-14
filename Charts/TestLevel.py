import pygame, sys, random
from button import Button
import time

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

TestBackground = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/Charts/test-level-background.png")
GameplayOverlay = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/gameplay-field.png")

# Circle skin assets
PressedCircle = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/circle_pressed.png")
RegularCirlce = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/circle_regular.png")
FallingNote = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/circle_regular.png")


# Rayman skin assets
PressedRaymanCircle = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/pressed-rayman-circle.png")
RegularRaymanCircle = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/regular-rayman-circle.png")
FallingRaymanCircle = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/regular-rayman-circle.png")

# Sound effects
HitSound = pygame.mixer.Sound("/Users/evaldsberzins/pygame/RayRhythm/Charts/hit-sound.wav")
ComboBreak = pygame.mixer.Sound("/Users/evaldsberzins/pygame/RayRhythm/Charts/combo-break.wav")

chart_lanes = [890, 1070, 1250, 1430]
player_keys = [pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k]
note_speed = 20
target_y_coordinate = 880
score = 0
combo = 0

music_offset_ms = 2000
spawn_lead_ms = 0

skin_variant = 0

chart = [
    {"time": 900, "lane": 0}, #1
    {"time": 1328, "lane": 1}, #2
    {"time": 1756, "lane": 2}, #3
    {"time": 2148, "lane": 3}, #4
    {"time": 2148, "lane": 2}, #4
    {"time": 2576, "lane": 2}, #5
    {"time": 3004, "lane": 3}, #6
    {"time": 3004, "lane": 2}, #6
    {"time": 3432, "lane": 2}, #7
    {"time": 3860, "lane": 3}, #8
    {"time": 3860, "lane": 2}, #8
    {"time": 4288, "lane": 0}, #9
    {"time": 4716, "lane": 2}, #10
    {"time": 5144, "lane": 1}, #11
    {"time": 5527, "lane": 2}, #12
    {"time": 6000, "lane": 2}, #13
    {"time": 6428, "lane": 1}, #14
    {"time": 6856, "lane": 3}, #15
    {"time": 7284, "lane": 1}, #16
    {"time": 7712, "lane": 3}, #17
    {"time": 8140, "lane": 2}, #18
    {"time": 8568, "lane": 1}, #19
    {"time": 8996, "lane": 0}, #20
    {"time": 9424, "lane": 0}, #21
    {"time": 9852, "lane": 1}, #22
    {"time": 10280, "lane": 0}, #23
    {"time": 10708, "lane": 0}, #24
    {"time": 11136, "lane": 2}, #25
    {"time": 11564, "lane": 0}, #26
    {"time": 11992, "lane": 0}, #27
    {"time": 12420, "lane": 3}, #28
    {"time": 12848, "lane": 2}, #29
    {"time": 13276, "lane": 3}, #30
    {"time": 13276, "lane": 2}, #30
    {"time": 13704, "lane": 3}, #31
    {"time": 13704, "lane": 2}, #31
    {"time": 14132, "lane": 3}, #32
    {"time": 14132, "lane": 2}, #32
]

def start_test_level(screen):
    global score
    score = 0
    global combo
    combo = 0
    global skin_variant
    skin_variant = 1
    running = True
    chart_index = 0
    notes = []

    pygame.mixer.music.load("/Users/evaldsberzins/pygame/RayRhythm/Charts/test-level.wav")
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

        screen.blit(TestBackground, (0, 0))
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

        pygame.display.flip()

        if keys[pygame.K_ESCAPE]:
            running = False
