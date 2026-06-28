#!/usr/bin/env python3

import os
import sys

# Prevent SDL from stealing the audio device.
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame

from core.config import Config
from providers.homeassistant import HomeAssistant

VERSION = "0.1.3"

BACKGROUND = (8, 8, 8)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
GREEN = (80, 220, 120)
BLUE = (120, 220, 255)
RED = (220, 80, 80)


def main():

    config = Config()

    status_text = "Connecting..."
    status_colour = BLUE

    try:

        ha = HomeAssistant(
            config.get("homeassistant.url"),
            config.get("homeassistant.token")
        )

        if ha.connect():

            entity = ha.get_entity(
                config.get("musicassistant.player")
            )

            if entity:

                state = entity.get("state", "unknown")

                status_text = f"Player State: {state}"
                status_colour = GREEN

            else:

                status_text = "Player Not Found"
                status_colour = RED

        else:

            status_text = "Authentication Failed"
            status_colour = RED

    except Exception as e:

        print(e)

        status_text = str(e)
        status_colour = RED

    pygame.init()

    display = pygame.display.Info()

    screen = pygame.display.set_mode(
        (display.current_w, display.current_h),
        pygame.FULLSCREEN
    )

    pygame.display.set_caption("SnapDisplay")

    title_font = pygame.font.SysFont(
        "DejaVu Sans",
        60,
        bold=True
    )

    small_font = pygame.font.SysFont(
        "DejaVu Sans",
        28
    )

    clock = pygame.time.Clock()

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BACKGROUND)

        title = title_font.render(
            "SnapDisplay",
            True,
            WHITE
        )

        version = small_font.render(
            f"Version {VERSION}",
            True,
            GRAY
        )

        status = small_font.render(
            status_text,
            True,
            status_colour
        )

        screen.blit(
            title,
            (
                display.current_w // 2 - title.get_width() // 2,
                display.current_h // 2 - 90
            )
        )

        screen.blit(
            version,
            (
                display.current_w // 2 - version.get_width() // 2,
                display.current_h // 2
            )
        )

        screen.blit(
            status,
            (
                display.current_w // 2 - status.get_width() // 2,
                display.current_h // 2 + 60
            )
        )

        pygame.display.flip()

        clock.tick(
            config.get("display.fps", 60)
        )

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
