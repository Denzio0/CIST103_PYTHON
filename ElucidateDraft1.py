import pygame
import random
import sys
import math
import time
import binascii
from datetime import datetime

#key1 : 616c70686120312e30  // Alpha
#key2 : 6265746120312e30    // Beta

def elucidate(key):

    pygame.init()

    screen_x, screen_y = 1275, 710
    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption("Elucidate RPG (alpha 1.0.87)")
    clock = pygame.time.Clock()

    sys_bg_color = (0, 0, 0)

    walls = []

    def wall(x, y, w, h):
        walls.append(pygame.Rect(x, y, w, h))

    def exit_game():
        pygame.quit()
        sys.exit()

    def display():
        pygame.display.flip()

    def gametick(n):
        clock.tick(n)

    def JAV_001(text):
        try:
            text = text.replace(" ", "")
            bytes_object = bytes.fromhex(text)
            return bytes_object.decode('utf-8')
        except ValueError:
            return "there was an error while generating this text."

    def static_text(text, color, position, size):
        t = str(text)
        t = JAV_001(t)
        font = pygame.font.SysFont("Times New Roman", size)
        text_surface = font.render(t, True, (color[0], color[1], color[2]))
        screen.blit(text_surface, (position[0], position[1]))

    def touple_static_text(*t, color, position, size):
        font = pygame.font.SysFont("Times New Roman", size)
        text_surface = font.render(" ".join(map(str, t)), True, (color[0], color[1], color[2]))
        screen.blit(text_surface, (position[0], position[1]))

    def sys_function_screen_border():
        pygame.draw.rect(screen, (80, 80, 80), (0, 0, screen_x, screen_y), 1)

    def sys_function_playable_screen_border():
        pygame.draw.rect(screen, (120, 120, 120), (0, 0, 1010, 710), 1)

    def sys_function_mouse_loc():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (0, 255, 0), (mouse_x, 0, 1, 10000))
        pygame.draw.rect(screen, (0, 255, 0), (0, mouse_y, 10000, 1))

    def sys_function_data():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        touple_static_text((mouse_x, mouse_y), color=(0, 255, 0), position=(mouse_x, mouse_y), size=15)
        touple_static_text(clock, color=(0, 255, 0), position=(mouse_x, mouse_y + 15), size=15)

    def sys_function_loading():
        screen.fill(sys_bg_color)
        sys_function_screen_border()
        sys_function_playable_screen_border()
        static_text("4c6f6164696e672e2e2e", color=(255, 255, 255), position=(20, screen_y - 55), size=40)
        display()
        time.sleep(1)

    def handle_quit_event(event):
        if event.type == pygame.QUIT:
            exit_game()

    def resolve_collision(mover, obstacle):
        if not mover.colliderect(obstacle):
            return mover.x, mover.y

        overlap_left  = mover.right   - obstacle.left
        overlap_right = obstacle.right - mover.left
        overlap_top   = mover.bottom  - obstacle.top
        overlap_bot   = obstacle.bottom - mover.top

        min_x = overlap_left  if overlap_left  < overlap_right else -overlap_right
        min_y = overlap_top   if overlap_top   < overlap_bot   else -overlap_bot

        if abs(min_x) < abs(min_y):
            return mover.x - min_x, mover.y
        else:
            return mover.x, mover.y - min_y

    sys_function_loading()

    if key == '616c70686120312e30':
        while True:
            screen.fill(sys_bg_color)
            sys_function_mouse_loc()
            sys_function_playable_screen_border()
            sys_function_mouse_loc()
            sys_function_data()

            for event in pygame.event.get():
                handle_quit_event(event)

            display()
            gametick(60)

    else:
        while True:
            screen.fill(sys_bg_color)
            sys_function_screen_border()
            sys_function_playable_screen_border()

            static_text("7379732e6c6f6720c2bb202e2e2e", color=(255, 255, 255), position=(20, 20), size=15)
            static_text("7379732e6c6f6720c2bb206572726f72203a206b657920697320696e76616c69642e", color=(255, 255, 255), position=(20, 35), size=15)
            font_small = pygame.font.SysFont("Times New Roman", 15)
            key_surf = font_small.render(f"  key = '{key}'", True, (180, 80, 80))
            screen.blit(key_surf, (20, 50))

            rect_exit = pygame.draw.rect(screen, (120, 120, 120), (1010, 0, 265, 20), 1)
            static_text("45786974", color=(255, 255, 255), position=(1020, 2), size=15)

            rect_mobility = pygame.draw.rect(screen, (120, 120, 120), (1010, 20, 265, 20), 1)
            static_text("4d6f62696c69747920546573742041726561", color=(255, 255, 255), position=(1020, 22), size=15)

            rect_collision = pygame.draw.rect(screen, (120, 120, 120), (1010, 40, 265, 20), 1)
            static_text("436f6c6c6973696f6e20546573742041726561", color=(255, 255, 255), position=(1020, 42), size=15)

            for event in pygame.event.get():
                handle_quit_event(event)

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if rect_exit.collidepoint(event.pos):
                        for countdown, y_off in [
                            ("7379732e6c6f6720c2bb20636c6f73696e672067616d6520696e20332e2e2e", 65),
                            ("7379732e6c6f6720c2bb20636c6f73696e672067616d6520696e20322e2e2e", 80),
                            ("7379732e6c6f6720c2bb20636c6f73696e672067616d6520696e20312e2e2e", 95),
                        ]:
                            static_text(countdown, color=(255, 255, 255), position=(20, y_off), size=15)
                            display()
                            time.sleep(1)
                        exit_game()

                    elif rect_collision.collidepoint(event.pos):
                        sys_function_loading()
                        running     = True
                        px, py      = 1.0, 305.0
                        BASE_SPEED  = 5
                        PLAY_W      = 1010
                        PLAY_H      = 710
                        PLAYER_SIZE = 40
                        
                        while running:
                            screen.fill(sys_bg_color)
                            sys_function_screen_border()
                            sys_function_playable_screen_border()

                            player_rect = pygame.Rect(int(px), int(py), PLAYER_SIZE, PLAYER_SIZE)

                            for w in walls:
                                pygame.draw.rect(screen, (80,80,80), w)

                            pygame.draw.rect(screen, (120, 0, 0), player_rect)

                            rect_exit_col = pygame.draw.rect(screen, (120,120,120),(1010,0,265,20),1)
                            static_text("4578697420436f6c6c6973696f6e2054657374", color=(255,255,255), position=(1020,2), size=15)

                            rect_map1_col = pygame.draw.rect(screen,(120,120,120),(1010,60,265,20),1)
                            static_text("6d61702031", color=(255,255,255), position=(1020,62), size=15)

                            rect_map2_col = pygame.draw.rect(screen,(120,120,120),(1010,80,265,20),1)
                            static_text("6d61702032", color=(255,255,255), position=(1020,82), size=15)

                            rect_map3_col = pygame.draw.rect(screen,(120,120,120),(1010,100,265,20),1)
                            static_text("6d61702033", color=(255,255,255), position=(1020,102), size=15)
                            
                            rect_map4_col = pygame.draw.rect(screen,(120,120,120),(1010,120,265,20),1)
                            static_text("6d61702034", color=(255,255,255), position=(1020,122), size=15)

                            for event in pygame.event.get():
                                handle_quit_event(event)
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if rect_exit_col.collidepoint(event.pos):
                                        running = False

                                    elif rect_map1_col.collidepoint(event.pos):
                                        walls.clear()
                                        wall(0,0,1010,50)
                                        wall(0,660,1010,50)
                                        px, py = 1.0,325.0

                                    elif rect_map2_col.collidepoint(event.pos):
                                        walls.clear()
                                        wall(200,200,600,50)
                                        wall(200,450,600,50)
                                        px, py = 1.0,325.0

                                    elif rect_map3_col.collidepoint(event.pos):
                                        walls.clear()
                                        wall(300,150,50,400)
                                        wall(650,150,50,400)
                                        px, py = 1.0,325.0
                                    
                                    elif rect_map4_col.collidepoint(event.pos):
                                        walls.clear()
                                        wall(0, 0, 300, 50)
                                        wall(0, 0, 50, 300)
                                        wall(0, 660, 300, 50)
                                        wall(0, 360, 50, 300)
                                        wall(710, 0, 300, 50)
                                        wall(960, 0, 50, 300)
                                        wall(710, 660, 300, 50)
                                        wall(960, 360, 50, 300)
                                        px, py = 1.0,325.0

                            keys = pygame.key.get_pressed()
                            dx, dy = 0, 0
                            speed = BASE_SPEED

                            if keys[pygame.K_w]: dy -= speed
                            if keys[pygame.K_s]: dy += speed
                            if keys[pygame.K_a]: dx -= speed
                            if keys[pygame.K_d]: dx += speed
                            if keys[pygame.K_UP]: dy -= speed
                            if keys[pygame.K_DOWN]: dy += speed
                            if keys[pygame.K_LEFT]: dx -= speed
                            if keys[pygame.K_RIGHT]: dx += speed

                            px += dx
                            for w in walls:
                                px, py = resolve_collision(pygame.Rect(int(px), int(py), PLAYER_SIZE, PLAYER_SIZE), w)

                            py += dy
                            for w in walls:
                                px, py = resolve_collision(pygame.Rect(int(px), int(py), PLAYER_SIZE, PLAYER_SIZE), w)

                            if px < 1:
                                px = PLAY_W - PLAYER_SIZE - 1
                            elif px + PLAYER_SIZE > PLAY_W - 1:
                                px = 1
                            if py < 1:
                                py = PLAY_H - PLAYER_SIZE - 1
                            elif py + PLAYER_SIZE > PLAY_H - 1:
                                py = 1

                            sys_function_mouse_loc()
                            sys_function_data()
                            display()
                            gametick(60)

                        sys_function_loading()

                    elif rect_mobility.collidepoint(event.pos):
                        sys_function_loading()

                        running     = True
                        px, py      = 1, 1
                        speed       = 5
                        PLAY_W      = 1010
                        PLAY_H      = 710
                        PLAYER_SIZE = 40

                        while running:
                            screen.fill(sys_bg_color)
                            sys_function_screen_border()
                            sys_function_playable_screen_border()

                            pygame.draw.rect(screen, (120, 0, 0), (px, py, PLAYER_SIZE, PLAYER_SIZE))

                            rect_exit_mob = pygame.draw.rect(screen, (120, 120, 120), (1010, 0, 265, 20), 1)
                            static_text("45786974204d6f62696c6974792054657374", color=(255, 255, 255), position=(1020, 2), size=15)

                            touple_static_text("Player Speed : "+str(speed), color=(255, 255, 255), position=(1020, 42), size=15)

                            btn_add_speed = pygame.draw.rect(screen, (120, 120, 120), (1010, 60, 265, 20), 1)
                            static_text("41646420706c617965722062617365207370656564205b355d", color=(255, 255, 255), position=(1020, 62), size=15)

                            btn_red_speed = pygame.draw.rect(screen, (120, 120, 120), (1010, 80, 265, 20), 1)
                            static_text("52656475636520706c617965722062617365207370656564205b2d355d", color=(255, 255, 255), position=(1020, 82), size=15)

                            for event in pygame.event.get():
                                handle_quit_event(event)
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if rect_exit_mob.collidepoint(event.pos):
                                        running = False
                                    elif btn_add_speed.collidepoint(event.pos):
                                        speed += 5
                                    elif btn_red_speed.collidepoint(event.pos):
                                        speed -= 5

                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_w]: py -= speed
                            if keys[pygame.K_s]: py += speed
                            if keys[pygame.K_a]: px -= speed
                            if keys[pygame.K_d]: px += speed
                            if keys[pygame.K_UP]: py -= speed
                            if keys[pygame.K_DOWN]: py += speed
                            if keys[pygame.K_LEFT]: px -= speed
                            if keys[pygame.K_RIGHT]: px += speed

                            if px < 1:
                                px = PLAY_W - PLAYER_SIZE - 1
                            elif px + PLAYER_SIZE > PLAY_W - 1:
                                px = 1
                            if py < 1:
                                py = PLAY_H - PLAYER_SIZE - 1
                            elif py + PLAYER_SIZE > PLAY_H - 1:
                                py = 1

                            sys_function_mouse_loc()
                            sys_function_data()
                            display()
                            gametick(60)

                        sys_function_loading()

            sys_function_mouse_loc()
            sys_function_data()
            display()
            gametick(60)

elucidate('b616c70686120312e30')
