#!/usr/bin/env python3
from core.config import Config

config = Config()
import os

# Don't let SDL/Pygame grab the audio device
os.environ["SDL_AUDIODRIVER"] = "dummy"

import sys
import pygame

pygame.init()

DISPLAY = pygame.display.Info()
SCREEN_W = DISPLAY.current_w
SCREEN_H = DISPLAY.current_h

# Internal rendering resolution
RENDER_W = 1280
RENDER_H = 720

screen = pygame.display.set_mode(
    (SCREEN_W, SCREEN_H),
    pygame.FULLSCREEN
)

virtual = pygame.Surface((RENDER_W, RENDER_H))

pygame.display.set_caption("SnapDisplay")

clock = pygame.time.Clock()

TITLE = pygame.font.SysFont("DejaVu Sans", 60, bold=True)
SMALL = pygame.font.SysFont("DejaVu Sans", 28)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

    # Draw everything to the virtual screen
    virtual.fill((8, 8, 8))

    title = TITLE.render("SnapDisplay", True, (255, 255, 255))
    version = SMALL.render("Version 0.1.1", True, (180, 180, 180))
    status = SMALL.render("Waiting for Home Assistant...", True, (120, 220, 255))

    virtual.blit(
        title,
        (
            RENDER_W // 2 - title.get_width() // 2,
            RENDER_H // 2 - 90
        )
    )

    virtual.blit(
        version,
        (
            RENDER_W // 2 - version.get_width() // 2,
            RENDER_H // 2
        )
    )

    virtual.blit(
        status,
        (
            RENDER_W // 2 - status.get_width() // 2,
            RENDER_H // 2 + 60
        )
    )

    # Scale to the display
    pygame.transform.smoothscale(
        virtual,
        (SCREEN_W, SCREEN_H),
        screen
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
