import pygame, sys
from button import Button
import time

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

IdentityBackground = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/Charts/IdentityBG.png")
GameplayOverlay = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/gameplay-field.png")
PressedCircle = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/circle_pressed.png")
RegularCirlce = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/circle_regular.png")
FallingNote = pygame.image.load("/Users/evaldsberzins/pygame/RayRhythm/graphics/circle_regular.png")

chart_lanes = [890, 1070, 1250, 1430]
player_keys = [pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k]
note_speed = 30
target_y_coordinate = 880
score = 0

music_offset_ms = 650
spawn_lead_ms = 0

chart = [
    {"time": 3426, "lane": 0}, #1
    {"time": 3533, "lane": 1}, #2
    {"time": 3670, "lane": 2}, #3
    {"time": 3855, "lane": 3}, #4
    {"time": 4069, "lane": 0}, #4
    {"time": 4176, "lane": 3}, #5
    {"time": 4283, "lane": 0}, #6
    {"time": 4390, "lane": 3}, #6
    {"time": 4497, "lane": 0}, #7
    {"time": 4712, "lane": 3}, #8
]

def start_identity_part4(screen):
    global score
    score = 0
    running = True
    chart_index = 0
    notes = []

    pygame.mixer.music.load("/Users/evaldsberzins/pygame/RayRhythm/Charts/identity-par4-4.wav")
    pygame.mixer.music.set_volume(0.2)
    
    music_started = False
    music_start_time = None
    level_start_time = pygame.time.get_ticks()
    # pygame.mixer_music.play()

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
                                closest_note["hit"] = True
                            elif closest_dist <= 100:
                                score += 50
                                closest_note["hit"] = True
                            elif closest_dist <= 200:
                                score += 25
                                closest_note["hit"] = True
        
        for n in notes:
            n["y"] += note_speed

        notes = [n for n in notes if n["y"] < 1050 and not n["hit"]]

        screen.blit(IdentityBackground, (0, 0))
        screen.blit(GameplayOverlay, (0, 0)) 
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

        font = pygame.font.Font(None, 60)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (100, 100))

        pygame.display.flip()

        if keys[pygame.K_ESCAPE]:
            running = False
